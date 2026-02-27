// Recode Review Tool — Single IIFE
(function () {
  "use strict";

  // =========================================================================
  // 1. STATE & CONSTANTS
  // =========================================================================
  const RELEVANCE_VALUES = ["primary", "secondary", "tangential"];

  let allEpisodes = [];
  let codebook = {};
  let currentEpisode = 0;       // 0-based index into allEpisodes
  let decisions = {};            // { "ep_0_T01": { relevance: "primary", timestamp: ... } }
  let activeThemeRow = 0;        // 0-based within current episode
  let openDropdown = null;       // { epIdx, themeId } or null
  let readonly = true;

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
  }

  // =========================================================================
  // 3. HELPERS
  // =========================================================================
  function escHTML(s) {
    return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  function decisionKey(epIdx, themeId) {
    return "ep_" + epIdx + "_" + themeId;
  }

  function totalCodings() {
    var n = 0;
    for (var i = 0; i < allEpisodes.length; i++) {
      n += allEpisodes[i].theme_codings.length;
    }
    return n;
  }

  function totalReviewed() {
    return Object.keys(decisions).length;
  }

  function episodeReviewed(epIdx) {
    var ep = allEpisodes[epIdx];
    for (var i = 0; i < ep.theme_codings.length; i++) {
      var key = decisionKey(epIdx, ep.theme_codings[i].theme_id);
      if (!decisions[key]) return false;
    }
    return true;
  }

  function getEffectiveRelevance(epIdx, themeId) {
    var key = decisionKey(epIdx, themeId);
    var dec = decisions[key];
    if (dec && dec.relevance) return dec.relevance;
    // Find original from episode
    var ep = allEpisodes[epIdx];
    for (var i = 0; i < ep.theme_codings.length; i++) {
      if (ep.theme_codings[i].theme_id === themeId) {
        return ep.theme_codings[i].relevance;
      }
    }
    return "tangential";
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
    activeThemeRow = 0;
    closeDropdown();
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
    } else if (curPos === -1 && visible.length > 0) {
      // Current episode is hidden, go to nearest visible before it
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
    } else if (curPos === -1 && visible.length > 0) {
      for (var i = 0; i < visible.length; i++) {
        if (visible[i] > currentEpisode) { goToEpisode(visible[i]); return; }
      }
      goToEpisode(visible[visible.length - 1]);
    }
  }

  function updateEpisodeCounter() {
    var visible = getVisibleEpisodes();
    var pos = visible.indexOf(currentEpisode);
    var label = (pos >= 0 ? pos + 1 : "?") + " / " + visible.length;
    document.getElementById("episode-counter").textContent = label;
  }

  // =========================================================================
  // 5. RENDER
  // =========================================================================
  function renderEpisode() {
    var ep = allEpisodes[currentEpisode];
    renderEpisodeHeader(ep);
    renderThemeRows(ep);
  }

  function renderEpisodeHeader(ep) {
    var guestHTML = "";
    for (var i = 0; i < ep.guests.length; i++) {
      var g = ep.guests[i];
      var label = escHTML(g.name);
      if (g.role) label += ", " + escHTML(g.role);
      if (g.organization) label += " — " + escHTML(g.organization);
      guestHTML += '<span class="guest-badge">' + label + '</span>';
    }

    // Relevance summary chips
    var chipHTML = "";
    for (var j = 0; j < ep.primary_themes.length; j++) {
      chipHTML += '<span class="ep-relevance-chip primary">' + escHTML(ep.primary_themes[j]) + '</span>';
    }
    for (var k = 0; k < ep.secondary_themes.length; k++) {
      chipHTML += '<span class="ep-relevance-chip secondary">' + escHTML(ep.secondary_themes[k]) + '</span>';
    }
    for (var l = 0; l < ep.tangential_themes.length; l++) {
      chipHTML += '<span class="ep-relevance-chip tangential">' + escHTML(ep.tangential_themes[l]) + '</span>';
    }

    document.getElementById("episode-header").innerHTML =
      '<div class="ep-title">' + escHTML(ep.title) + '</div>' +
      '<div class="ep-meta">' +
        '<span class="ep-date">' + escHTML(ep.date) + '</span>' +
        '<span>Host: ' + escHTML(ep.host) + '</span>' +
        guestHTML +
      '</div>' +
      '<div class="ep-relevance-summary">' + chipHTML + '</div>';
  }

  function renderThemeRows(ep) {
    var relFilter = document.getElementById("filter-relevance").value;
    var container = document.getElementById("theme-rows");
    var fragment = document.createDocumentFragment();
    var visibleIdx = 0;

    for (var i = 0; i < ep.theme_codings.length; i++) {
      var tc = ep.theme_codings[i];
      var effRel = getEffectiveRelevance(currentEpisode, tc.theme_id);

      if (relFilter && effRel !== relFilter) continue;

      var key = decisionKey(currentEpisode, tc.theme_id);
      var dec = decisions[key];
      var isReviewed = !!dec;
      var isActive = visibleIdx === activeThemeRow;

      var row = document.createElement("div");
      row.className = "theme-row";
      row.dataset.themeIdx = i;
      row.dataset.visIdx = visibleIdx;
      if (isActive) row.classList.add("active");
      if (isReviewed) row.classList.add("reviewed");

      row.innerHTML = buildThemeRowHTML(currentEpisode, tc, dec, isActive);

      // Click handler
      (function (vi) {
        row.addEventListener("click", function (e) {
          if (e.target.closest(".dropdown-menu")) return;
          if (e.target.closest(".relevance-dropdown") && !readonly) {
            e.stopPropagation();
            activeThemeRow = vi;
            closeDropdown();
            renderThemeRows(ep);
            openDropdownFor(currentEpisode, tc.theme_id);
            return;
          }
          if (vi !== activeThemeRow) {
            activeThemeRow = vi;
            closeDropdown();
            renderThemeRows(ep);
          }
        });
      })(visibleIdx);

      fragment.appendChild(row);
      visibleIdx++;
    }

    container.innerHTML = "";
    container.appendChild(fragment);
  }

  function buildThemeRowHTML(epIdx, tc, dec, isActive) {
    var themeId = tc.theme_id;
    var effRel = getEffectiveRelevance(epIdx, themeId);
    var originalRel = tc.relevance;
    var isOverridden = dec && dec.relevance && dec.relevance !== originalRel;
    var roClass = readonly ? " readonly" : "";

    // Header: badge + theme ID + name + dropdown
    var badgeClass = "relevance-" + effRel;
    var html = '<div class="theme-row-header">' +
      '<span class="relevance-badge ' + badgeClass + '">' + escHTML(effRel) + '</span>' +
      '<span class="theme-id">' + escHTML(themeId) + '</span>' +
      '<span class="theme-name">' + escHTML(tc.theme_name) + '</span>' +
      '<div class="relevance-dropdown' + roClass + '" data-ep-idx="' + epIdx + '" data-theme-id="' + escHTML(themeId) + '">' +
        '<span>' + escHTML(effRel) + '</span>' +
      '</div>' +
    '</div>';

    if (isOverridden) {
      html += '<div class="override-note">was: ' + escHTML(originalRel) + '</div>';
    }

    // Sub-theme pills
    if (tc.sub_themes_present && tc.sub_themes_present.length > 0) {
      html += '<div class="sub-theme-pills">';
      for (var i = 0; i < tc.sub_themes_present.length; i++) {
        var stId = tc.sub_themes_present[i];
        var cbTheme = codebook[themeId];
        var stName = (cbTheme && cbTheme.sub_themes && cbTheme.sub_themes[stId]) || "";
        html += '<span class="sub-theme-pill">' + escHTML(stId) + (stName ? " " + escHTML(stName) : "") + '</span>';
      }
      html += '</div>';
    }

    // Quote
    if (tc.best_quote && tc.best_quote.text) {
      html += '<blockquote class="theme-quote">' +
        escHTML(tc.best_quote.text) +
        (tc.best_quote.speaker ? '<span class="speaker">— ' + escHTML(tc.best_quote.speaker) + '</span>' : '') +
      '</blockquote>';
    }

    // Summary
    if (tc.summary) {
      html += '<div class="theme-summary">' + escHTML(tc.summary) + '</div>';
    }

    return html;
  }

  // =========================================================================
  // 6. DROPDOWN MANAGER
  // =========================================================================
  function openDropdownFor(epIdx, themeId) {
    closeDropdown();
    openDropdown = { epIdx: epIdx, themeId: themeId };

    var wrapper = document.querySelector(
      '.relevance-dropdown[data-ep-idx="' + epIdx + '"][data-theme-id="' + themeId + '"]'
    );
    if (!wrapper) return;

    var currentValue = getEffectiveRelevance(epIdx, themeId);

    var menu = document.createElement("div");
    menu.className = "dropdown-menu open";

    RELEVANCE_VALUES.forEach(function (opt, i) {
      var item = document.createElement("div");
      item.className = "dropdown-item" + (opt === currentValue ? " selected" : "");
      item.innerHTML = escHTML(opt) + '<span class="shortcut">' + (i + 1) + '</span>';
      item.addEventListener("click", function (e) {
        e.stopPropagation();
        applyDecision(epIdx, themeId, opt);
        closeDropdown();
      });
      menu.appendChild(item);
    });

    wrapper.appendChild(menu);
  }

  function closeDropdown() {
    openDropdown = null;
    document.querySelectorAll(".dropdown-menu").forEach(function (m) { m.remove(); });
  }

  function applyDecision(epIdx, themeId, value) {
    if (readonly) return;
    var key = decisionKey(epIdx, themeId);
    decisions[key] = {
      relevance: value,
      timestamp: Date.now()
    };
    updateProgress();
    renderThemeRows(allEpisodes[currentEpisode]);
    updateEpisodeCounter();
    ghScheduleSave();
  }

  // =========================================================================
  // 7. KEYBOARD HANDLER
  // =========================================================================
  function handleKeydown(e) {
    // Modals
    if (!document.getElementById("modal-overlay").classList.contains("hidden")) {
      if (e.key === "Escape") closeModal();
      return;
    }
    if (!document.getElementById("gh-modal").classList.contains("hidden")) {
      if (e.key === "Escape") ghCloseSettings();
      return;
    }

    var key = e.key;
    var ep = allEpisodes[currentEpisode];
    var visibleCount = getVisibleThemeCount();

    // Up/Down or j/k: navigate theme rows
    if (key === "ArrowDown" || key === "j") {
      e.preventDefault();
      if (activeThemeRow < visibleCount - 1) {
        activeThemeRow++;
        closeDropdown();
        renderThemeRows(ep);
        scrollToActiveThemeRow();
      }
      return;
    }
    if (key === "ArrowUp" || key === "k") {
      e.preventDefault();
      if (activeThemeRow > 0) {
        activeThemeRow--;
        closeDropdown();
        renderThemeRows(ep);
        scrollToActiveThemeRow();
      }
      return;
    }

    // Left/Right or h/l: prev/next episode
    if (key === "ArrowLeft" || key === "h") {
      if (openDropdown) return;
      e.preventDefault();
      goToPrevEpisode();
      return;
    }
    if (key === "ArrowRight" || key === "l") {
      if (openDropdown) return;
      e.preventDefault();
      goToNextEpisode();
      return;
    }

    // Enter: open/close dropdown
    if (key === "Enter") {
      e.preventDefault();
      if (readonly) return;
      var activeTc = getActiveThemeCoding();
      if (!activeTc) return;
      if (openDropdown && openDropdown.themeId === activeTc.theme_id) {
        closeDropdown();
      } else {
        openDropdownFor(currentEpisode, activeTc.theme_id);
      }
      return;
    }

    // Escape: close dropdown
    if (key === "Escape") {
      e.preventDefault();
      closeDropdown();
      return;
    }

    // Number shortcuts 1/2/3
    if (readonly) return;
    var num = parseInt(key);
    if (num >= 1 && num <= 3) {
      e.preventDefault();
      var tc = getActiveThemeCoding();
      if (tc) {
        applyDecision(currentEpisode, tc.theme_id, RELEVANCE_VALUES[num - 1]);
        closeDropdown();
      }
      return;
    }
  }

  function getVisibleThemeCount() {
    return document.querySelectorAll("#theme-rows .theme-row").length;
  }

  function getActiveThemeCoding() {
    var rows = document.querySelectorAll("#theme-rows .theme-row");
    if (activeThemeRow >= rows.length) return null;
    var row = rows[activeThemeRow];
    var themeIdx = parseInt(row.dataset.themeIdx);
    return allEpisodes[currentEpisode].theme_codings[themeIdx];
  }

  function scrollToActiveThemeRow() {
    var rows = document.querySelectorAll("#theme-rows .theme-row");
    if (activeThemeRow < rows.length) {
      rows[activeThemeRow].scrollIntoView({ block: "nearest", behavior: "smooth" });
    }
  }

  // =========================================================================
  // 8. PROGRESS & FILTERS
  // =========================================================================
  function updateProgress() {
    var reviewed = totalReviewed();
    var total = totalCodings();
    document.getElementById("progress").textContent =
      reviewed + " / " + total + " reviewed";
  }

  function applyFilters() {
    activeThemeRow = 0;
    closeDropdown();
    renderThemeRows(allEpisodes[currentEpisode]);
    updateEpisodeCounter();
  }

  // =========================================================================
  // 9. DECISION I/O
  // =========================================================================
  function exportDecisions() {
    var data = {
      tool: "recode-review",
      version: 1,
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
    var added = 0;
    var updated = 0;
    Object.keys(incoming).forEach(function (key) {
      if (!decisions[key]) {
        decisions[key] = incoming[key];
        added++;
      } else if (incoming[key].timestamp > decisions[key].timestamp) {
        decisions[key] = incoming[key];
        updated++;
      }
    });

    var status = added + " added, " + updated + " updated";
    document.getElementById("import-status").textContent = status;
    renderEpisode();
    updateProgress();
  }

  // =========================================================================
  // 10. GITHUB SYNC
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
      version: 1,
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

    if (gh.token && gh.owner && gh.repo && gh.path) {
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
          renderThemeRows(allEpisodes[currentEpisode]);
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
        renderThemeRows(allEpisodes[currentEpisode]);
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
    renderThemeRows(allEpisodes[currentEpisode]);
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
        if (data && data.content) {
          gh.sha = data.content.sha;
        }
        ghSetStatus("Saved", 3000);
      })
      .catch(function (err) {
        ghSetStatus("Save failed: " + err.message);
      });
  }

  function ghLoad() {
    return fetch(ghApiUrl(), { headers: ghHeaders() })
      .then(function (resp) {
        if (resp.status === 404) {
          gh.sha = "";
          return;
        }
        if (!resp.ok) throw new Error("HTTP " + resp.status);
        return resp.json();
      })
      .then(function (data) {
        if (!data) return;
        gh.sha = data.sha;
        var json = atob(data.content.replace(/\n/g, ""));
        var parsed = JSON.parse(json);
        if (parsed.decisions) {
          mergeDecisions(parsed.decisions);
        }
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
    var modal = document.getElementById("gh-modal");
    document.getElementById("gh-input-token").value = gh.token;
    document.getElementById("gh-input-owner").value = gh.owner || GH_DEFAULTS.owner;
    document.getElementById("gh-input-repo").value = gh.repo || GH_DEFAULTS.repo;
    document.getElementById("gh-input-path").value = GH_DEFAULTS.path;
    document.getElementById("gh-modal-status").textContent = "";

    var disconnBtn = document.getElementById("gh-disconnect-btn");
    disconnBtn.style.display = gh.connected ? "" : "none";

    modal.classList.remove("hidden");
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
  // 11. THEME TOGGLE
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
  // 12. INIT
  // =========================================================================
  function init() {
    initTheme();
    loadData();

    // Populate relevance filter
    var relSel = document.getElementById("filter-relevance");
    RELEVANCE_VALUES.forEach(function (r) {
      var o = document.createElement("option");
      o.value = r; o.textContent = r;
      relSel.appendChild(o);
    });

    // Initial render
    renderEpisode();
    updateProgress();
    updateEpisodeCounter();

    // Keyboard
    document.addEventListener("keydown", handleKeydown);

    // Close dropdown on outside click
    document.addEventListener("click", function (e) {
      if (!openDropdown) return;
      if (!document.contains(e.target)) return;
      if (e.target.closest(".dropdown-menu") || e.target.closest(".relevance-dropdown")) return;
      closeDropdown();
    });

    // Toolbar bindings
    document.getElementById("btn-prev").addEventListener("click", goToPrevEpisode);
    document.getElementById("btn-next").addEventListener("click", goToNextEpisode);
    document.getElementById("hide-reviewed").addEventListener("change", applyFilters);
    document.getElementById("filter-relevance").addEventListener("change", applyFilters);
    document.getElementById("btn-theme").addEventListener("click", toggleTheme);
    document.getElementById("btn-export").addEventListener("click", exportDecisions);
    document.getElementById("btn-import").addEventListener("click", openModal);
    document.getElementById("modal-cancel").addEventListener("click", closeModal);
    document.getElementById("modal-confirm").addEventListener("click", handleImport);
    document.getElementById("modal-overlay").addEventListener("click", function (e) {
      if (e.target === this) closeModal();
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
