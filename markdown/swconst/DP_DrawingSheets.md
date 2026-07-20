---
title: "Document Properties > Drawing Sheets"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_DrawingSheets.htm"
---

# Document Properties > Drawing Sheets

HTML PUBLIC "-//W3C//DTD HTML 4.0 Frameset//EN"

(==============================================================)

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Sheet format for new sheets - Use different sheet format | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingSheetsUseDifferentSheetFormat,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingSheetsUseDifferentSheetFormat,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to use a different sheet format |
| Sheet format for new sheets - Sheet format file location | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swFileLocationsNewSheetFormat,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceString (swUserPreferenceStringValue_e.swFileLocationsNewSheetFormat,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | String value | Specifies the location of the sheet format file to use |
| Zones - Origin | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDrawingSheetsZonesOrigin,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDrawingSheetsZonesOrigin,
swUserPreferenceOption_e.swDetailingNoOptionSpecified,
swDrawingSheetsZonesOrigin_e.< Value >) | See swDrawingSheetsZonesOrigin_e for valid options | Specifies the corner where the lowest letters and numbers start on the drawing
sheet |
| Zones - Letter Layout | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDrawingSheetsZonesLetterLayout,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDrawingSheetsZonesLetterLayout,
swUserPreferenceOption_e.swDetailingNoOptionSpecified,
swDrawingSheetsZonesLetterLayout_e.< Value >) | See swDrawingSheetsZonesLetterLayout_e for valid options | Specifies where the letters and numbers appear on the drawing sheet |
| Zones - List number first in Zone callout | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingSheetsListNumFirstInZoneCallout,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingSheetsListNumFirstInZoneCallout,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value > | Boolean value | Specifies whether to list letter or number as first character in zone callouts: Letter first (A1, B3, C4,
etc.); default Number first (1A, 3B, 4C,
etc.) |
| Zones - Continue column iteration across sheets | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingSheetsContinueColumnIteration,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingSheetsContinueColumnIteration,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to restart columns or rows (default) across drawing sheets;
(i.e., A, B, C, etc.) |
| Multi-sheet custom properties source - Use custom property values from
this sheet on all sheets | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingSheetsMatchCustomPropVals,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingSheetsMatchCustomPropVals,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to use custom property values from this sheet on all
sheets |
| Multi-sheet custom properties source - Sheet number | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDrawingSheetCustomPropSheetNo,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDrawingSheetCustomPropSheetNo,
swUserPreferenceOption_e.swDetailingNoOptionSpecified,
< Value >) | Integer value | Sheet number |
| Store images for OLE object data in drawing file (Note: will increase file
size) | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swStoreOLEImagesWithModel,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swStoreOLEImagesWithModel,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For drawings |
