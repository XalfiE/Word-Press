# Cross-Browser QA Checklist

**Date:** April 4, 2026  
**Tester:** Freelance WordPress Developer

## Browsers Tested

| Browser | Version | OS | Result |
|---------|---------|-----|--------|
| Google Chrome | 124 | Windows 11 | ✅ Pass |
| Mozilla Firefox | 125 | Windows 11 | ✅ Pass |
| Apple Safari | 17.4 | macOS Sonoma | ✅ Pass |
| Microsoft Edge | 124 | Windows 11 | ✅ Pass |

## Pages Tested

- [x] Homepage — hero, services strip, blog preview, CTA
- [x] About — bio, timeline, recognitions
- [x] Blog archive — post grid, pagination
- [x] Single post — typography, author block, share buttons
- [x] Free Tools — tool card grid, external links
- [x] Contact — WPForms layout, field focus states, submission confirmation

## Devices Tested

- [x] Desktop 1440px
- [x] Laptop 1280px
- [x] Tablet 768px (iPad)
- [x] Mobile 375px (iPhone SE simulation)
- [x] Mobile 390px (iPhone 14 simulation)

## Issues Found and Resolved Prior to QA Sign-off

- Safari 16: `word-break` overflow on About page bio — fixed in child theme CSS
- Firefox: WPForms select arrow styling inconsistent — normalized with custom CSS
- Edge: Form focus ring color not matching — added `outline-offset` override

## Result

✅ QA Pass — All pages render correctly across all tested browsers and viewports.
