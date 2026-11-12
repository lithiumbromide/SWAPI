---
title: "System Options > Drawings > Display Style"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_Drawings-DisplayStyle.htm"
---

# System Options > Drawings > Display Style

This topic contains two tables. The information in the table:

- appearing immediately after the screen capture of the dialog corresponds to the settings on that dialog.
- titled [Obsolete Enumerators](#Obsolete) contains enumerators that previously appeared on the dialog but are now obsolete.

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Display style - Wireframe | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swHiddenEdgeDisplayDefault) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swHiddenEdgeDisplayDefault, <swDisplayMode_e.swWIREFRAME) | See swDisplayMode_e for valid options |  |
| Display style - Hidden lines visible | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swHiddenEdgeDisplayDefault) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swHiddenEdgeDisplayDefault, <swDisplayMode_e.swHIDDEN_GREYED) | See swDisplayMode_e for valid options |  |
| Display style - Hidden lines removed | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swHiddenEdgeDisplayDefault) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swHiddenEdgeDisplayDefault, <swDisplayMode_e.swHIDDEN) | See swDisplayMode_e for valid options |  |
| Display style - Shaded with edges | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swHiddenEdgeDisplayDefault) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swHiddenEdgeDisplayDefault, <swDisplayMode_e.swSHADED) | See swDisplayMode_e for valid options | To display a drawing view shaded with edges, also set ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingsDefaultDisplayTypeHLREdgesWhenShaded, True) |
| Display style - Shaded | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingsDefaultDisplayTypeHLREdgesWhenShaded) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingsDefaultDisplayTypeHLREdgesWhenShaded, < OnFlag >) | Boolean value |  |
| Tangent edges - Visible | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTangentEdgeDisplayDefault) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTangentEdgeDisplayDefault, <swDisplayTangentEdges_e.swTangentEdgesVisible) | See swDisplayTangentEdges_e for valid options | Specifies tangent edges using a solid line |
| Tangent edges - Use font | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTangentEdgeDisplayDefault) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTangentEdgeDisplayDefault, <swDisplayTangentEdges_e.swTangentEdgesVisibleAndFonted) | See swDisplayTangentEdges_e for valid options | Specifies tangent edges using a line in the default font |
| Tangent edges - Hide ends | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingHideEnds) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingHideEnds, < OnFlag >) | Boolean value | Specifies whether to hide the start and end segments of tangent edges |
| Tangent edges - Removed | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTangentEdgeDisplayDefault) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTangentEdgeDisplayDefault, <swDisplayTangentEdges_e.swTangentEdgesHidden) | See swDisplayTangentEdges_e for valid options | Specifies to not display tangent edges |
| Edge quality for wireframe and hidden views - High/Draft quality | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgeQualityWireframeHiddenViews) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgeQualityWireframeHiddenViews, False) | Boolean value | True for high edge quality for wireframe and hidden views; false for draft edge quality |
| Edge quality for shaded edge views - High/Draft quality | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgeQualityShadedEdgeViews) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgeQualityShadedEdgeViews, True) | Boolean value | True for high edge quality for shaded edge views; false for draft edge quality |

Obsolete Enumerators

| Enumerator | Comment |
| --- | --- |
| swDrawingsDefaultDisplayTypeFastHLRHLV | Obsolete ; specified the display quality for new drawing views |
