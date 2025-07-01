// ==UserScript==
// @name         Visionpapers Timer Skipper
// @match        https://visionpapers.info/*
// @run-at       document-end
// ==/UserScript==

(function() {
    'use strict';

    // Hijack timer functions to zero-delay
    const origSetTimeout = unsafeWindow.setTimeout;
    unsafeWindow.setTimeout = (fn, delay, ...args) => origSetTimeout(fn, 0, ...args);
    const origSetInterval = unsafeWindow.setInterval;
    unsafeWindow.setInterval = (fn, delay, ...args) => origSetInterval(fn, 0, ...args);

    // Observe DOM to remove overlays and auto-click
    new MutationObserver(() => {
        document.querySelectorAll('.overlay, #timer, .countdown, .wait').forEach(e => e.remove());
        const nextBtn = document.querySelector('a.btn, button.btn');
        if (nextBtn && !nextBtn.disabled) nextBtn.click();
    }).observe(document.body, {childList: true, subtree: true});

    // Run once immediately
    document.querySelectorAll('a.btn, button.btn').forEach(b => b.click());
})();
