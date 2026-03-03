// Taxonomy Review Tool
(function () {
  "use strict";

  // =========================================================================
  // 1. STATE & CONSTANTS
  // =========================================================================
  const PIPELINE_STEPS = ["Define", "Find", "Get", "Verify", "Clean", "Analyse", "Present"];
  const ACCESSIBILITY_LEVELS = ["spreadsheet", "gui_tool", "structured_prompt", "code_required"];
  const SOURCE_TYPES = ["case_study", "podcast"];
  const VERDICTS = ["approve", "reject", "merge"];
  // Decision columns: verdict, accessibility_level override
  const COLS = ["verdict", "accessibility_level"];
  const COL_OPTIONS = [VERDICTS, ACCESSIBILITY_LEVELS];

  let allRows = [];
  let filteredIndices = [];
  let decisions = {};
  let activeRow = 0;
  let activeCol = 1;
  let openDropdown = null;
  let isMobile = false;
  let readonly = true;

  const ROW_HEIGHT = 150;
  const ROW_HEIGHT_MOBILE = 280;
  const BUFFER = 10;

  // =========================================================================
  // 2. DATA LOADER
  // =========================================================================
  function loadData() {
    var el = document.getElementById("taxonomy-data");
    var b64 = el.textContent.trim();
    var binary = atob(b64);
    var bytes = new Uint8Array(binary.length);
    for (var i = 0; i < binary.length; i++) bytes[i] = binary.charCodeAt(i);
    var decompressed = fflate.gunzipSync(bytes);
    allRows = JSON.parse(new TextDecoder().decode(decompressed));
  }

  // =========================================================================
  // 3. VIRTUAL SCROLLER
  // =========================================================================
  var scrollContainer = function () { return document.getElementById("scroll-container"); };
  var scrollSpacer = function () { return document.getElementById("scroll-spacer"); };
  var visibleRowsEl = function () { return document.getElementById("visible-rows"); };

  function getRowHeight() { return isMobile ? ROW_HEIGHT_MOBILE : ROW_HEIGHT; }

  function renderVisibleRows() {
    var container = scrollContainer();
    var rh = getRowHeight();
    scrollSpacer().style.height = (filteredIndices.length * rh) + "px";
    var scrollTop = container.scrollTop;
    var viewportHeight = container.clientHeight;
    var startIdx = Math.max(0, Math.floor(scrollTop / rh) - BUFFER);
    var endIdx = Math.min(filteredIndices.length, Math.ceil((scrollTop + viewportHeight) / rh) + BUFFER);
    var el = visibleRowsEl();
    el.style.transform = "translateY(" + (startIdx * rh) + "px)";
    var fragment = document.createDocumentFragment();
    for (var i = startIdx; i < endIdx; i++) fragment.appendChild(buildRow(i));
    el.innerHTML = "";
    el.appendChild(fragment);
  }

  function buildRow(visIdx) {
    var dataIdx = filteredIndices[visIdx];
    var row = allRows[dataIdx];
    var dec = decisions[dataIdx] || {};
    var isActive = visIdx === activeRow;
    var isReviewed = !!decisions[dataIdx];

    var el = document.createElement("div");
    el.className = "row";
    el.dataset.visIdx = visIdx;
    if (isActive) el.classList.add("active");
    if (isReviewed) el.classList.add("reviewed");

    if (isMobile) {
      el.innerHTML = buildCardHTML(dataIdx, row, dec, isActive);
    } else {
      el.innerHTML =
        buildPracticeCell(dataIdx, row, dec, isActive) +
        buildDetailCell(dataIdx, row, isActive) +
        buildDecisionCell(dataIdx, 0, "Verdict", "", dec.verdict, isActive) +
        buildDecisionCell(dataIdx, 1, "Access", row.accessibility_level, dec.accessibility_level, isActive) +
        buildNotesCell(dataIdx, dec);
    }

    if (!isMobile) {
      el.addEventListener("mouseover", function (e) {
        if (openDropdown) return;
        var cell = e.target.closest(".cell");
        var col = cell ? parseInt(cell.dataset.col) : activeCol;
        if (isNaN(col)) col = activeCol;
        if (visIdx !== activeRow || col !== activeCol) {
          activeRow = visIdx;
          activeCol = col;
          renderVisibleRows();
        }
      });
    }

    el.addEventListener("click", function (e) {
      if (e.target.closest(".dropdown-menu")) return;
      if (e.target.closest(".notes-input")) return;
      var wrapper = e.target.closest(".dropdown-wrapper");
      var decCell = !isMobile ? e.target.closest(".cell-decision") : null;
      if ((wrapper || decCell) && !readonly) {
        e.stopPropagation();
        var col, dIdx;
        if (wrapper) { col = parseInt(wrapper.dataset.col); dIdx = parseInt(wrapper.dataset.dataIdx); }
        else { col = parseInt(decCell.dataset.col); dIdx = parseInt(decCell.dataset.dataIdx); }
        activeRow = visIdx;
        activeCol = col;
        closeDropdown();
        renderVisibleRows();
        openDropdownFor(dIdx, col);
        return;
      }
      setActiveRow(visIdx);
    });

    return el;
  }

  function buildPracticeCell(dataIdx, row, dec, isActive) {
    var verdict = dec.verdict || "";
    var verdictHTML = "";
    if (verdict) verdictHTML = '<span class="verdict-badge verdict-' + verdict + '">' + verdict + '</span> ';

    return '<div class="cell cell-practice' + (isActive && activeCol === 0 ? ' focused' : '') + '" data-col="0">' +
      '<div>' + verdictHTML +
        '<span class="practice-name">' + escHTML(row.practice_name || "") + '</span>' +
        ' <span class="meta">[' + escHTML(row.practice_id || "") + ']</span>' +
      '</div>' +
      '<div class="practice-desc">' + escHTML(row.description || "") + '</div>' +
      '<div class="meta">' +
        '<span>' + escHTML(row.source_type || "") + ': ' + escHTML(row.source_id || "") + '</span>' +
        '<span>Steps: ' + escHTML(row.pipeline_steps || "") + '</span>' +
        '<span>Tools: ' + escHTML(row.tools_mentioned || "") + '</span>' +
      '</div>' +
    '</div>';
  }

  function buildDetailCell(dataIdx, row, isActive) {
    return '<div class="cell cell-detail" data-col="-1">' +
      '<div class="detail-label">Replaces</div>' +
      '<div class="detail-value">' + escHTML(row.replaces_category || "") + '</div>' +
      '<div class="detail-label" style="margin-top:6px">Verification</div>' +
      '<div class="detail-value">' + escHTML(row.verification_method || "") + '</div>' +
      '<div class="detail-label" style="margin-top:6px">Example</div>' +
      '<div class="detail-value" style="max-height:' + (isActive ? 'none' : '40px') + ';overflow:hidden">' + escHTML(row.example || "") + '</div>' +
    '</div>';
  }

  function buildDecisionCell(dataIdx, col, label, originalValue, overrideValue, isActive) {
    var displayValue = overrideValue || originalValue || "";
    var isOverridden = overrideValue && overrideValue !== originalValue;
    var focused = isActive && activeCol === (col + 2) ? " focused" : "";
    var roClass = readonly ? " readonly" : "";

    return '<div class="cell cell-decision' + focused + roClass + '" data-col="' + col + '" data-data-idx="' + dataIdx + '">' +
      '<div class="cell-label">' + label + '</div>' +
      '<div class="dropdown-wrapper' + roClass + '" data-col="' + col + '" data-data-idx="' + dataIdx + '">' +
        '<span class="current-value">' + escHTML(displayValue) + '</span>' +
      '</div>' +
      (isOverridden ? '<div class="override-note">was: ' + escHTML(originalValue) + '</div>' : '') +
    '</div>';
  }

  function buildNotesCell(dataIdx, dec) {
    var notes = dec.notes || "";
    var roAttr = readonly ? ' disabled' : '';
    return '<div class="cell" data-col="-1" style="padding:10px">' +
      '<div class="cell-label">Notes</div>' +
      '<textarea class="notes-input" rows="3" data-data-idx="' + dataIdx + '"' + roAttr + '>' + escHTML(notes) + '</textarea>' +
    '</div>';
  }

  function buildCardHTML(dataIdx, row, dec, isActive) {
    var verdict = dec.verdict || "";
    var verdictHTML = verdict ? '<span class="verdict-badge verdict-' + verdict + '">' + verdict + '</span> ' : '';
    return '<div class="cell cell-practice">' +
        '<div>' + verdictHTML + '<span class="practice-name">' + escHTML(row.practice_name || "") + '</span> [' + escHTML(row.practice_id || "") + ']</div>' +
        '<div class="practice-desc">' + escHTML(row.description || "") + '</div>' +
        '<div class="meta"><span>' + escHTML(row.source_type || "") + '</span><span>Steps: ' + escHTML(row.pipeline_steps || "") + '</span></div>' +
      '</div>' +
      '<div style="display:flex;flex-wrap:wrap;gap:8px;padding-top:10px;border-top:1px solid var(--border-light)">' +
        buildDecisionCell(dataIdx, 0, "Verdict", "", dec.verdict, isActive) +
        buildDecisionCell(dataIdx, 1, "Access", row.accessibility_level, dec.accessibility_level, isActive) +
      '</div>';
  }

  function escHTML(s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }

  function scrollToActiveRow() {
    var container = scrollContainer();
    var rh = getRowHeight();
    var rowTop = activeRow * rh;
    var rowBottom = rowTop + rh;
    var viewTop = container.scrollTop;
    var viewBottom = viewTop + container.clientHeight;
    if (rowTop < viewTop) container.scrollTop = rowTop;
    else if (rowBottom > viewBottom) container.scrollTop = rowBottom - container.clientHeight;
    renderVisibleRows();
  }

  function setActiveRow(visIdx) {
    if (visIdx < 0 || visIdx >= filteredIndices.length) return;
    activeRow = visIdx;
    closeDropdown();
    scrollToActiveRow();
  }

  // =========================================================================
  // 4. KEYBOARD
  // =========================================================================
  function handleKeydown(e) {
    if (!document.getElementById("modal-overlay").classList.contains("hidden")) { if (e.key === "Escape") closeModal(); return; }
    if (!document.getElementById("gh-modal").classList.contains("hidden")) { if (e.key === "Escape") ghCloseSettings(); return; }
    if (e.key === "ArrowDown") { e.preventDefault(); setActiveRow(Math.min(activeRow + 1, filteredIndices.length - 1)); return; }
    if (e.key === "ArrowUp") { e.preventDefault(); setActiveRow(Math.max(activeRow - 1, 0)); return; }
    if (e.key === "ArrowRight" && !openDropdown) { e.preventDefault(); activeCol = Math.min(activeCol + 1, 1); renderVisibleRows(); return; }
    if (e.key === "ArrowLeft" && !openDropdown) { e.preventDefault(); activeCol = Math.max(activeCol - 1, 0); renderVisibleRows(); return; }
    if (e.key === "Enter") {
      e.preventDefault();
      if (readonly) return;
      if (openDropdown && openDropdown.col === activeCol) closeDropdown();
      else openDropdownFor(filteredIndices[activeRow], activeCol);
      return;
    }
    if (e.key === "Escape") { e.preventDefault(); if (openDropdown) closeDropdown(); return; }
    var num = parseInt(e.key);
    if (readonly) return;
    if (num >= 1 && num <= 9) {
      e.preventDefault();
      var options = COL_OPTIONS[activeCol];
      if (options && num <= options.length) { applyDecision(filteredIndices[activeRow], activeCol, options[num - 1]); closeDropdown(); }
    }
  }

  // =========================================================================
  // 5. DROPDOWN
  // =========================================================================
  function openDropdownFor(dataIdx, col) {
    closeDropdown();
    openDropdown = { dataIdx: dataIdx, col: col };
    var wrapper = visibleRowsEl().querySelector('.dropdown-wrapper[data-col="' + col + '"][data-data-idx="' + dataIdx + '"]');
    if (!wrapper) return;
    var options = COL_OPTIONS[col];
    var currentValue = getEffectiveValue(dataIdx, col);
    var menu = document.createElement("div");
    menu.className = "dropdown-menu open";
    options.forEach(function (opt, i) {
      var item = document.createElement("div");
      item.className = "dropdown-item" + (opt === currentValue ? " selected" : "");
      item.innerHTML = escHTML(opt) + '<span class="shortcut">' + (i + 1) + '</span>';
      item.addEventListener("click", function (e) { e.stopPropagation(); applyDecision(dataIdx, col, opt); closeDropdown(); });
      menu.appendChild(item);
    });
    wrapper.appendChild(menu);
  }

  function closeDropdown() {
    openDropdown = null;
    document.querySelectorAll(".dropdown-menu").forEach(function (m) { m.remove(); });
    var strip = document.getElementById("pill-strip");
    if (strip) strip.classList.add("hidden");
  }

  function getEffectiveValue(dataIdx, col) {
    var field = COLS[col];
    var dec = decisions[dataIdx];
    if (dec && dec[field] !== undefined) return dec[field];
    if (col === 1) return allRows[dataIdx].accessibility_level || "";
    return "";
  }

  function applyDecision(dataIdx, col, value) {
    if (readonly) return;
    if (!decisions[dataIdx]) decisions[dataIdx] = { timestamp: Date.now() };
    decisions[dataIdx][COLS[col]] = value;
    decisions[dataIdx].timestamp = Date.now();
    updateProgress();
    renderVisibleRows();
    ghScheduleSave();
  }

  // =========================================================================
  // 6. TOUCH
  // =========================================================================
  var touchTimer = null, touchTarget = null, pillStripActive = false;

  function handleTouchStart(e) {
    if (readonly) return;
    var wrapper = e.target.closest(".dropdown-wrapper");
    if (!wrapper) return;
    touchTarget = { col: parseInt(wrapper.dataset.col), dataIdx: parseInt(wrapper.dataset.dataIdx), x: e.touches[0].clientX, y: e.touches[0].clientY };
    touchTimer = setTimeout(function () {
      showPillStrip(touchTarget.col, touchTarget.dataIdx, touchTarget.x, touchTarget.y);
      pillStripActive = true;
    }, 150);
  }

  function handleTouchMove(e) {
    if (!pillStripActive) return;
    e.preventDefault();
    var touch = e.touches[0];
    var el = document.elementFromPoint(touch.clientX, touch.clientY);
    document.querySelectorAll(".pill").forEach(function (p) { p.classList.remove("active"); });
    if (el && el.classList.contains("pill")) el.classList.add("active");
  }

  function handleTouchEnd() {
    if (touchTimer) { clearTimeout(touchTimer); touchTimer = null; }
    if (pillStripActive) {
      var activePill = document.querySelector(".pill.active");
      if (activePill && touchTarget) applyDecision(touchTarget.dataIdx, touchTarget.col, activePill.dataset.value);
      pillStripActive = false;
      document.getElementById("pill-strip").classList.add("hidden");
    } else if (touchTarget) {
      openDropdownFor(touchTarget.dataIdx, touchTarget.col);
    }
    touchTarget = null;
  }

  function showPillStrip(col, dataIdx, x, y) {
    var strip = document.getElementById("pill-strip");
    strip.innerHTML = "";
    var options = COL_OPTIONS[col];
    options.forEach(function (opt) {
      var pill = document.createElement("div");
      pill.className = "pill";
      pill.dataset.value = opt;
      pill.textContent = opt.length > 9 ? opt.substring(0, 8) + "\u2026" : opt;
      strip.appendChild(pill);
    });
    strip.classList.remove("hidden");
    var stripWidth = Math.min(options.length * 80, window.innerWidth * 0.95);
    strip.style.left = Math.max(4, Math.min(x - stripWidth / 2, window.innerWidth - stripWidth - 4)) + "px";
    strip.style.top = Math.max(4, y - 60) + "px";
  }

  // =========================================================================
  // 7. FILTERS
  // =========================================================================
  function applyFilters() {
    var hideReviewed = document.getElementById("hide-reviewed").checked;
    var stepFilter = document.getElementById("filter-step").value;
    var accFilter = document.getElementById("filter-accessibility").value;
    var srcFilter = document.getElementById("filter-source").value;

    filteredIndices = [];
    for (var i = 0; i < allRows.length; i++) {
      var row = allRows[i];
      var dec = decisions[i];
      if (hideReviewed && dec) continue;
      if (stepFilter && !(row.pipeline_steps || "").split(",").some(function (s) { return s.trim() === stepFilter; })) continue;
      var effAcc = (dec && dec.accessibility_level) || row.accessibility_level;
      if (accFilter && effAcc !== accFilter) continue;
      if (srcFilter && row.source_type !== srcFilter) continue;
      filteredIndices.push(i);
    }

    activeRow = Math.min(activeRow, Math.max(0, filteredIndices.length - 1));
    updateProgress();
    scrollSpacer().style.height = (filteredIndices.length * getRowHeight()) + "px";
    scrollToActiveRow();
  }

  function clearAllFilters() {
    document.getElementById("hide-reviewed").checked = false;
    document.getElementById("filter-step").value = "";
    document.getElementById("filter-accessibility").value = "";
    document.getElementById("filter-source").value = "";
    activeRow = 0;
    applyFilters();
  }

  function updateProgress() {
    var reviewed = Object.keys(decisions).length;
    document.getElementById("progress").textContent = reviewed + " / " + allRows.length + " reviewed (" + filteredIndices.length + " visible)";
  }

  function populateFilterDropdowns() {
    var stepSel = document.getElementById("filter-step");
    PIPELINE_STEPS.forEach(function (s) { var o = document.createElement("option"); o.value = s; o.textContent = s; stepSel.appendChild(o); });
    var accSel = document.getElementById("filter-accessibility");
    ACCESSIBILITY_LEVELS.forEach(function (a) { var o = document.createElement("option"); o.value = a; o.textContent = a; accSel.appendChild(o); });
    var srcSel = document.getElementById("filter-source");
    SOURCE_TYPES.forEach(function (s) { var o = document.createElement("option"); o.value = s; o.textContent = s; srcSel.appendChild(o); });
  }

  // =========================================================================
  // 8. DECISION I/O
  // =========================================================================
  function exportDecisions() {
    var data = { tool: "taxonomy-review", version: 1, exported: new Date().toISOString(), total_rows: allRows.length, reviewed_count: Object.keys(decisions).length, decisions: decisions };
    var blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json" });
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a"); a.href = url; a.download = "taxonomy-decisions-" + new Date().toISOString().slice(0, 10) + ".json"; a.click();
    URL.revokeObjectURL(url);
  }

  function openModal() { document.getElementById("modal-overlay").classList.remove("hidden"); document.getElementById("import-files").value = ""; document.getElementById("import-status").textContent = ""; }
  function closeModal() { document.getElementById("modal-overlay").classList.add("hidden"); }

  function handleImport() {
    var files = document.getElementById("import-files").files;
    if (!files.length) { document.getElementById("import-status").textContent = "No files selected."; return; }
    var pending = files.length, allImported = [];
    Array.from(files).forEach(function (file) {
      var reader = new FileReader();
      reader.onload = function (e) {
        try { var data = JSON.parse(e.target.result); if (data.decisions) allImported.push({ source: file.name, decisions: data.decisions }); } catch (err) {}
        pending--;
        if (pending === 0) { mergeImports(allImported); closeModal(); }
      };
      reader.readAsText(file);
    });
  }

  function mergeImports(imports) {
    imports.forEach(function (imp) {
      Object.keys(imp.decisions).forEach(function (key) {
        var idx = parseInt(key), incoming = imp.decisions[key];
        if (!decisions[idx]) { decisions[idx] = incoming; }
        else {
          var existing = decisions[idx];
          COLS.forEach(function (field) {
            if (incoming[field] !== undefined) {
              if (!existing[field] || incoming.timestamp > existing.timestamp) existing[field] = incoming[field];
            }
          });
          if (incoming.notes) existing.notes = incoming.notes;
          existing.timestamp = Math.max(existing.timestamp || 0, incoming.timestamp || 0);
        }
      });
    });
    applyFilters();
  }

  // =========================================================================
  // 9. NOTES HANDLER
  // =========================================================================
  function handleNotesChange(e) {
    if (readonly) return;
    var textarea = e.target.closest(".notes-input");
    if (!textarea) return;
    var dataIdx = parseInt(textarea.dataset.dataIdx);
    if (isNaN(dataIdx)) return;
    if (!decisions[dataIdx]) decisions[dataIdx] = { timestamp: Date.now() };
    decisions[dataIdx].notes = textarea.value;
    decisions[dataIdx].timestamp = Date.now();
    ghScheduleSave();
  }

  // =========================================================================
  // 10. GITHUB SYNC
  // =========================================================================
  var gh = { owner: "", repo: "", path: "", token: "", sha: "", connected: false };
  var saveTimer = null, SAVE_DEBOUNCE = 2000, POLL_INTERVAL = 30000, pollTimer = null;
  var GH_DEFAULTS = { owner: "clombion", repo: "ijba-datalab-2026", path: "research/pipeline-canon-2/decisions/taxonomy.json" };

  function ghHeaders() { return { Authorization: "Bearer " + gh.token, Accept: "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28" }; }
  function ghApiUrl() { return "https://api.github.com/repos/" + gh.owner + "/" + gh.repo + "/contents/" + gh.path; }
  function ghSetStatus(text, fadeMs) { var el = document.getElementById("gh-status-text"); if (!el) return; el.textContent = text; el.classList.remove("fade-out"); if (fadeMs) setTimeout(function () { el.classList.add("fade-out"); }, fadeMs); }
  function ghUpdateIndicator() { var dot = document.getElementById("gh-indicator"), btn = document.getElementById("btn-github"); if (!dot || !btn) return; if (gh.connected) { dot.className = "gh-dot connected"; btn.textContent = "Connected"; } else { dot.className = "gh-dot"; btn.textContent = "Connect"; } }
  function buildDecisionPayload() { return { tool: "taxonomy-review", version: 1, exported: new Date().toISOString(), total_rows: allRows.length, reviewed_count: Object.keys(decisions).length, decisions: decisions }; }

  function ghInit() {
    try { gh.token = localStorage.getItem("gh_token") || ""; gh.owner = localStorage.getItem("gh_owner") || GH_DEFAULTS.owner; gh.repo = localStorage.getItem("gh_repo") || GH_DEFAULTS.repo; } catch (e) {}
    gh.path = GH_DEFAULTS.path;
    if (gh.token && gh.owner && gh.repo) ghConnect(true);
    else { readonly = true; ghUpdateIndicator(); }
  }

  function ghConnect(silent) {
    ghSetStatus("Connecting...");
    fetch(ghApiUrl(), { headers: ghHeaders() }).then(function (resp) {
      if (resp.status === 404) { gh.sha = ""; gh.connected = true; readonly = false; ghSaveCredentials(); ghUpdateIndicator(); ghSetStatus("Connected (no decisions yet)", 3000); pollTimer = setInterval(ghPoll, POLL_INTERVAL); renderVisibleRows(); return; }
      if (!resp.ok) throw new Error("HTTP " + resp.status);
      return resp.json();
    }).then(function (data) {
      if (!data) return;
      gh.sha = data.sha; gh.connected = true; readonly = false; ghSaveCredentials(); ghUpdateIndicator();
      var json = atob(data.content.replace(/\n/g, "")); var parsed = JSON.parse(json);
      if (parsed.decisions && Object.keys(parsed.decisions).length > 0) { mergeImports([{ source: "github", decisions: parsed.decisions }]); ghSetStatus("Loaded " + Object.keys(parsed.decisions).length + " decisions", 3000); }
      else ghSetStatus("Connected", 3000);
      pollTimer = setInterval(ghPoll, POLL_INTERVAL); renderVisibleRows();
    }).catch(function (err) { gh.connected = false; readonly = true; ghUpdateIndicator(); ghSetStatus("Error: " + err.message); if (!silent) document.getElementById("gh-modal-status").textContent = "Failed: " + err.message; });
  }

  function ghDisconnect() { gh.connected = false; gh.token = ""; gh.sha = ""; readonly = true; try { localStorage.removeItem("gh_token"); localStorage.removeItem("gh_owner"); localStorage.removeItem("gh_repo"); } catch (e) {} if (pollTimer) { clearInterval(pollTimer); pollTimer = null; } ghUpdateIndicator(); ghSetStatus(""); renderVisibleRows(); }
  function ghSaveCredentials() { try { localStorage.setItem("gh_token", gh.token); localStorage.setItem("gh_owner", gh.owner); localStorage.setItem("gh_repo", gh.repo); } catch (e) {} }

  function ghSave() {
    if (!gh.connected) return;
    ghSetStatus("Saving...");
    var payload = JSON.stringify(buildDecisionPayload(), null, 2);
    var body = { message: "Update taxonomy decisions (" + Object.keys(decisions).length + " reviewed)", content: btoa(unescape(encodeURIComponent(payload))), committer: { name: "Taxonomy Review", email: "noreply@review.tool" } };
    if (gh.sha) body.sha = gh.sha;
    fetch(ghApiUrl(), { method: "PUT", headers: ghHeaders(), body: JSON.stringify(body) }).then(function (resp) {
      if (resp.status === 409) { ghSetStatus("Conflict, reloading..."); return ghLoad().then(function () { ghSave(); }); }
      if (!resp.ok) throw new Error("HTTP " + resp.status);
      return resp.json();
    }).then(function (data) { if (data && data.content) gh.sha = data.content.sha; ghSetStatus("Saved", 3000); }).catch(function (err) { ghSetStatus("Save failed: " + err.message); });
  }

  function ghLoad() {
    return fetch(ghApiUrl(), { headers: ghHeaders() }).then(function (resp) { if (resp.status === 404) { gh.sha = ""; return; } if (!resp.ok) throw new Error("HTTP " + resp.status); return resp.json(); }).then(function (data) {
      if (!data) return; gh.sha = data.sha; var json = atob(data.content.replace(/\n/g, "")); var parsed = JSON.parse(json); if (parsed.decisions) mergeImports([{ source: "github", decisions: parsed.decisions }]);
    });
  }

  function ghScheduleSave() { if (!gh.connected) return; if (saveTimer) clearTimeout(saveTimer); saveTimer = setTimeout(ghSave, SAVE_DEBOUNCE); }
  function ghPoll() { if (!gh.connected) return; fetch(ghApiUrl(), { headers: ghHeaders() }).then(function (resp) { if (!resp.ok) return null; return resp.json(); }).then(function (data) { if (!data) return; if (data.sha && data.sha !== gh.sha) { gh.sha = data.sha; var json = atob(data.content.replace(/\n/g, "")); var parsed = JSON.parse(json); if (parsed.decisions) { mergeImports([{ source: "github-poll", decisions: parsed.decisions }]); ghSetStatus("Updated from remote", 3000); } } }).catch(function () {}); }

  function ghShowSettings() {
    document.getElementById("gh-input-token").value = gh.token;
    document.getElementById("gh-input-owner").value = gh.owner || GH_DEFAULTS.owner;
    document.getElementById("gh-input-repo").value = gh.repo || GH_DEFAULTS.repo;
    document.getElementById("gh-input-path").value = gh.path || GH_DEFAULTS.path;
    document.getElementById("gh-modal-status").textContent = "";
    document.getElementById("gh-disconnect-btn").style.display = gh.connected ? "" : "none";
    document.getElementById("gh-modal").classList.remove("hidden");
  }
  function ghCloseSettings() { document.getElementById("gh-modal").classList.add("hidden"); }
  function ghHandleConnect() {
    gh.token = document.getElementById("gh-input-token").value.trim();
    gh.owner = document.getElementById("gh-input-owner").value.trim();
    gh.repo = document.getElementById("gh-input-repo").value.trim();
    gh.path = document.getElementById("gh-input-path").value.trim();
    if (!gh.token) { document.getElementById("gh-modal-status").textContent = "Token is required."; return; }
    ghCloseSettings(); ghConnect(false);
  }

  // =========================================================================
  // 11. INIT
  // =========================================================================
  function initTheme() {
    var stored = null; try { stored = localStorage.getItem("horizon-theme"); } catch(e) {}
    if (stored === "light" || stored === "dark") document.documentElement.setAttribute("data-theme", stored);
    else document.documentElement.setAttribute("data-theme", window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    updateThemeButton();
  }
  function toggleTheme() { var next = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark"; document.documentElement.setAttribute("data-theme", next); try { localStorage.setItem("horizon-theme", next); } catch(e) {} updateThemeButton(); }
  function updateThemeButton() { var btn = document.getElementById("btn-theme"); if (btn) btn.textContent = document.documentElement.getAttribute("data-theme") === "dark" ? "Light" : "Dark"; }

  function init() {
    initTheme();
    isMobile = window.innerWidth <= 768;
    window.addEventListener("resize", function () { var was = isMobile; isMobile = window.innerWidth <= 768; if (was !== isMobile) renderVisibleRows(); });
    loadData();
    populateFilterDropdowns();
    filteredIndices = []; for (var i = 0; i < allRows.length; i++) filteredIndices.push(i);
    applyFilters();
    scrollContainer().addEventListener("scroll", renderVisibleRows);
    document.addEventListener("keydown", handleKeydown);
    document.addEventListener("touchstart", handleTouchStart, { passive: true });
    document.addEventListener("touchmove", handleTouchMove, { passive: false });
    document.addEventListener("touchend", handleTouchEnd, { passive: true });
    document.addEventListener("click", function (e) { if (!openDropdown) return; if (!document.contains(e.target)) return; if (e.target.closest(".dropdown-menu") || e.target.closest(".dropdown-wrapper") || e.target.closest(".cell-decision")) return; closeDropdown(); });
    document.addEventListener("input", handleNotesChange);

    document.getElementById("hide-reviewed").addEventListener("change", applyFilters);
    document.getElementById("filter-step").addEventListener("change", applyFilters);
    document.getElementById("filter-accessibility").addEventListener("change", applyFilters);
    document.getElementById("filter-source").addEventListener("change", applyFilters);
    document.getElementById("btn-clear").addEventListener("click", clearAllFilters);
    document.getElementById("btn-theme").addEventListener("click", toggleTheme);
    document.getElementById("btn-export").addEventListener("click", exportDecisions);
    document.getElementById("btn-import").addEventListener("click", openModal);
    document.getElementById("modal-cancel").addEventListener("click", closeModal);
    document.getElementById("modal-confirm").addEventListener("click", handleImport);
    document.getElementById("modal-overlay").addEventListener("click", function (e) { if (e.target === this) closeModal(); });
    document.getElementById("hamburger").addEventListener("click", function () { document.getElementById("toolbar-controls").classList.toggle("open"); });
    document.getElementById("btn-github").addEventListener("click", ghShowSettings);
    document.getElementById("gh-connect-btn").addEventListener("click", ghHandleConnect);
    document.getElementById("gh-disconnect-btn").addEventListener("click", function () { ghDisconnect(); ghCloseSettings(); });
    document.getElementById("gh-close-btn").addEventListener("click", ghCloseSettings);
    document.getElementById("gh-modal").addEventListener("click", function (e) { if (e.target === this) ghCloseSettings(); });

    renderVisibleRows();
    updateProgress();
    ghInit();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
