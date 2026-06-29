/*!
 * responsive-table.js
 * Transforms standard table.responsive tables into the responsive label pattern.
 *
 * Usage: add class="responsive" to any <table>, then include this script.
 * It reads each column header from <thead> and injects a hidden <span class="label">
 * alongside a <span class="data"> wrapper inside every <td> — the same markup the
 * CSS expects. No configuration required.
 *
 * Safe to include multiple times; already-transformed cells are skipped.
 */
(function () {
  'use strict';

  function transform(table) {
    var headerRow = table.querySelector('thead tr');
    if (!headerRow) return;

    var headers = Array.from(headerRow.querySelectorAll('th')).map(function (th) {
      return th.textContent.trim();
    });
    if (!headers.length) return;

    table.querySelectorAll('tbody tr').forEach(function (row) {
      row.querySelectorAll('td').forEach(function (td, i) {
        if (td.querySelector('.label')) return; // already transformed

        var labelSpan = document.createElement('span');
        labelSpan.className = 'label';
        labelSpan.textContent = headers[i] !== undefined ? headers[i] : '';

        var dataSpan = document.createElement('span');
        dataSpan.className = 'data';
        while (td.firstChild) {
          dataSpan.appendChild(td.firstChild);
        }

        td.appendChild(labelSpan);
        td.appendChild(dataSpan);
      });
    });
  }

  function init() {
    document.querySelectorAll('table.responsive').forEach(transform);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
}());
