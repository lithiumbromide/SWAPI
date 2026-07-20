---
title: "System Options > Drawings"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_Drawings.htm"
---

# System Options > Drawings

This topic contains two tables. The information in the table:

- appearing immediately after the screen capture
  of the dialog corresponds to the settings on
  that dialog.

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Zoom level to open drawings | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swZoomLevelOnOpen) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swZoomLevelOnOpen,
swZoomLevelOnOpenType_e.<Value>) | See swZoomLevelOnOpenType_e for valid options |  |
| Eliminate duplicate model dimensions on insert | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingEliminateDuplicateDimsOnInsert) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingEliminateDuplicateDimsOnInsert, <OnFlag> ) | Boolean value | Specifies whether duplicate dimensions are eliminated when model dimensions
inserted |
| Eliminate duplicate model notes on
insert | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingEliminateDuplicateModelNotesOnInsert) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingEliminateDuplicateModelNotesOnInsert, <OnFlag> ) | Boolean value | Specifies whether to eliminate
duplicate notes when model notes are inserted in a drawing |
| Mark all part/assembly dimension for import into drawings by default | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingMarkAllDimensionsForDrawing) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingMarkAllDimensionsForDrawing, <OnFlag> ) | Boolean value | Specifies whether to mark all part and assembly dimensions for import
into drawings by default |
| Automatically scale new drawing views | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swAutomaticScaling3ViewDrawings) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swAutomaticScaling3ViewDrawings, <OnFlag> ) | Boolean value | Specifies whether new views are scaled to fit drawing sheet, regardless
of selected paper size |
| Enable symbol when adding new revision | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingEnableSymbolAddingNewRevision) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingEnableSymbolAddingNewRevision, <OnFlag> ) | Boolean value | Specifies whether to insert revision symbols when a new revision row is added to
a revision table |
| Display new detail circles as circles | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingCreateDetailAsCircle) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingCreateDetailAsCircle, <OnFlag> ) | Boolean value | Specifies whether new profiles for detail views are displayed as circles
or sketched profiles |
| Select hidden entities | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingSelectHiddenEntities) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingSelectHiddenEntities, <OnFlag> ) | Boolean value | Specifies whether hidden tangent edges and edges hidden manually can
be selected |
| Disable note/dimension inference | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingDisableNoteDimensionInference) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingDisableNoteDimensionInference, <OnFlag> ) | Boolean value | Specifies whether to disable note and dimension inferencing in drawings |
| Disable note merging when dragging | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingDisableNoteMergeWhenDragging) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingDisableNoteMergeWhenDragging, <OnFlag> ) | Boolean | Specifies whether to merge two notes, or a note and a dimension, when dragged toward
each other |
| Print out-of-sync water mark | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swRapidDraftPrintOutOfSynchWaterMark) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swRapidDraftPrintOutOfSynchWaterMark, <OnFlag> ) | Boolean value | Specifies whether to print out-of-synch watermarks on detached drawings
printouts if drawings not synchronized with the models |
| Show reference geometry names in drawings | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swShowRefGeomName) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swShowRefGeomName, <OnFlag> ) | Boolean value | Specifies whether to show names of reference geometry entities when
imported into a drawing |
| Automatically hide components on view creation | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingViewAutoHideComponents) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingViewAutoHideComponents, <OnFlag> ) | Boolean value | Specifies whether any components of assembly not visible in a new drawing
view are hidden |
| Display sketch arc centerpoints | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingDisplayArcCenterPoints) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingDisplayArcCenterPoints, <OnFlag> ) | Boolean value | Specifies whether to display arc center points |
| Display sketch entity points | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingDisplayEntityPoints) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingDisplayEntityPoints, <OnFlag> ) | Boolean value | Specifies whether to display sketch entity points |
| Display sketch hatch behind geometry | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingDisplaySketchHatchBehindGeometry) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingDisplaySketchHatchBehindGeometry, <OnFlag> ) | Boolean value | Specifies whether to display sketch hatch behind geometry |
| Display sketch pictures on sheet behind geometry | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingDisplaySketchPicturesOnSheetBehindGeometry) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingDisplaySketchPicturesOnSheetBehindGeometry, <OnFlag> ) | Boolean value | Specifies whether to display sketch pictures behind geometry |
| Print breaklines in break view | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingPrintBreaklinesInBrokenView) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingPrintBreaklinesInBrokenView, <OnFlag> ) | Boolean value | Specifies whether to print breaklines in break views |
| Align breaks with parent view for
projected view | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swBreakAlignWithParent ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swBreakAlignWithParent, <OnFlag> ) | Boolean value | Specifies whether to align break
lines of a projected view with its parent view; by default, set to true |
| Automatically populate View Palette with views | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swShowDrawingViewPalette) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swShowDrawingViewPalette, <OnFlag> ) | Boolean value | Specifies whether to show View Palette |
| Show sheet format dialog when adding new sheet | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingShowSheetFormatDialog) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingShowSheetFormatDialog, <OnFlag> ) | Boolean value | Specifies whether to show the drawing sheet format dialog when adding
new drawing sheets |
| Reduce spacing when dimensions are deleted or edited (add or change
tolerance, text etc...) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingAutoSpaceDimsOnDelete) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingAutoSpaceDimsOnDelete, <OnFlag> ) | Boolean value | Specifies whether to adjust spacing when dimensions are deleted or text
is removed |
| Reuse view letters from deleted
auxiliary, detail, and section views | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingReuseViewLettersFromDeletedAuxilary) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingReuseViewLettersFromDeletedAuxilary, <OnFlag> ) | Boolean value | Specifies whether to reuse letters
from deleted views (auxiliary, detail, and section) in the drawing |
| Enable paragraph auto numbering | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swNoteParagraphAutoNumbering) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swNoteParagraphAutoNumbering, <OnFlag> ) | Boolean value | Specifies whether to enable
Microsoft Word-like auto-numbering behavior in notes; enabled by default |
| Zoom to fit on open | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swNoteZoomToFit) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swNoteZoomToFit, <OnFlag> ) | Boolean value | Zoom to fit on open |
| Override quantity column name in Bill Of Materials | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swOverrideQuantityColumnName) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swOverrideQuantityColumnName, <OnFlag> ) | Boolean value | Specifies whether to override the quantity column name in Bill of Materials |
| Name to use | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swOverriddenQuantityColumnName) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swOverriddenQuantityColumnName,
< Value > ) | String value | String for quantity column name in Bill of Materials |
| Detail view scaling | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swDrawingDetailViewScale) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swDrawingDetailViewScale,
< Value >) | Double value | Specifies value to scale detail views |
| Custom property used as Revision | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swDrawingCustomPropertyUsedAsRevision) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swDrawingCustomPropertyUsedAsRevision,
< Value >) | String value | Specifies custom property for drawing revision |
| Keyboard movement increment | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swDrawingKeyboardMovementIncrement) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.wDrawingKeyboardMovementIncrement,
< Value >) | Double value | Specifies the unit value of movement when you use the arrow keys to
move (nudge) drawing views, annotations, or dimensions |

Obsolete Enumerators

(Table)=========================================================

| Enumerator | Comment |
| --- | --- |
| swDrawingDetailinInferCenter | Obsolete ; specified whether borders
are displayed around individual drawing views |
| swDrawingDetailInferCorner | Obsolete ; specified whether when
a corner is clicked and detail item dragged, corner can infer to the corners
of stationary detail items, and vice versa |
| swDrawingAutomaticBOMUpdate | Obsolete ; use document-level property swUserPreferenceToggle_e.swDetailingAutoUpdateBOM |
| swDrawingProjectionType | Obsolete |
