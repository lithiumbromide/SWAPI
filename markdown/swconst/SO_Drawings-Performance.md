---
title: "System Options > Drawings > Performance"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_Drawings-Performance.htm"
---

# System Options > Drawings > Performance

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Show contents while dragging drawing view | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingViewShowContentsWhileDragging) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingViewShowContentsWhileDragging,
< OnFlag >) | Boolean value | Specifies whether model or view boundary is displayed when view is dragged |
| Allow auto-update when opening drawings | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swAutomaticDrawingViewUpdateDefault ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swAutomaticDrawingViewUpdateDefault,
< OnFlag >) | Boolean value | Specifies whether drawing views are updated when a drawing is opened |
| Save tessellated data for drawings with shaded and draft quality views | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingSaveShadedData) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingSaveShadedData,
< OnFlag >) | Boolean value | Specifies whether to save tessellated data in drawing documents with shaded
and draft quality views |
| Turn Off Automatic Solve Mode and Undo and turn on No Solve Mode when drawing
view contains more than... | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingTurnOffAutomaticSolveModeAndUndo) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingTurnOffAutomaticSolveModeAndUndo,
< OnFlag >) | Boolean value | True to turn off Automatic Solve Mode and Undo and turn on No Solve
Mode when drawing view contains more than the specified number of sketch
entities False to turn on Automatic Solve Mode and Undo and turn off No Solve
Mode when drawing view contains more than the specified number of sketch
entities |
| this number of sketch entities | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDrawing_Auto_Solve_Threshold) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDrawing_Auto_Solve_Threshold,
< Value >) | Integer value | The specified number of sketch entities mentioned in the previous
comment |
| Always open a drawing in detailing mode | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingOpenInDetailingMode) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingOpenInDetailingMode,
< OnFlag >) | Boolean value |  |
