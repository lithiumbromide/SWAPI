---
title: "Sketch Ink Toolbar"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/ToolbarSketchInk.htm"
---

# Sketch Ink Toolbar

Visible only on Windows 10:

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comments |
| --- | --- | --- | --- |
| Pen > Colors | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPenSketchStrokeColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPenSketchStrokeColor, < Value >) | COLORREF value | COLORREF values in SOLIDWORKS IColorTable ; use function RGB to convert R,G, and B values to COLORREF values; the following colors are displayed in the graphic from left to right and top to bottom: RGB(0,0,0) RGB(102,102,102) RGB(153,153,153) RGB(221,221,221) RGB(255,255,255) RGB(204,0,0) RGB(255,153,0) RGB(255,255,0) RGB(0,158,15) RGB(153,0,255) RGB(255,0,255) RGB(147,196,125) RGB(255,217,102) RGB(142,124,195) RGB(194,123,160) RGB(111,168,220) RGB(56,118,29) RGB(224,102,102) RGB(97,61,48) |
| Pen > Size | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPenSketchStrokeThickness) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPenSketchStrokeThickness, < Value >) | Valid options as defined in swLineWeights_e : swLW_THIN swLW_NORMAL swLW_THICK swLW_THICK2 swLW_THICK3 swLW_THICK4 swLW_THICK5 | Thickness of pen stroke; if you set an invalid value (<0 or >6) then the pen size is automatically set to swLW_THIN = 0 |
