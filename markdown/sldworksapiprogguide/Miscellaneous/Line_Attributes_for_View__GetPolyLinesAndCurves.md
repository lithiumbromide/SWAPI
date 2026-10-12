---
title: "Line Attributes for View::GetPolyLinesAndCurves"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Miscellaneous/Line_Attributes_for_View__GetPolyLinesAndCurves.htm"
---

# Line Attributes for View::GetPolyLinesAndCurves

## Line Attributes for IView::GetPolyLinesAndCurves

- LineColor = polyline color. This value is determined either by the explicitly set value or by the layer that the polyline is on.
- LineStyle = value combines polyline font and weight information. This value can be used as an input to GetLineFontInfo and GetLineFontName. If this value is -1, then the user has probably modified the line display manually in the drawing, and you should use the LineFont and LineWeight return values to recreate the exact polyline style.
- LineFont = value is used for polyline font information. This value can be used as an input to the GetLineFontInfo2 and GetLineFontName2 functions. This value will only be valid if LineStyle is -1.
- LineWeight = polyline weight where Thin = 0.0, Normal = 1.0, Thick = 2.0. This value will only be valid if LineStyle is -1.
- LayerID = integer value indicating which layer holds this polyline. The ILayer object can be obtained by passing this integer value to ILayerMgr::GetLayerById.
- LayerOverride = integer with bit flags set to determine which properties, if any, have been overridden with respect to the layer default properties. If a bit flag is set, then the corresponding property or has been overridden. The bit flags are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride is 3, then LineColor and LineStyle override the default color and style of the layer.
