// Horizon Table Review Tool — Single IIFE
(function () {
  "use strict";

  // =========================================================================
  // 1. STATE & CONSTANTS
  // =========================================================================
  const PIPELINE_STEPS = ["Define", "Find", "Get", "Verify", "Clean", "Analyse", "Present"];
  const EXTRACT_TYPES = ["procedural", "epistemological", "organizational", "tool-specific"];
  const RELEVANCE_VALUES = ["endures", "needs_update", "displaced"];
  const VERDICTS = ["pass", "reject"];
  const COLS = ["verdict", "pipeline_step", "extract_type", "llm_relevance"];
  const COL_OPTIONS = [VERDICTS, PIPELINE_STEPS, EXTRACT_TYPES, RELEVANCE_VALUES];

  let allRows = [];
  let filteredIndices = [];
  let decisions = {};       // { rowIndex: { field: value, timestamp } }
  let conflicts = {};       // { rowIndex: { field: [{ value, timestamp, source }] } }
  let resolvedConflicts = new Set();

  let activeRow = 0;        // index into filteredIndices
  let activeCol = 1;        // 0=chunk, 1=step, 2=type, 3=relevance
  let openDropdown = null;  // { dataIdx, col } or null
  let isMobile = false;
  let readonly = true;       // true until GitHub PAT is configured

  const ROW_HEIGHT = 120;
  const ROW_HEIGHT_MOBILE = 200;
  const BUFFER = 10;

  // =========================================================================
  // 2. DATA LOADER
  // =========================================================================
  function loadData() {
    const el = document.getElementById("horizon-data");
    const b64 = el.textContent.trim();

    // base64 → Uint8Array
    const binary = atob(b64);
    const bytes = new Uint8Array(binary.length);
    for (let i = 0; i < binary.length; i++) {
      bytes[i] = binary.charCodeAt(i);
    }

    // gunzip via fflate
    const decompressed = fflate.gunzipSync(bytes);

    // Uint8Array → string → JSON
    const text = new TextDecoder().decode(decompressed);
    allRows = JSON.parse(text);
  }

  // =========================================================================
  // 3. VIRTUAL SCROLLER
  // =========================================================================
  const scrollContainer = () => document.getElementById("scroll-container");
  const scrollSpacer = () => document.getElementById("scroll-spacer");
  const visibleRowsEl = () => document.getElementById("visible-rows");

  function getRowHeight() {
    return isMobile ? ROW_HEIGHT_MOBILE : ROW_HEIGHT;
  }

  function renderVisibleRows() {
    const container = scrollContainer();
    const rh = getRowHeight();
    const totalHeight = filteredIndices.length * rh;
    scrollSpacer().style.height = totalHeight + "px";

    const scrollTop = container.scrollTop;
    const viewportHeight = container.clientHeight;
    const startIdx = Math.max(0, Math.floor(scrollTop / rh) - BUFFER);
    const endIdx = Math.min(filteredIndices.length, Math.ceil((scrollTop + viewportHeight) / rh) + BUFFER);

    const el = visibleRowsEl();
    el.style.transform = "translateY(" + (startIdx * rh) + "px)";

    const fragment = document.createDocumentFragment();
    for (let i = startIdx; i < endIdx; i++) {
      fragment.appendChild(buildRow(i));
    }
    el.innerHTML = "";
    el.appendChild(fragment);
  }

  function buildRow(visIdx) {
    const dataIdx = filteredIndices[visIdx];
    const row = allRows[dataIdx];
    const dec = decisions[dataIdx] || {};
    const isActive = visIdx === activeRow;
    const isReviewed = !!decisions[dataIdx];
    const isConflict = !!conflicts[dataIdx] && !resolvedConflicts.has(dataIdx);
    const isResolved = resolvedConflicts.has(dataIdx);

    const el = document.createElement("div");
    el.className = "row";
    el.dataset.visIdx = visIdx;
    if (isActive) el.classList.add("active");
    if (isReviewed) el.classList.add("reviewed");
    if (isConflict) el.classList.add("conflict");
    if (isResolved) el.classList.add("conflict-resolved");

    if (isMobile) {
      el.innerHTML = buildCardHTML(dataIdx, row, dec, isActive);
    } else {
      el.innerHTML =
        buildChunkCell(dataIdx, row, dec, isActive) +
        buildDecisionCell(dataIdx, 1, "Step", row.pipeline_step, dec.pipeline_step, row.secondary_step ? "2nd: " + row.secondary_step : "", isActive) +
        buildDecisionCell(dataIdx, 2, "Type", row.extract_type, dec.extract_type, "", isActive) +
        buildDecisionCell(dataIdx, 3, "Relevance", row.llm_relevance, dec.llm_relevance, row.relevance_rationale || "", isActive);
    }

    // Desktop: row + cell highlight follows mouse hover
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

    // Row click — handle dropdown clicks separately to avoid DOM destruction race
    el.addEventListener("click", function (e) {
      if (e.target.closest(".dropdown-menu")) return;

      // Clicking anywhere in a decision cell opens its dropdown (desktop only).
      // The whole cell is the click target — not just the small wrapper text.
      var wrapper = e.target.closest(".dropdown-wrapper");
      var decCell = !isMobile ? e.target.closest(".cell-decision") : null;

      if ((wrapper || decCell) && !readonly) {
        e.stopPropagation();
        var col, dIdx;
        if (wrapper) {
          col = parseInt(wrapper.dataset.col);
          dIdx = parseInt(wrapper.dataset.dataIdx);
        } else {
          col = parseInt(decCell.dataset.col);
          dIdx = parseInt(decCell.dataset.dataIdx);
        }
        activeRow = visIdx;
        activeCol = col;
        // Close existing, re-render with correct active state, then open
        closeDropdown();
        renderVisibleRows();
        openDropdownFor(dIdx, col);
        return;
      }

      setActiveRow(visIdx);
    });

    return el;
  }

  function buildChunkCell(dataIdx, row, dec, isActive) {
    const verdict = dec.verdict || "";
    const textLen = (row.extract || "").length;
    const clipped = textLen > 200 ? " clipped" : "";

    var verdictInner;
    if (verdict === "pass") {
      verdictInner = '<span class="verdict-badge verdict-pass">pass</span>';
    } else if (verdict === "reject") {
      verdictInner = '<span class="verdict-badge verdict-reject">reject</span>';
    } else {
      verdictInner = '<span class="verdict-placeholder">review</span>';
    }

    const conflictHTML = conflicts[dataIdx]
      ? '<span class="conflict-icon' + (resolvedConflicts.has(dataIdx) ? ' resolved-icon' : '') + '">' +
        (resolvedConflicts.has(dataIdx) ? '&#10003;' : '!') + '</span>'
      : '';

    var roClass = readonly ? " readonly" : "";
    return '<div class="cell cell-chunk' + (isActive && activeCol === 0 ? ' focused' : '') + '" data-col="0">' +
      '<div class="chunk-header">' +
        '<div class="dropdown-wrapper verdict-dropdown' + roClass + '" data-col="0" data-data-idx="' + dataIdx + '">' +
          verdictInner +
        '</div>' +
        '<span class="meta"><span>' + escHTML(row.source_title || "") + ' (' + (row.year || "") + ')</span></span>' +
        conflictHTML +
      '</div>' +
      '<div class="extract-text' + clipped + '">' + escHTML(row.extract || "") + '</div>' +
      '<div class="meta">' +
        '<span>Ch: ' + escHTML(row.chapter || "") + '</span>' +
        '<span>Themes: ' + escHTML(row.themes || "") + '</span>' +
      '</div>' +
    '</div>';
  }

  function buildDecisionCell(dataIdx, col, label, originalValue, overrideValue, extraInfo, isActive) {
    const displayValue = overrideValue || originalValue || "";
    const isOverridden = overrideValue && overrideValue !== originalValue;
    const focused = isActive && activeCol === col ? " focused" : "";
    const roClass = readonly ? " readonly" : "";

    return '<div class="cell cell-decision' + focused + roClass + '" data-col="' + col + '" data-data-idx="' + dataIdx + '">' +
      '<div class="cell-label">' + label + '</div>' +
      '<div class="dropdown-wrapper' + roClass + '" data-col="' + col + '" data-data-idx="' + dataIdx + '">' +
        '<span class="current-value">' + escHTML(displayValue) + '</span>' +
      '</div>' +
      (isOverridden ? '<div class="override-note">was: ' + escHTML(originalValue) + '</div>' : '') +
      (extraInfo ? '<div class="rationale">' + escHTML(extraInfo) + '</div>' : '') +
    '</div>';
  }

  function buildCardHTML(dataIdx, row, dec, isActive) {
    const verdict = dec.verdict || "";
    const verdictHTML = verdict
      ? '<span class="verdict-badge verdict-' + verdict + '">' + verdict + '</span> '
      : '';

    return '<div class="cell cell-chunk">' +
        '<div>' + verdictHTML +
          '<span class="meta"><span>' + escHTML(row.source_title || "") + ' (' + (row.year || "") + ')</span></span>' +
        '</div>' +
        '<div class="extract-text">' + escHTML(row.extract || "") + '</div>' +
        '<div class="meta">' +
          '<span>Ch: ' + escHTML(row.chapter || "") + '</span>' +
          '<span>Themes: ' + escHTML(row.themes || "") + '</span>' +
        '</div>' +
      '</div>' +
      '<div class="decision-row">' +
        buildDecisionCell(dataIdx, 1, "Step", row.pipeline_step, dec.pipeline_step, "") +
        buildDecisionCell(dataIdx, 2, "Type", row.extract_type, dec.extract_type, "") +
        buildDecisionCell(dataIdx, 3, "Rel", row.llm_relevance, dec.llm_relevance, "") +
      '</div>' +
      (row.relevance_rationale ? '<div class="rationale" style="padding:4px 0;font-size:11px;color:var(--fg-muted);font-style:italic">' + escHTML(row.relevance_rationale) + '</div>' : '');
  }

  function escHTML(s) {
    return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  function scrollToActiveRow() {
    const container = scrollContainer();
    const rh = getRowHeight();
    const rowTop = activeRow * rh;
    const rowBottom = rowTop + rh;
    const viewTop = container.scrollTop;
    const viewBottom = viewTop + container.clientHeight;

    if (rowTop < viewTop) {
      container.scrollTop = rowTop;
    } else if (rowBottom > viewBottom) {
      container.scrollTop = rowBottom - container.clientHeight;
    }
    renderVisibleRows();
  }

  function setActiveRow(visIdx) {
    if (visIdx < 0 || visIdx >= filteredIndices.length) return;
    activeRow = visIdx;
    closeDropdown();
    scrollToActiveRow();
  }

  // =========================================================================
  // 4. KEYBOARD HANDLER
  // =========================================================================
  function handleKeydown(e) {
    // Modals open — only handle Esc
    if (!document.getElementById("modal-overlay").classList.contains("hidden")) {
      if (e.key === "Escape") closeModal();
      return;
    }
    if (!document.getElementById("gh-modal").classList.contains("hidden")) {
      if (e.key === "Escape") ghCloseSettings();
      return;
    }

    const key = e.key;

    // Arrow navigation
    if (key === "ArrowDown") {
      e.preventDefault();
      setActiveRow(Math.min(activeRow + 1, filteredIndices.length - 1));
      return;
    }
    if (key === "ArrowUp") {
      e.preventDefault();
      setActiveRow(Math.max(activeRow - 1, 0));
      return;
    }
    if (key === "ArrowRight" && !openDropdown) {
      e.preventDefault();
      activeCol = Math.min(activeCol + 1, 3);
      renderVisibleRows();
      return;
    }
    if (key === "ArrowLeft" && !openDropdown) {
      e.preventDefault();
      activeCol = Math.max(activeCol, 1);
      activeCol = Math.max(activeCol - 1, 1);
      renderVisibleRows();
      return;
    }

    // Enter — toggle dropdown (editing only)
    if (key === "Enter") {
      e.preventDefault();
      if (readonly) return;
      if (activeCol >= 1 && activeCol <= 3) {
        if (openDropdown && openDropdown.col === activeCol) {
          closeDropdown();
        } else {
          openDropdownFor(filteredIndices[activeRow], activeCol);
        }
      }
      return;
    }

    // Escape — close dropdown or deselect
    if (key === "Escape") {
      e.preventDefault();
      if (openDropdown) {
        closeDropdown();
      }
      return;
    }

    // Number shortcuts (1-9, editing only)
    const num = parseInt(key);
    if (readonly) return;
    if (num >= 1 && num <= 9 && activeCol >= 0) {
      e.preventDefault();
      const col = activeCol < 1 ? 0 : activeCol;
      const options = COL_OPTIONS[col];
      if (options && num <= options.length) {
        applyDecision(filteredIndices[activeRow], col, options[num - 1]);
        closeDropdown();
      }
      return;
    }
  }

  // =========================================================================
  // 5. DROPDOWN MANAGER
  // =========================================================================
  function openDropdownFor(dataIdx, col) {
    closeDropdown();
    openDropdown = { dataIdx: dataIdx, col: col };

    const wrapper = visibleRowsEl().querySelector(
      '.dropdown-wrapper[data-col="' + col + '"][data-data-idx="' + dataIdx + '"]'
    );
    if (!wrapper) return;

    const options = COL_OPTIONS[col];
    const currentValue = getEffectiveValue(dataIdx, col);

    const menu = document.createElement("div");
    menu.className = "dropdown-menu open";

    options.forEach(function (opt, i) {
      const item = document.createElement("div");
      item.className = "dropdown-item" + (opt === currentValue ? " selected" : "");
      item.innerHTML = escHTML(opt) + '<span class="shortcut">' + (i + 1) + '</span>';
      item.addEventListener("click", function (e) {
        e.stopPropagation();
        applyDecision(dataIdx, col, opt);
        closeDropdown();
      });
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
    const field = COLS[col];
    const dec = decisions[dataIdx];
    if (dec && dec[field] !== undefined) return dec[field];
    const row = allRows[dataIdx];
    return row[field] || "";
  }

  function applyDecision(dataIdx, col, value) {
    if (readonly) return;
    if (!decisions[dataIdx]) {
      decisions[dataIdx] = { timestamp: Date.now() };
    }
    decisions[dataIdx][COLS[col]] = value;
    decisions[dataIdx].timestamp = Date.now();

    // Implicit approval: changing any decision column implies pass
    if (col >= 1 && !decisions[dataIdx].verdict) {
      decisions[dataIdx].verdict = "pass";
    }

    updateProgress();
    renderVisibleRows();
    ghScheduleSave();
  }

  // =========================================================================
  // 6. TOUCH HANDLER
  // =========================================================================
  let touchTimer = null;
  let touchTarget = null;
  let pillStripActive = false;

  function handleTouchStart(e) {
    if (readonly) return;
    const wrapper = e.target.closest(".dropdown-wrapper");
    if (!wrapper) return;

    const col = parseInt(wrapper.dataset.col);
    const dataIdx = parseInt(wrapper.dataset.dataIdx);
    touchTarget = { col: col, dataIdx: dataIdx, x: e.touches[0].clientX, y: e.touches[0].clientY };

    touchTimer = setTimeout(function () {
      showPillStrip(touchTarget.col, touchTarget.dataIdx, touchTarget.x, touchTarget.y);
      pillStripActive = true;
    }, 150);
  }

  function handleTouchMove(e) {
    if (!pillStripActive) return;
    e.preventDefault();
    const touch = e.touches[0];
    const el = document.elementFromPoint(touch.clientX, touch.clientY);
    document.querySelectorAll(".pill").forEach(function (p) { p.classList.remove("active"); });
    if (el && el.classList.contains("pill")) {
      el.classList.add("active");
    }
  }

  function handleTouchEnd(e) {
    if (touchTimer) {
      clearTimeout(touchTimer);
      touchTimer = null;
    }

    if (pillStripActive) {
      // Select highlighted pill
      const activePill = document.querySelector(".pill.active");
      if (activePill && touchTarget) {
        applyDecision(touchTarget.dataIdx, touchTarget.col, activePill.dataset.value);
      }
      pillStripActive = false;
      document.getElementById("pill-strip").classList.add("hidden");
    } else if (touchTarget) {
      // Short tap — open dropdown
      openDropdownFor(touchTarget.dataIdx, touchTarget.col);
    }

    touchTarget = null;
  }

  function showPillStrip(col, dataIdx, x, y) {
    const strip = document.getElementById("pill-strip");
    strip.innerHTML = "";
    const options = COL_OPTIONS[col];

    options.forEach(function (opt) {
      const pill = document.createElement("div");
      pill.className = "pill";
      pill.dataset.value = opt;
      pill.textContent = opt.length > 7 ? opt.substring(0, 6) + "\u2026" : opt;
      strip.appendChild(pill);
    });

    strip.classList.remove("hidden");

    // Position 60px above touch point
    const stripWidth = Math.min(options.length * 72, window.innerWidth * 0.95);
    strip.style.left = Math.max(4, Math.min(x - stripWidth / 2, window.innerWidth - stripWidth - 4)) + "px";
    strip.style.top = Math.max(4, y - 60) + "px";
  }

  // =========================================================================
  // 7. FILTER ENGINE
  // =========================================================================
  function applyFilters() {
    const hideReviewed = document.getElementById("hide-reviewed").checked;
    const conflictsOnly = document.getElementById("conflicts-only").checked;
    const showResolved = document.getElementById("conflict-resolved").checked;
    const stepFilter = document.getElementById("filter-step").value;
    const typeFilter = document.getElementById("filter-type").value;
    const relFilter = document.getElementById("filter-relevance").value;

    filteredIndices = [];
    for (let i = 0; i < allRows.length; i++) {
      const row = allRows[i];
      const dec = decisions[i];

      if (hideReviewed && dec) continue;
      if (conflictsOnly && !conflicts[i]) continue;
      if (conflictsOnly && !showResolved && resolvedConflicts.has(i)) continue;

      const effStep = (dec && dec.pipeline_step) || row.pipeline_step;
      const effType = (dec && dec.extract_type) || row.extract_type;
      const effRel = (dec && dec.llm_relevance) || row.llm_relevance;

      if (stepFilter && effStep !== stepFilter) continue;
      if (typeFilter && effType !== typeFilter) continue;
      if (relFilter && effRel !== relFilter) continue;

      filteredIndices.push(i);
    }

    activeRow = Math.min(activeRow, Math.max(0, filteredIndices.length - 1));
    writeFiltersToURL();
    updateProgress();

    // Update spacer before scrolling so browser doesn't clamp to old height
    var rh = getRowHeight();
    scrollSpacer().style.height = (filteredIndices.length * rh) + "px";
    scrollToActiveRow();
  }

  function clearAllFilters() {
    document.getElementById("hide-reviewed").checked = false;
    document.getElementById("conflicts-only").checked = false;
    document.getElementById("conflict-resolved").checked = false;
    document.getElementById("filter-step").value = "";
    document.getElementById("filter-type").value = "";
    document.getElementById("filter-relevance").value = "";
    activeRow = 0;
    applyFilters();
  }

  function writeFiltersToURL() {
    const params = [];
    const step = document.getElementById("filter-step").value;
    const type = document.getElementById("filter-type").value;
    const rel = document.getElementById("filter-relevance").value;
    const hr = document.getElementById("hide-reviewed").checked;
    const co = document.getElementById("conflicts-only").checked;
    const cr = document.getElementById("conflict-resolved").checked;

    if (step) params.push("step=" + encodeURIComponent(step));
    if (type) params.push("type=" + encodeURIComponent(type));
    if (rel) params.push("rel=" + encodeURIComponent(rel));
    if (hr) params.push("hide=1");
    if (co) params.push("conflicts=1");
    if (cr) params.push("resolved=1");

    window.location.hash = params.join("&");
  }

  function readFiltersFromURL() {
    const hash = window.location.hash.replace(/^#/, "");
    if (!hash) return;
    const params = {};
    hash.split("&").forEach(function (pair) {
      const parts = pair.split("=");
      params[parts[0]] = decodeURIComponent(parts[1] || "");
    });

    if (params.step) document.getElementById("filter-step").value = params.step;
    if (params.type) document.getElementById("filter-type").value = params.type;
    if (params.rel) document.getElementById("filter-relevance").value = params.rel;
    if (params.hide) document.getElementById("hide-reviewed").checked = true;
    if (params.conflicts) document.getElementById("conflicts-only").checked = true;
    if (params.resolved) document.getElementById("conflict-resolved").checked = true;
  }

  function updateProgress() {
    const reviewed = Object.keys(decisions).length;
    const total = allRows.length;
    const visible = filteredIndices.length;
    document.getElementById("progress").textContent =
      reviewed + " / " + total + " reviewed (" + visible + " visible)";
  }

  function populateFilterDropdowns() {
    const stepSel = document.getElementById("filter-step");
    PIPELINE_STEPS.forEach(function (s) {
      var o = document.createElement("option");
      o.value = s; o.textContent = s;
      stepSel.appendChild(o);
    });

    var typeSel = document.getElementById("filter-type");
    EXTRACT_TYPES.forEach(function (t) {
      var o = document.createElement("option");
      o.value = t; o.textContent = t;
      typeSel.appendChild(o);
    });

    var relSel = document.getElementById("filter-relevance");
    RELEVANCE_VALUES.forEach(function (r) {
      var o = document.createElement("option");
      o.value = r; o.textContent = r;
      relSel.appendChild(o);
    });
  }

  // =========================================================================
  // 8. DECISION I/O
  // =========================================================================
  function exportDecisions() {
    var data = {
      tool: "horizon-review",
      version: 1,
      exported: new Date().toISOString(),
      total_rows: allRows.length,
      reviewed_count: Object.keys(decisions).length,
      decisions: decisions
    };

    var blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json" });
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    a.download = "horizon-decisions-" + new Date().toISOString().slice(0, 10) + ".json";
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
      document.getElementById("import-status").textContent = "No files selected.";
      return;
    }

    var pending = files.length;
    var allImported = [];

    Array.from(files).forEach(function (file) {
      var reader = new FileReader();
      reader.onload = function (e) {
        try {
          var data = JSON.parse(e.target.result);
          if (data.decisions) {
            allImported.push({ source: file.name, decisions: data.decisions });
          }
        } catch (err) {
          document.getElementById("import-status").textContent = "Error parsing " + file.name;
        }
        pending--;
        if (pending === 0) {
          mergeImports(allImported);
          closeModal();
        }
      };
      reader.readAsText(file);
    });
  }

  function mergeImports(imports) {
    var newConflicts = 0;

    imports.forEach(function (imp) {
      Object.keys(imp.decisions).forEach(function (key) {
        var idx = parseInt(key);
        var incoming = imp.decisions[key];

        if (!decisions[idx]) {
          // No existing decision — accept
          decisions[idx] = incoming;
        } else {
          // Check for conflicts
          var existing = decisions[idx];
          var hasConflict = false;

          COLS.forEach(function (field) {
            if (incoming[field] !== undefined && existing[field] !== undefined &&
                incoming[field] !== existing[field]) {
              hasConflict = true;
              if (!conflicts[idx]) conflicts[idx] = {};
              if (!conflicts[idx][field]) conflicts[idx][field] = [];

              // Store both versions
              var existingEntry = { value: existing[field], timestamp: existing.timestamp, source: "existing" };
              var incomingEntry = { value: incoming[field], timestamp: incoming.timestamp, source: imp.source };

              // Avoid duplicate entries
              var hasExisting = conflicts[idx][field].some(function(c) { return c.source === "existing"; });
              if (!hasExisting) conflicts[idx][field].push(existingEntry);
              conflicts[idx][field].push(incomingEntry);
            }
          });

          if (hasConflict) {
            newConflicts++;
          } else {
            // No conflict — merge (latest timestamp wins for each field)
            COLS.forEach(function (field) {
              if (incoming[field] !== undefined) {
                if (!existing[field] || incoming.timestamp > existing.timestamp) {
                  existing[field] = incoming[field];
                }
              }
            });
            existing.timestamp = Math.max(existing.timestamp || 0, incoming.timestamp || 0);
          }
        }
      });
    });

    var status = imports.reduce(function(sum, imp) { return sum + Object.keys(imp.decisions).length; }, 0) +
      " decisions imported";
    if (newConflicts > 0) status += ", " + newConflicts + " conflicts detected";
    document.getElementById("import-status").textContent = status;

    applyFilters();
  }

  // =========================================================================
  // 9. CONFLICT RESOLVER
  // =========================================================================
  // Conflicts are surfaced visually via CSS classes applied in buildRow().
  // Resolution: when a user changes a value on a conflicted row, it resolves
  // that field's conflict. When all fields are resolved, the row is marked resolved.

  function resolveConflict(dataIdx, field, value) {
    if (conflicts[dataIdx] && conflicts[dataIdx][field]) {
      delete conflicts[dataIdx][field];
      if (Object.keys(conflicts[dataIdx]).length === 0) {
        delete conflicts[dataIdx];
        resolvedConflicts.add(dataIdx);
      }
    }
    applyDecision(dataIdx, COLS.indexOf(field), value);
  }

  // Override applyDecision to also resolve conflicts
  var _origApplyDecision = applyDecision;
  applyDecision = function (dataIdx, col, value) {
    var field = COLS[col];
    if (conflicts[dataIdx] && conflicts[dataIdx][field]) {
      resolveConflict(dataIdx, field, value);
      return;
    }
    _origApplyDecision(dataIdx, col, value);
  };

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
    path: "research/pipeline-canon/decisions.json"
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
      tool: "horizon-review",
      version: 1,
      exported: new Date().toISOString(),
      total_rows: allRows.length,
      reviewed_count: Object.keys(decisions).length,
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
          // File doesn't exist yet — that's fine, we'll create it on first save
          gh.sha = "";
          gh.connected = true;
          readonly = false;
          ghSaveCredentials();
          ghUpdateIndicator();
          ghSetStatus("Connected (no decisions yet)", 3000);
          pollTimer = setInterval(ghPoll, POLL_INTERVAL);
          renderVisibleRows();
          return;
        }
        if (!resp.ok) throw new Error("HTTP " + resp.status);
        return resp.json();
      })
      .then(function (data) {
        if (!data) return; // handled in 404 branch
        gh.sha = data.sha;
        gh.connected = true;
        readonly = false;
        ghSaveCredentials();
        ghUpdateIndicator();

        // Decode and load decisions
        var json = atob(data.content.replace(/\n/g, ""));
        var parsed = JSON.parse(json);
        if (parsed.decisions && Object.keys(parsed.decisions).length > 0) {
          mergeImports([{ source: "github", decisions: parsed.decisions }]);
          ghSetStatus("Loaded " + Object.keys(parsed.decisions).length + " decisions", 3000);
        } else {
          ghSetStatus("Connected", 3000);
        }
        pollTimer = setInterval(ghPoll, POLL_INTERVAL);
        renderVisibleRows();
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
    renderVisibleRows();
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
      message: "Update review decisions (" + Object.keys(decisions).length + " reviewed)",
      content: btoa(unescape(encodeURIComponent(payload))),
      committer: { name: "Horizon Review", email: "noreply@review.tool" }
    };
    if (gh.sha) body.sha = gh.sha;

    fetch(ghApiUrl(), {
      method: "PUT",
      headers: ghHeaders(),
      body: JSON.stringify(body)
    })
      .then(function (resp) {
        if (resp.status === 409) {
          // SHA mismatch — re-fetch and retry
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
          mergeImports([{ source: "github", decisions: parsed.decisions }]);
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
    fetch(ghApiUrl(), {
      method: "HEAD",
      headers: ghHeaders()
    }).catch(function () {
      // HEAD not reliable on GitHub Contents API, use GET with If-None-Match
    });
    // Simpler: just GET and check sha
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
            mergeImports([{ source: "github-poll", decisions: parsed.decisions }]);
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
    document.getElementById("gh-input-path").value = gh.path || GH_DEFAULTS.path;
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
    gh.path = document.getElementById("gh-input-path").value.trim();

    if (!gh.token) {
      document.getElementById("gh-modal-status").textContent = "Token is required.";
      return;
    }

    ghCloseSettings();
    ghConnect(false);
  }

  // =========================================================================
  // 11. INIT
  // =========================================================================
  // Theme toggle — user-controlled light/dark, persisted to localStorage
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

  function init() {
    // Theme
    initTheme();

    // Detect mobile
    isMobile = window.innerWidth <= 768;
    window.addEventListener("resize", function () {
      var wasMobile = isMobile;
      isMobile = window.innerWidth <= 768;
      if (wasMobile !== isMobile) renderVisibleRows();
    });

    // Load data
    loadData();

    // Populate filter dropdowns
    populateFilterDropdowns();

    // Read URL filters
    readFiltersFromURL();

    // Initial filter
    filteredIndices = [];
    for (var i = 0; i < allRows.length; i++) filteredIndices.push(i);
    applyFilters();

    // Scroll handler
    scrollContainer().addEventListener("scroll", renderVisibleRows);

    // Keyboard
    document.addEventListener("keydown", handleKeydown);

    // Touch
    document.addEventListener("touchstart", handleTouchStart, { passive: true });
    document.addEventListener("touchmove", handleTouchMove, { passive: false });
    document.addEventListener("touchend", handleTouchEnd, { passive: true });

    // Close dropdown on outside click.
    // Guard: if target was detached by renderVisibleRows (DOM rebuild), skip —
    // otherwise the document handler fires after the cell-click handler re-renders
    // and immediately closes the dropdown it just opened.
    document.addEventListener("click", function (e) {
      if (!openDropdown) return;
      if (!document.contains(e.target)) return;
      if (e.target.closest(".dropdown-menu") || e.target.closest(".dropdown-wrapper") || e.target.closest(".cell-decision")) return;
      closeDropdown();
    });

    // Toolbar bindings
    document.getElementById("hide-reviewed").addEventListener("change", applyFilters);
    document.getElementById("conflicts-only").addEventListener("change", applyFilters);
    document.getElementById("conflict-resolved").addEventListener("change", applyFilters);
    document.getElementById("filter-step").addEventListener("change", applyFilters);
    document.getElementById("filter-type").addEventListener("change", applyFilters);
    document.getElementById("filter-relevance").addEventListener("change", applyFilters);
    document.getElementById("btn-clear").addEventListener("click", clearAllFilters);
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

    // Initial render
    renderVisibleRows();
    updateProgress();

    // Try auto-connect from stored credentials
    ghInit();
  }

  // Boot
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
