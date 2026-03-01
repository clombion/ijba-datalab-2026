// Contextual Recode Review Tool — Single IIFE
(function () {
  "use strict";

  // =========================================================================
  // 1. STATE & CONSTANTS
  // =========================================================================
  var RELEVANCE_VALUES = ["primary", "secondary", "tangential"];

  var allEpisodes = [];
  var codebook = {};         // { "T01": { name, sub_themes: { "T01.1": "name" } } }
  var allSubThemes = [];     // flat list: [{ id: "T01.1", name: "...", themeId: "T01" }, ...]
  var currentEpisode = 0;
  var decisions = {};
  var activeHighlightIdx = -1;  // index into current episode's sorted highlights
  var readonly = true;

  // New passage selection state
  var pendingSelection = null;  // { start, end, text }
  var passageCodeTempCodes = []; // temp codes for add-passage modal
  var passageCodeForModal = null; // "panel" or "passage" — which modal target

  // =========================================================================
  // 2. DATA LOADER
  // =========================================================================
  function loadData() {
    var el = document.getElementById("recode-data");
    var b64 = el.textContent.trim();
    var binary = atob(b64);
    var bytes = new Uint8Array(binary.length);
    for (var i = 0; i < binary.length; i++) {
      bytes[i] = binary.charCodeAt(i);
    }
    var decompressed = fflate.gunzipSync(bytes);
    var text = new TextDecoder().decode(decompressed);
    var data = JSON.parse(text);

    allEpisodes = data.episodes;
    codebook = data.codebook;

    // Build flat sub-theme list for fuzzy search
    allSubThemes = [];
    Object.keys(codebook).forEach(function (tid) {
      var theme = codebook[tid];
      Object.keys(theme.sub_themes).forEach(function (stid) {
        allSubThemes.push({ id: stid, name: theme.sub_themes[stid], themeId: tid });
      });
    });
    allSubThemes.sort(function (a, b) { return a.id.localeCompare(b.id); });
  }

  // =========================================================================
  // 3. HELPERS
  // =========================================================================
  function esc(s) {
    if (!s) return "";
    return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  function decisionKey(epIdx, themeId) {
    return "ep_" + epIdx + "_" + themeId;
  }

  function newPassageKey(epIdx) {
    // Find next available new passage index
    var i = 1;
    while (decisions["ep_" + epIdx + "_new_" + i]) i++;
    return "ep_" + epIdx + "_new_" + i;
  }

  function getDecision(epIdx, themeId) {
    return decisions[decisionKey(epIdx, themeId)];
  }

  function isValid(epIdx, themeId) {
    var dec = getDecision(epIdx, themeId);
    if (dec && dec.valid === false) return false;
    return true;
  }

  function getEffectiveRelevance(epIdx, match) {
    var dec = getDecision(epIdx, match.theme_id);
    if (dec && dec.relevance) return dec.relevance;
    return match.relevance || "tangential";
  }

  function getEffectiveCodes(epIdx, match) {
    var dec = getDecision(epIdx, match.theme_id);
    if (dec && dec.codes) return dec.codes;
    return match.sub_themes_present || [];
  }

  function totalCodings() {
    var n = 0;
    for (var i = 0; i < allEpisodes.length; i++) {
      n += allEpisodes[i].matches.length;
    }
    // Also count added passages
    Object.keys(decisions).forEach(function (key) {
      if (decisions[key].added) n++;
    });
    return n;
  }

  function totalReviewed() {
    return Object.keys(decisions).length;
  }

  function episodeReviewed(epIdx) {
    var ep = allEpisodes[epIdx];
    for (var i = 0; i < ep.matches.length; i++) {
      if (!decisions[decisionKey(epIdx, ep.matches[i].theme_id)]) return false;
    }
    return true;
  }

  // Get sorted highlights for current episode (matched passages + added passages)
  function getSortedHighlights(epIdx) {
    var ep = allEpisodes[epIdx];
    var highlights = [];

    // Machine-generated matches with positions
    ep.matches.forEach(function (m, i) {
      if (m.passage_start != null) {
        highlights.push({
          type: "match",
          matchIdx: i,
          themeId: m.theme_id,
          start: m.passage_start,
          end: m.passage_end,
          match: m
        });
      }
    });

    // Reviewer-added passages
    Object.keys(decisions).forEach(function (key) {
      var dec = decisions[key];
      if (!dec.added) return;
      // Check if belongs to this episode
      var prefix = "ep_" + epIdx + "_new_";
      if (key.indexOf(prefix) !== 0) return;
      highlights.push({
        type: "added",
        key: key,
        themeId: dec.theme_id,
        start: dec.passage_start,
        end: dec.passage_end,
        decision: dec
      });
    });

    // Sort by start position
    highlights.sort(function (a, b) { return a.start - b.start; });
    return highlights;
  }

  // Fuzzy match for code search
  function fuzzyMatch(query, text) {
    query = query.toLowerCase();
    text = text.toLowerCase();
    var qi = 0;
    for (var ti = 0; ti < text.length && qi < query.length; ti++) {
      if (text[ti] === query[qi]) qi++;
    }
    return qi === query.length;
  }

  // =========================================================================
  // 4. EPISODE NAVIGATION
  // =========================================================================
  function getVisibleEpisodes() {
    var hideReviewed = document.getElementById("hide-reviewed").checked;
    var indices = [];
    for (var i = 0; i < allEpisodes.length; i++) {
      if (hideReviewed && episodeReviewed(i)) continue;
      indices.push(i);
    }
    return indices;
  }

  function goToEpisode(epIdx) {
    if (epIdx < 0 || epIdx >= allEpisodes.length) return;
    currentEpisode = epIdx;
    activeHighlightIdx = -1;
    closePanel();
    renderEpisode();
    updateProgress();
    updateEpisodeCounter();
    window.scrollTo(0, 0);
  }

  function goToPrevEpisode() {
    var visible = getVisibleEpisodes();
    if (visible.length === 0) return;
    var curPos = visible.indexOf(currentEpisode);
    if (curPos > 0) {
      goToEpisode(visible[curPos - 1]);
    } else if (curPos === -1) {
      for (var i = visible.length - 1; i >= 0; i--) {
        if (visible[i] < currentEpisode) { goToEpisode(visible[i]); return; }
      }
      goToEpisode(visible[0]);
    }
  }

  function goToNextEpisode() {
    var visible = getVisibleEpisodes();
    if (visible.length === 0) return;
    var curPos = visible.indexOf(currentEpisode);
    if (curPos >= 0 && curPos < visible.length - 1) {
      goToEpisode(visible[curPos + 1]);
    } else if (curPos === -1) {
      for (var i = 0; i < visible.length; i++) {
        if (visible[i] > currentEpisode) { goToEpisode(visible[i]); return; }
      }
      goToEpisode(visible[visible.length - 1]);
    }
  }

  function updateEpisodeCounter() {
    var visible = getVisibleEpisodes();
    var pos = visible.indexOf(currentEpisode);
    document.getElementById("episode-counter").textContent =
      (pos >= 0 ? pos + 1 : "?") + " / " + visible.length;
  }

  // =========================================================================
  // 5. RENDER EPISODE
  // =========================================================================
  function renderEpisode() {
    var ep = allEpisodes[currentEpisode];
    renderEpisodeHeader(ep);
    renderTranscript(ep);
  }

  function renderEpisodeHeader(ep) {
    var guestHTML = "";
    for (var i = 0; i < ep.guests.length; i++) {
      var g = ep.guests[i];
      var label = esc(g.name);
      if (g.role) label += ", " + esc(g.role);
      if (g.organization) label += " &mdash; " + esc(g.organization);
      guestHTML += '<span class="guest-badge">' + label + '</span>';
    }

    var claimsHTML = "";
    if (ep.summary_claims && ep.summary_claims.length > 0) {
      claimsHTML = '<div class="ep-claims"><ul>';
      for (var j = 0; j < ep.summary_claims.length; j++) {
        claimsHTML += '<li>' + esc(ep.summary_claims[j]) + '</li>';
      }
      claimsHTML += '</ul></div>';
    }

    document.getElementById("episode-header").innerHTML =
      '<div class="ep-title">' + esc(ep.title) + '</div>' +
      '<div class="ep-meta">' +
        '<span class="ep-date">' + esc(ep.date) + '</span>' +
        '<span>Host: ' + esc(ep.host) + '</span>' +
        guestHTML +
      '</div>' +
      claimsHTML +
      '<div class="ep-legend">' +
        '<span class="legend-item"><span class="legend-swatch primary"></span> primary</span>' +
        '<span class="legend-item"><span class="legend-swatch secondary"></span> secondary</span>' +
        '<span class="legend-item"><span class="legend-swatch tangential"></span> tangential</span>' +
        '<span class="legend-item"><span class="legend-swatch invalid"></span> invalidated</span>' +
      '</div>';
  }

  function renderTranscript(ep) {
    var transcript = ep.transcript || "";
    if (!transcript) {
      document.getElementById("transcript-body").textContent = "(No transcript available)";
      return;
    }

    var highlights = getSortedHighlights(currentEpisode);

    // Build HTML with highlights inserted
    var html = "";
    var lastEnd = 0;

    // Remove overlapping highlights by keeping the first one in each overlapping group
    var nonOverlapping = [];
    for (var h = 0; h < highlights.length; h++) {
      var hl = highlights[h];
      if (hl.start == null || hl.end == null) continue;
      if (nonOverlapping.length === 0 || hl.start >= nonOverlapping[nonOverlapping.length - 1].end) {
        nonOverlapping.push(hl);
      }
    }

    for (var i = 0; i < nonOverlapping.length; i++) {
      var hi = nonOverlapping[i];
      var start = hi.start;
      var end = Math.min(hi.end, transcript.length);

      // Text before this highlight
      if (start > lastEnd) {
        html += esc(transcript.substring(lastEnd, start));
      }

      // Determine highlight class
      var relClass, isInvalid = false, isReviewed = false;
      if (hi.type === "match") {
        relClass = getEffectiveRelevance(currentEpisode, hi.match);
        isInvalid = !isValid(currentEpisode, hi.themeId);
        isReviewed = !!getDecision(currentEpisode, hi.themeId);
      } else {
        relClass = hi.decision.relevance || "tangential";
        isReviewed = true;
      }

      var cls = "passage-highlight " + (isInvalid ? "invalid" : relClass);
      if (isReviewed && !isInvalid) cls += " reviewed";
      if (i === activeHighlightIdx) cls += " active";

      html += '<span class="' + cls + '" data-hl-idx="' + i + '">' +
        esc(transcript.substring(start, end)) +
        '</span>';

      lastEnd = end;
    }

    // Text after last highlight
    if (lastEnd < transcript.length) {
      html += esc(transcript.substring(lastEnd));
    }

    document.getElementById("transcript-body").innerHTML = html;

    // Attach click handlers to highlights
    document.querySelectorAll(".passage-highlight").forEach(function (el) {
      el.addEventListener("click", function (e) {
        e.stopPropagation();
        var idx = parseInt(el.dataset.hlIdx);
        openHighlight(idx);
      });
    });
  }

  // =========================================================================
  // 6. SIDE PANEL
  // =========================================================================
  function openHighlight(hlIdx) {
    var highlights = getSortedHighlights(currentEpisode);
    // Filter to only positioned highlights
    var positioned = highlights.filter(function (h) { return h.start != null; });
    if (hlIdx < 0 || hlIdx >= positioned.length) return;

    activeHighlightIdx = hlIdx;
    var hi = positioned[hlIdx];

    // Update active class on highlights
    document.querySelectorAll(".passage-highlight").forEach(function (el, i) {
      el.classList.toggle("active", i === hlIdx);
    });

    // Populate panel
    var panel = document.getElementById("side-panel");
    var themeInfo = codebook[hi.themeId] || { name: hi.themeId, sub_themes: {} };

    document.getElementById("panel-theme-id").textContent = hi.themeId;
    document.getElementById("panel-theme-name").textContent = themeInfo.name;

    var isAdded = hi.type === "added";
    var dec, effRel, effCodes, quoteText, quoteSpeaker, summaryText, origRel;

    if (isAdded) {
      dec = hi.decision;
      effRel = dec.relevance || "tangential";
      effCodes = dec.codes || [];
      quoteText = "";
      quoteSpeaker = dec.speaker || "";
      summaryText = dec.summary || "";
      origRel = null;
    } else {
      var match = hi.match;
      dec = getDecision(currentEpisode, hi.themeId);
      effRel = getEffectiveRelevance(currentEpisode, match);
      effCodes = getEffectiveCodes(currentEpisode, match);
      quoteText = match.best_quote ? match.best_quote.text : "";
      quoteSpeaker = match.best_quote ? match.best_quote.speaker : "";
      summaryText = match.summary || "";
      origRel = match.relevance;
    }

    // Valid/Invalid buttons
    var valid = !dec || dec.valid !== false;
    var btnValid = document.getElementById("btn-validate");
    var btnInvalid = document.getElementById("btn-invalidate");
    btnValid.classList.toggle("selected", valid);
    btnInvalid.classList.toggle("selected", !valid);
    btnValid.classList.toggle("readonly", readonly || isAdded);
    btnInvalid.classList.toggle("readonly", readonly || isAdded);

    // Relevance buttons
    document.querySelectorAll(".rel-btn").forEach(function (btn) {
      btn.classList.toggle("selected", btn.dataset.rel === effRel);
      btn.classList.toggle("readonly", readonly);
    });

    // Codes
    renderPanelCodes(hi.themeId, effCodes);

    // Add code button
    document.getElementById("btn-add-code").classList.toggle("readonly", readonly);

    // Quote
    var quoteEl = document.getElementById("panel-quote");
    if (quoteText) {
      quoteEl.innerHTML = esc(quoteText) +
        (quoteSpeaker ? '<span class="speaker">&mdash; ' + esc(quoteSpeaker) + '</span>' : '');
    } else if (isAdded && quoteSpeaker) {
      quoteEl.innerHTML = '<span class="speaker">' + esc(quoteSpeaker) + '</span>';
    } else {
      quoteEl.innerHTML = '<em style="color:var(--fg-dim)">No quote</em>';
    }

    // Summary
    document.getElementById("panel-summary").textContent = summaryText;

    // Override note
    var noteEl = document.getElementById("panel-override-note");
    if (dec && origRel && dec.relevance && dec.relevance !== origRel) {
      noteEl.textContent = "was: " + origRel;
    } else {
      noteEl.textContent = "";
    }

    // Show panel
    panel.classList.remove("hidden");
    document.getElementById("main-layout").classList.add("panel-open");

    // Scroll highlight into view
    var activeEl = document.querySelector('.passage-highlight[data-hl-idx="' + hlIdx + '"]');
    if (activeEl) {
      activeEl.scrollIntoView({ block: "center", behavior: "smooth" });
    }
  }

  function renderPanelCodes(themeId, codes) {
    var container = document.getElementById("panel-codes");
    var html = "";
    codes.forEach(function (codeId) {
      var theme = codebook[themeId] || { sub_themes: {} };
      var name = theme.sub_themes[codeId] || "";
      html += '<span class="code-pill">' + esc(codeId) +
        (name ? " " + esc(name) : "") +
        (readonly ? '' : ' <span class="code-remove" data-code="' + esc(codeId) + '">&times;</span>') +
        '</span>';
    });
    container.innerHTML = html;

    // Attach remove handlers
    container.querySelectorAll(".code-remove").forEach(function (el) {
      el.addEventListener("click", function (e) {
        e.stopPropagation();
        removeCode(el.dataset.code);
      });
    });
  }

  function closePanel() {
    activeHighlightIdx = -1;
    document.getElementById("side-panel").classList.add("hidden");
    document.getElementById("main-layout").classList.remove("panel-open");
    document.querySelectorAll(".passage-highlight.active").forEach(function (el) {
      el.classList.remove("active");
    });
  }

  // =========================================================================
  // 7. DECISION ACTIONS
  // =========================================================================
  function getCurrentHighlight() {
    if (activeHighlightIdx < 0) return null;
    var highlights = getSortedHighlights(currentEpisode);
    var positioned = highlights.filter(function (h) { return h.start != null; });
    return positioned[activeHighlightIdx] || null;
  }

  function applyValidation(valid) {
    if (readonly) return;
    var hi = getCurrentHighlight();
    if (!hi || hi.type === "added") return;

    var key = decisionKey(currentEpisode, hi.themeId);
    if (!decisions[key]) {
      decisions[key] = {
        valid: valid,
        relevance: hi.match.relevance,
        codes: hi.match.sub_themes_present.slice(),
        timestamp: Date.now()
      };
    } else {
      decisions[key].valid = valid;
      decisions[key].timestamp = Date.now();
    }
    updateProgress();
    renderTranscript(allEpisodes[currentEpisode]);
    openHighlight(activeHighlightIdx);
    ghScheduleSave();
  }

  function applyRelevance(value) {
    if (readonly) return;
    var hi = getCurrentHighlight();
    if (!hi) return;

    if (hi.type === "added") {
      hi.decision.relevance = value;
      hi.decision.timestamp = Date.now();
    } else {
      var key = decisionKey(currentEpisode, hi.themeId);
      if (!decisions[key]) {
        decisions[key] = {
          valid: true,
          relevance: value,
          codes: hi.match.sub_themes_present.slice(),
          timestamp: Date.now()
        };
      } else {
        decisions[key].relevance = value;
        decisions[key].timestamp = Date.now();
      }
    }
    updateProgress();
    renderTranscript(allEpisodes[currentEpisode]);
    openHighlight(activeHighlightIdx);
    ghScheduleSave();
  }

  function removeCode(codeId) {
    if (readonly) return;
    var hi = getCurrentHighlight();
    if (!hi) return;

    var key, codes;
    if (hi.type === "added") {
      key = hi.key;
      codes = hi.decision.codes || [];
    } else {
      key = decisionKey(currentEpisode, hi.themeId);
      if (!decisions[key]) {
        decisions[key] = {
          valid: true,
          relevance: hi.match.relevance,
          codes: hi.match.sub_themes_present.slice(),
          timestamp: Date.now()
        };
      }
      codes = decisions[key].codes;
    }

    var idx = codes.indexOf(codeId);
    if (idx >= 0) {
      codes.splice(idx, 1);
      decisions[key].timestamp = Date.now();
    }
    openHighlight(activeHighlightIdx);
    ghScheduleSave();
  }

  function addCode(codeId) {
    if (readonly) return;
    var hi = getCurrentHighlight();
    if (!hi) return;

    var key, codes;
    if (hi.type === "added") {
      key = hi.key;
      codes = hi.decision.codes || [];
    } else {
      key = decisionKey(currentEpisode, hi.themeId);
      if (!decisions[key]) {
        decisions[key] = {
          valid: true,
          relevance: hi.match.relevance,
          codes: hi.match.sub_themes_present.slice(),
          timestamp: Date.now()
        };
      }
      codes = decisions[key].codes;
    }

    if (codes.indexOf(codeId) < 0) {
      codes.push(codeId);
      codes.sort();
      decisions[key].timestamp = Date.now();
    }
    ghScheduleSave();
  }

  // =========================================================================
  // 8. CODE SEARCH MODAL
  // =========================================================================
  function openCodeModal(target) {
    passageCodeForModal = target; // "panel" or "passage"
    var modal = document.getElementById("code-modal");
    var searchInput = document.getElementById("code-search");
    searchInput.value = "";
    modal.classList.remove("hidden");
    renderCodeList("");
    searchInput.focus();
  }

  function closeCodeModal() {
    document.getElementById("code-modal").classList.add("hidden");
    passageCodeForModal = null;
  }

  function renderCodeList(query) {
    var container = document.getElementById("code-list");
    var currentCodes;

    if (passageCodeForModal === "passage") {
      currentCodes = passageCodeTempCodes;
    } else {
      var hi = getCurrentHighlight();
      if (!hi) { container.innerHTML = ""; return; }
      currentCodes = hi.type === "added"
        ? (hi.decision.codes || [])
        : getEffectiveCodes(currentEpisode, hi.match);
    }

    var filtered = allSubThemes;
    if (query) {
      filtered = allSubThemes.filter(function (st) {
        return fuzzyMatch(query, st.id + " " + st.name);
      });
    }

    var html = "";

    // Show assigned codes first
    if (!query) {
      var assigned = allSubThemes.filter(function (st) {
        return currentCodes.indexOf(st.id) >= 0;
      });
      if (assigned.length > 0) {
        html += '<div style="font-size:10px;font-weight:600;color:var(--fg-dim);padding:4px 8px;text-transform:uppercase">Assigned</div>';
        assigned.forEach(function (st) {
          html += buildCodeItemHTML(st, true);
        });
        html += '<div style="height:1px;background:var(--border);margin:8px 0"></div>';
      }
    }

    filtered.forEach(function (st) {
      if (!query && currentCodes.indexOf(st.id) >= 0) return; // already shown above
      var isAssigned = currentCodes.indexOf(st.id) >= 0;
      html += buildCodeItemHTML(st, isAssigned);
    });

    container.innerHTML = html;

    // Attach click handlers
    container.querySelectorAll(".code-item").forEach(function (el) {
      el.addEventListener("click", function () {
        var codeId = el.dataset.codeId;
        toggleCodeInModal(codeId);
      });
    });
  }

  function buildCodeItemHTML(st, isAssigned) {
    return '<div class="code-item' + (isAssigned ? ' assigned' : '') + '" data-code-id="' + esc(st.id) + '">' +
      '<span class="code-check">' + (isAssigned ? '&#10003;' : '') + '</span>' +
      '<span class="code-id">' + esc(st.id) + '</span>' +
      '<span class="code-name">' + esc(st.name) + '</span>' +
      '</div>';
  }

  function toggleCodeInModal(codeId) {
    if (passageCodeForModal === "passage") {
      var idx = passageCodeTempCodes.indexOf(codeId);
      if (idx >= 0) {
        passageCodeTempCodes.splice(idx, 1);
      } else {
        passageCodeTempCodes.push(codeId);
        passageCodeTempCodes.sort();
      }
      renderCodeList(document.getElementById("code-search").value);
      updatePassageCodesDisplay();
      checkPassageCompleteness();
    } else {
      // Panel mode: directly toggle on current highlight
      var hi = getCurrentHighlight();
      if (!hi) return;

      var codes;
      if (hi.type === "added") {
        codes = hi.decision.codes || [];
      } else {
        codes = getEffectiveCodes(currentEpisode, hi.match);
      }

      var idx = codes.indexOf(codeId);
      if (idx >= 0) {
        removeCode(codeId);
      } else {
        addCode(codeId);
      }
      renderCodeList(document.getElementById("code-search").value);
      renderPanelCodes(hi.themeId, hi.type === "added"
        ? (hi.decision.codes || [])
        : getEffectiveCodes(currentEpisode, hi.match));
    }
  }

  // =========================================================================
  // 9. TEXT SELECTION — ADD PASSAGE
  // =========================================================================
  function handleTextSelection() {
    var sel = window.getSelection();
    var btn = document.getElementById("add-passage-btn");

    if (!sel || sel.isCollapsed || readonly) {
      btn.classList.add("hidden");
      pendingSelection = null;
      return;
    }

    // Check if selection is within transcript body
    var range = sel.getRangeAt(0);
    var transcriptBody = document.getElementById("transcript-body");
    if (!transcriptBody.contains(range.startContainer) || !transcriptBody.contains(range.endContainer)) {
      btn.classList.add("hidden");
      return;
    }

    var text = sel.toString().trim();
    if (text.length < 10) {
      btn.classList.add("hidden");
      return;
    }

    // Calculate character offsets in transcript
    var transcript = allEpisodes[currentEpisode].transcript;
    var selectedText = text;
    var startIdx = transcript.indexOf(selectedText);
    if (startIdx < 0) {
      // Try finding via first 30 chars
      var prefix = selectedText.substring(0, 30);
      startIdx = transcript.indexOf(prefix);
    }

    if (startIdx >= 0) {
      pendingSelection = {
        start: startIdx,
        end: startIdx + selectedText.length,
        text: selectedText
      };

      // Position button near selection
      var rect = range.getBoundingClientRect();
      btn.style.top = (rect.bottom + window.scrollY + 4) + "px";
      btn.style.left = (rect.left + window.scrollX) + "px";
      btn.classList.remove("hidden");
    }
  }

  function openAddPassageModal() {
    if (!pendingSelection) return;

    var modal = document.getElementById("passage-modal");
    document.getElementById("passage-selected-text").textContent =
      pendingSelection.text.length > 200
        ? pendingSelection.text.substring(0, 200) + "..."
        : pendingSelection.text;

    // Populate theme dropdown
    var themeSelect = document.getElementById("passage-theme");
    themeSelect.innerHTML = '<option value="">Select theme...</option>';
    Object.keys(codebook).sort().forEach(function (tid) {
      var opt = document.createElement("option");
      opt.value = tid;
      opt.textContent = tid + " " + codebook[tid].name;
      themeSelect.appendChild(opt);
    });

    // Reset form
    document.getElementById("passage-relevance").value = "";
    document.getElementById("passage-speaker").value = "";
    document.getElementById("passage-summary").value = "";
    passageCodeTempCodes = [];
    updatePassageCodesDisplay();
    document.getElementById("passage-modal-status").textContent = "";
    document.getElementById("passage-save").disabled = true;

    modal.classList.remove("hidden");
    document.getElementById("add-passage-btn").classList.add("hidden");
    window.getSelection().removeAllRanges();
  }

  function updatePassageCodesDisplay() {
    var container = document.getElementById("passage-codes-list");
    var html = "";
    passageCodeTempCodes.forEach(function (codeId) {
      var name = "";
      for (var i = 0; i < allSubThemes.length; i++) {
        if (allSubThemes[i].id === codeId) { name = allSubThemes[i].name; break; }
      }
      html += '<span class="code-pill">' + esc(codeId) + ' ' + esc(name) + '</span>';
    });
    container.innerHTML = html;
  }

  function checkPassageCompleteness() {
    var theme = document.getElementById("passage-theme").value;
    var rel = document.getElementById("passage-relevance").value;
    var speaker = document.getElementById("passage-speaker").value.trim();
    var summary = document.getElementById("passage-summary").value.trim();
    var codes = passageCodeTempCodes.length > 0;

    var complete = theme && rel && speaker && summary && codes;
    document.getElementById("passage-save").disabled = !complete;

    if (!complete) {
      var missing = [];
      if (!theme) missing.push("theme");
      if (!rel) missing.push("relevance");
      if (!codes) missing.push("codes");
      if (!speaker) missing.push("speaker");
      if (!summary) missing.push("summary");
      document.getElementById("passage-modal-status").textContent =
        missing.length > 0 ? "Missing: " + missing.join(", ") : "";
    } else {
      document.getElementById("passage-modal-status").textContent = "";
    }
  }

  function saveNewPassage() {
    if (!pendingSelection) return;

    var key = newPassageKey(currentEpisode);
    decisions[key] = {
      added: true,
      theme_id: document.getElementById("passage-theme").value,
      relevance: document.getElementById("passage-relevance").value,
      codes: passageCodeTempCodes.slice(),
      speaker: document.getElementById("passage-speaker").value.trim(),
      summary: document.getElementById("passage-summary").value.trim(),
      passage_start: pendingSelection.start,
      passage_end: pendingSelection.end,
      timestamp: Date.now()
    };

    closePassageModal();
    pendingSelection = null;
    updateProgress();
    renderTranscript(allEpisodes[currentEpisode]);
    ghScheduleSave();
  }

  function closePassageModal() {
    document.getElementById("passage-modal").classList.add("hidden");
  }

  // =========================================================================
  // 10. KEYBOARD HANDLER
  // =========================================================================
  function anyModalOpen() {
    return !document.getElementById("code-modal").classList.contains("hidden") ||
           !document.getElementById("passage-modal").classList.contains("hidden") ||
           !document.getElementById("modal-overlay").classList.contains("hidden") ||
           !document.getElementById("gh-modal").classList.contains("hidden");
  }

  function handleKeydown(e) {
    // Code modal: let search input work
    if (!document.getElementById("code-modal").classList.contains("hidden")) {
      if (e.key === "Escape") { closeCodeModal(); e.preventDefault(); }
      return;
    }

    // Passage modal
    if (!document.getElementById("passage-modal").classList.contains("hidden")) {
      if (e.key === "Escape") { closePassageModal(); e.preventDefault(); }
      return;
    }

    // Import modal
    if (!document.getElementById("modal-overlay").classList.contains("hidden")) {
      if (e.key === "Escape") closeModal();
      return;
    }

    // GH modal
    if (!document.getElementById("gh-modal").classList.contains("hidden")) {
      if (e.key === "Escape") ghCloseSettings();
      return;
    }

    var key = e.key;

    // n/Down: next highlight
    if (key === "ArrowDown" || key === "n") {
      e.preventDefault();
      navigateHighlight(1);
      return;
    }
    // p/Up: previous highlight
    if (key === "ArrowUp" || key === "p") {
      e.preventDefault();
      navigateHighlight(-1);
      return;
    }

    // Left/h: prev episode
    if (key === "ArrowLeft" || key === "h") {
      e.preventDefault();
      goToPrevEpisode();
      return;
    }
    // Right/l: next episode
    if (key === "ArrowRight" || key === "l") {
      e.preventDefault();
      goToNextEpisode();
      return;
    }

    // Escape: close panel
    if (key === "Escape") {
      e.preventDefault();
      closePanel();
      return;
    }

    if (readonly) return;

    // x: toggle valid/invalid
    if (key === "x") {
      e.preventDefault();
      var hi = getCurrentHighlight();
      if (hi && hi.type !== "added") {
        var currentlyValid = isValid(currentEpisode, hi.themeId);
        applyValidation(!currentlyValid);
      }
      return;
    }

    // c: open code modal
    if (key === "c") {
      e.preventDefault();
      if (activeHighlightIdx >= 0) openCodeModal("panel");
      return;
    }

    // 1/2/3: set relevance
    var num = parseInt(key);
    if (num >= 1 && num <= 3) {
      e.preventDefault();
      applyRelevance(RELEVANCE_VALUES[num - 1]);
      return;
    }
  }

  function navigateHighlight(direction) {
    var highlights = getSortedHighlights(currentEpisode);
    var positioned = highlights.filter(function (h) { return h.start != null; });
    if (positioned.length === 0) return;

    var newIdx = activeHighlightIdx + direction;
    if (newIdx < 0) newIdx = 0;
    if (newIdx >= positioned.length) newIdx = positioned.length - 1;

    openHighlight(newIdx);
  }

  // =========================================================================
  // 11. PROGRESS
  // =========================================================================
  function updateProgress() {
    document.getElementById("progress").textContent =
      totalReviewed() + " / " + totalCodings() + " reviewed";
  }

  // =========================================================================
  // 12. DECISION I/O
  // =========================================================================
  function exportDecisions() {
    var data = {
      tool: "recode-review",
      version: 2,
      archetype: "contextual",
      exported: new Date().toISOString(),
      total_episodes: allEpisodes.length,
      total_codings: totalCodings(),
      reviewed_count: totalReviewed(),
      decisions: decisions
    };
    var blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json" });
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    a.download = "recode-decisions-" + new Date().toISOString().slice(0, 10) + ".json";
    a.click();
    URL.revokeObjectURL(url);
  }

  function openModal() {
    document.getElementById("modal-overlay").classList.remove("hidden");
    document.getElementById("import-files").value = "";
    document.getElementById("import-status").textContent = "";
  }

  function closeModal() {
    document.getElementById("modal-overlay").classList.add("hidden");
  }

  function handleImport() {
    var files = document.getElementById("import-files").files;
    if (!files.length) {
      document.getElementById("import-status").textContent = "No file selected.";
      return;
    }
    var reader = new FileReader();
    reader.onload = function (e) {
      try {
        var data = JSON.parse(e.target.result);
        if (data.decisions) {
          mergeDecisions(data.decisions);
          closeModal();
        }
      } catch (err) {
        document.getElementById("import-status").textContent = "Error parsing file.";
      }
    };
    reader.readAsText(files[0]);
  }

  function mergeDecisions(incoming) {
    var added = 0, updated = 0;
    Object.keys(incoming).forEach(function (key) {
      if (!decisions[key]) {
        decisions[key] = incoming[key];
        added++;
      } else if (incoming[key].timestamp > decisions[key].timestamp) {
        decisions[key] = incoming[key];
        updated++;
      }
    });
    document.getElementById("import-status").textContent = added + " added, " + updated + " updated";
    renderEpisode();
    updateProgress();
  }

  // =========================================================================
  // 13. GITHUB SYNC
  // =========================================================================
  var gh = { owner: "", repo: "", path: "", token: "", sha: "", connected: false };
  var saveTimer = null;
  var SAVE_DEBOUNCE = 2000;
  var POLL_INTERVAL = 30000;
  var pollTimer = null;

  var GH_DEFAULTS = {
    owner: "clombion",
    repo: "ijba-datalab-2026",
    path: "research/newsroom-robots/decisions.json"
  };

  function ghHeaders() {
    return {
      Authorization: "Bearer " + gh.token,
      Accept: "application/vnd.github+json",
      "X-GitHub-Api-Version": "2022-11-28"
    };
  }

  function ghApiUrl() {
    return "https://api.github.com/repos/" + gh.owner + "/" + gh.repo + "/contents/" + gh.path;
  }

  function ghSetStatus(text, fadeMs) {
    var el = document.getElementById("gh-status-text");
    if (!el) return;
    el.textContent = text;
    el.classList.remove("fade-out");
    if (fadeMs) {
      setTimeout(function () { el.classList.add("fade-out"); }, fadeMs);
    }
  }

  function ghUpdateIndicator() {
    var dot = document.getElementById("gh-indicator");
    var btn = document.getElementById("btn-github");
    if (!dot || !btn) return;
    if (gh.connected) {
      dot.className = "gh-dot connected";
      btn.textContent = "Connected";
    } else {
      dot.className = "gh-dot";
      btn.textContent = "Connect";
    }
  }

  function buildDecisionPayload() {
    return {
      tool: "recode-review",
      version: 2,
      archetype: "contextual",
      exported: new Date().toISOString(),
      total_episodes: allEpisodes.length,
      total_codings: totalCodings(),
      reviewed_count: totalReviewed(),
      decisions: decisions
    };
  }

  function ghInit() {
    try {
      gh.token = localStorage.getItem("gh_token") || "";
      gh.owner = localStorage.getItem("gh_owner") || GH_DEFAULTS.owner;
      gh.repo = localStorage.getItem("gh_repo") || GH_DEFAULTS.repo;
    } catch (e) {}
    gh.path = GH_DEFAULTS.path;

    if (gh.token && gh.owner && gh.repo) {
      ghConnect(true);
    } else {
      readonly = true;
      ghUpdateIndicator();
    }
  }

  function ghConnect(silent) {
    ghSetStatus("Connecting...");
    fetch(ghApiUrl(), { headers: ghHeaders() })
      .then(function (resp) {
        if (resp.status === 404) {
          gh.sha = "";
          gh.connected = true;
          readonly = false;
          ghSaveCredentials();
          ghUpdateIndicator();
          ghSetStatus("Connected (no decisions yet)", 3000);
          pollTimer = setInterval(ghPoll, POLL_INTERVAL);
          renderTranscript(allEpisodes[currentEpisode]);
          return;
        }
        if (!resp.ok) throw new Error("HTTP " + resp.status);
        return resp.json();
      })
      .then(function (data) {
        if (!data) return;
        gh.sha = data.sha;
        gh.connected = true;
        readonly = false;
        ghSaveCredentials();
        ghUpdateIndicator();

        var json = atob(data.content.replace(/\n/g, ""));
        var parsed = JSON.parse(json);
        if (parsed.decisions && Object.keys(parsed.decisions).length > 0) {
          mergeDecisions(parsed.decisions);
          ghSetStatus("Loaded " + Object.keys(parsed.decisions).length + " decisions", 3000);
        } else {
          ghSetStatus("Connected", 3000);
        }
        pollTimer = setInterval(ghPoll, POLL_INTERVAL);
        renderTranscript(allEpisodes[currentEpisode]);
      })
      .catch(function (err) {
        gh.connected = false;
        readonly = true;
        ghUpdateIndicator();
        ghSetStatus("Error: " + err.message);
        if (!silent) {
          document.getElementById("gh-modal-status").textContent = "Connection failed: " + err.message;
        }
      });
  }

  function ghDisconnect() {
    gh.connected = false;
    gh.token = "";
    gh.sha = "";
    readonly = true;
    try {
      localStorage.removeItem("gh_token");
      localStorage.removeItem("gh_owner");
      localStorage.removeItem("gh_repo");
    } catch (e) {}
    if (pollTimer) { clearInterval(pollTimer); pollTimer = null; }
    ghUpdateIndicator();
    ghSetStatus("");
    renderTranscript(allEpisodes[currentEpisode]);
  }

  function ghSaveCredentials() {
    try {
      localStorage.setItem("gh_token", gh.token);
      localStorage.setItem("gh_owner", gh.owner);
      localStorage.setItem("gh_repo", gh.repo);
    } catch (e) {}
  }

  function ghSave() {
    if (!gh.connected) return;
    ghSetStatus("Saving...");

    var payload = JSON.stringify(buildDecisionPayload(), null, 2);
    var body = {
      message: "Update recode decisions (" + totalReviewed() + " reviewed)",
      content: btoa(unescape(encodeURIComponent(payload))),
      committer: { name: "Recode Review", email: "noreply@review.tool" }
    };
    if (gh.sha) body.sha = gh.sha;

    fetch(ghApiUrl(), {
      method: "PUT",
      headers: ghHeaders(),
      body: JSON.stringify(body)
    })
      .then(function (resp) {
        if (resp.status === 409) {
          ghSetStatus("Conflict, reloading...");
          return ghLoad().then(function () { ghSave(); });
        }
        if (!resp.ok) throw new Error("HTTP " + resp.status);
        return resp.json();
      })
      .then(function (data) {
        if (data && data.content) gh.sha = data.content.sha;
        ghSetStatus("Saved", 3000);
      })
      .catch(function (err) {
        ghSetStatus("Save failed: " + err.message);
      });
  }

  function ghLoad() {
    return fetch(ghApiUrl(), { headers: ghHeaders() })
      .then(function (resp) {
        if (resp.status === 404) { gh.sha = ""; return; }
        if (!resp.ok) throw new Error("HTTP " + resp.status);
        return resp.json();
      })
      .then(function (data) {
        if (!data) return;
        gh.sha = data.sha;
        var json = atob(data.content.replace(/\n/g, ""));
        var parsed = JSON.parse(json);
        if (parsed.decisions) mergeDecisions(parsed.decisions);
      });
  }

  function ghScheduleSave() {
    if (!gh.connected) return;
    if (saveTimer) clearTimeout(saveTimer);
    saveTimer = setTimeout(ghSave, SAVE_DEBOUNCE);
  }

  function ghPoll() {
    if (!gh.connected) return;
    fetch(ghApiUrl(), { headers: ghHeaders() })
      .then(function (resp) {
        if (!resp.ok) return null;
        return resp.json();
      })
      .then(function (data) {
        if (!data) return;
        if (data.sha && data.sha !== gh.sha) {
          gh.sha = data.sha;
          var json = atob(data.content.replace(/\n/g, ""));
          var parsed = JSON.parse(json);
          if (parsed.decisions) {
            mergeDecisions(parsed.decisions);
            ghSetStatus("Updated from remote", 3000);
          }
        }
      })
      .catch(function () {});
  }

  function ghShowSettings() {
    document.getElementById("gh-input-token").value = gh.token;
    document.getElementById("gh-input-owner").value = gh.owner || GH_DEFAULTS.owner;
    document.getElementById("gh-input-repo").value = gh.repo || GH_DEFAULTS.repo;
    document.getElementById("gh-input-path").value = GH_DEFAULTS.path;
    document.getElementById("gh-modal-status").textContent = "";
    document.getElementById("gh-disconnect-btn").style.display = gh.connected ? "" : "none";
    document.getElementById("gh-modal").classList.remove("hidden");
  }

  function ghCloseSettings() {
    document.getElementById("gh-modal").classList.add("hidden");
  }

  function ghHandleConnect() {
    gh.token = document.getElementById("gh-input-token").value.trim();
    gh.owner = document.getElementById("gh-input-owner").value.trim();
    gh.repo = document.getElementById("gh-input-repo").value.trim();
    gh.path = GH_DEFAULTS.path;
    if (!gh.token) {
      document.getElementById("gh-modal-status").textContent = "Token is required.";
      return;
    }
    ghCloseSettings();
    ghConnect(false);
  }

  // =========================================================================
  // 14. THEME TOGGLE
  // =========================================================================
  function initTheme() {
    var stored = null;
    try { stored = localStorage.getItem("horizon-theme"); } catch(e) {}
    if (stored === "light" || stored === "dark") {
      document.documentElement.setAttribute("data-theme", stored);
    } else {
      var prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
      document.documentElement.setAttribute("data-theme", prefersDark ? "dark" : "light");
    }
    updateThemeButton();
  }

  function toggleTheme() {
    var current = document.documentElement.getAttribute("data-theme");
    var next = current === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    try { localStorage.setItem("horizon-theme", next); } catch(e) {}
    updateThemeButton();
  }

  function updateThemeButton() {
    var btn = document.getElementById("btn-theme");
    if (!btn) return;
    var theme = document.documentElement.getAttribute("data-theme");
    btn.textContent = theme === "dark" ? "Light" : "Dark";
  }

  // =========================================================================
  // 15. INIT
  // =========================================================================
  function init() {
    initTheme();
    loadData();

    // Initial render
    renderEpisode();
    updateProgress();
    updateEpisodeCounter();

    // Keyboard
    document.addEventListener("keydown", handleKeydown);

    // Text selection for add-passage
    document.addEventListener("mouseup", function () {
      setTimeout(handleTextSelection, 10);
    });

    // Add passage button
    document.getElementById("add-passage-btn").addEventListener("click", openAddPassageModal);

    // Toolbar bindings
    document.getElementById("btn-prev").addEventListener("click", goToPrevEpisode);
    document.getElementById("btn-next").addEventListener("click", goToNextEpisode);
    document.getElementById("hide-reviewed").addEventListener("change", function () {
      updateEpisodeCounter();
    });
    document.getElementById("btn-theme").addEventListener("click", toggleTheme);
    document.getElementById("btn-export").addEventListener("click", exportDecisions);
    document.getElementById("btn-import").addEventListener("click", openModal);
    document.getElementById("modal-cancel").addEventListener("click", closeModal);
    document.getElementById("modal-confirm").addEventListener("click", handleImport);
    document.getElementById("modal-overlay").addEventListener("click", function (e) {
      if (e.target === this) closeModal();
    });

    // Panel bindings
    document.getElementById("panel-close").addEventListener("click", closePanel);
    document.getElementById("btn-validate").addEventListener("click", function () {
      applyValidation(true);
    });
    document.getElementById("btn-invalidate").addEventListener("click", function () {
      applyValidation(false);
    });
    document.querySelectorAll(".rel-btn").forEach(function (btn) {
      btn.addEventListener("click", function () {
        applyRelevance(btn.dataset.rel);
      });
    });
    document.getElementById("btn-add-code").addEventListener("click", function () {
      if (!readonly) openCodeModal("panel");
    });

    // Code modal
    document.getElementById("code-search").addEventListener("input", function () {
      renderCodeList(this.value);
    });
    document.getElementById("code-modal-done").addEventListener("click", closeCodeModal);
    document.getElementById("code-modal").addEventListener("click", function (e) {
      if (e.target === this) closeCodeModal();
    });

    // Passage modal
    document.getElementById("passage-theme").addEventListener("change", function () {
      // When theme changes, reset codes to only sub-themes of selected theme
      passageCodeTempCodes = [];
      updatePassageCodesDisplay();
      checkPassageCompleteness();
    });
    document.getElementById("passage-relevance").addEventListener("change", checkPassageCompleteness);
    document.getElementById("passage-speaker").addEventListener("input", checkPassageCompleteness);
    document.getElementById("passage-summary").addEventListener("input", checkPassageCompleteness);
    document.getElementById("passage-add-code-btn").addEventListener("click", function () {
      openCodeModal("passage");
    });
    document.getElementById("passage-cancel").addEventListener("click", closePassageModal);
    document.getElementById("passage-save").addEventListener("click", saveNewPassage);
    document.getElementById("passage-modal").addEventListener("click", function (e) {
      if (e.target === this) closePassageModal();
    });

    // Hamburger menu
    document.getElementById("hamburger").addEventListener("click", function () {
      document.getElementById("toolbar-controls").classList.toggle("open");
    });

    // GitHub sync
    document.getElementById("btn-github").addEventListener("click", ghShowSettings);
    document.getElementById("gh-connect-btn").addEventListener("click", ghHandleConnect);
    document.getElementById("gh-disconnect-btn").addEventListener("click", function () {
      ghDisconnect();
      ghCloseSettings();
    });
    document.getElementById("gh-close-btn").addEventListener("click", ghCloseSettings);
    document.getElementById("gh-modal").addEventListener("click", function (e) {
      if (e.target === this) ghCloseSettings();
    });

    // Auto-connect
    ghInit();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
