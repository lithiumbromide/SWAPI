---
title: "File > Save As > Save as type > Dxf or Dwg > Options"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileSaveAsDXFOptions.htm"
---

# File > Save As > Save as type > Dxf or Dwg > Options

In order to display this dialog, open a part or drawing and:

Click**Tools > Options > System Options > Export >
DXF/DWG**.

- or -

1. Click

  File > Save As

  .
2. In

  Save as type

  , select

  Dxf or Dwg

  .
3. Click

  Options

  .

This topic contains four tables. The information in the table:

- appearing immediately after the screen capture corresponds to the
  settings on that dialog.
- titled

  [Hidden Layers Dialog Enumerators](#HiddenLayers)

  contains enumerators corresponding to options on the hidden layers warning
  dialog that pops up during export to DXF/DWG of drawings that have one or
  more hidden layers.
- titled

  [Miscellaneous
  Enumerators](#Miscellaneous)

  contains miscellaneous DXF/DWG enumerators.
- titled

  [Obsolete
  Enumerators](#Obsolete)

  contains enumerators that previously appeared on the
  dialog but are now obsolete.

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Version | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDxfVersion) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDxfVersion,
swDxfFormat.e.< Value >) | See swDxfFormat_e for valid options |  |
| Fonts | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDxfOutputFonts) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDxfOutputFonts,
swDxfFormat.e.< Value >) | 0 = AutoCAD STANDARD only 1 = TrueType |  |
| Line styles | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDxfOutputLineStyles) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDxfOutputLineStyles,
swDxfFormat.e.< Value >) | 0 = AutoCAD Standard Styles 1 = SOLIDWORKS Custom Styles |  |
| Custom Map SOLIDWORKS to DXF/DWG - Enable | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDxfMapping) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDxfMapping,
< OnFlag >) | Boolean value | Specifies whether to implement mapping |
| Custom Map SOLIDWORKS to DXF/DWG - Don't show mapping on each save | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDXFDontShowMap) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDXFDontShowMap,
< OnFlag >) | Boolean value | Specifies whether dialog appears when saving drawing when swDxfMapping
set to True |
| Custom Map SOLIDWORKS to DXF/DWG - Map file | ISldWorks::GetUserPreferenceStringListValue (swUserPreferenceStringListValue_e.swDxfMappingFiles) ISldWorks::SetUserPreferenceStringListValue (swUserPreferenceStringListValue_e.swDxfMappingFiles,
< Value >) IMPORTANT : In addition to
specifying the custom map file, you must specify a custom map file index to
indicate which custom map file to use in the custom map file list. The following code snippet shows how to specify the custom map file index
when adding the first custom map file to the custom map file list: swApp.SetUserPreferenceStringListValue
swUserPreferenceStringListValue_e.swDxfMappingFiles, mapFilePath index =
swApp.GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDxfMappingFileIndex) If (index = -1)
Then swApp.SetUserPreferenceIntegerValue
swUserPreferenceIntegerValue_e.swDxfMappingFileIndex, 0 End If index =
swApp.GetUserPreferenceIntegerValue(swUserPreferenceIntegerValue_e.swDxfMappingFileIndex) result=
swModel.SaveAs4(outputPath, swSaveAsVersion_e.swSaveAsCurrentVersion,
swSaveAsOptions_e.swSaveAsOptions_Silent, errors, warnings) | String value | Sets up DXF/DWG mapping file; setting is persistent across SOLIDWORKS sessions; you can also interactively
get or set the custom map file setting by clicking File,
Save As, .dxf or .dwg as Save
as type, and Options ; separate
each string in the list by a line feed (e.g.,
the vbLf constant in Visual Basic) |
| Scale output 1:1 - Enable and Base scale | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDxfOutputNoScale) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDxfOutputNoScale,
< Value >) | 0 = not enabled 1 = 1:1 scale | Enabled for drawings only; no options currently available to either
differentiate between sheet scale and view scale or specify a scale factor |
| Scale output 1:1 - Warn me if enabled | See Comment | See Comment | Not currently available in SOLIDWORKS API |
| End Point Merging - Enable Merging | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDxfEndPointMerge) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDxfEndPointMerge,
< OnFlag >) | Boolean value | Specifies whether to merge the end points of entities when exporting
a part to
a DXF/DWG file; this option helps to avoid gaps between model edges, but
it increases the export time; it is off by default |
| End Point Merging - < n > | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swDxfMergingDistance) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swDxfMergingDistance,
< Value >) | Double value | Specifies the tolerance within which gaps between line endpoints are
eliminated |
| End Point Merging - High quality DWG export | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDXFHighQualityExport) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDXFHighQualityExport,
< OnFlag >) | Boolean value | Only for End Point Merging - Enable
Merging set to True; specifies whether to export at a higher level
of quality (with a possible increase in time to export) |
| Spline export options - Export all splines as splines | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDxfExportSplinesAsSplines) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDxfExportSplinesAsSplines,
< OnFlag >) | True | Specifies to export all splines as splines |
| Spline export options - Export all splines as polylines | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDxfExportSplinesAsSplines) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDxfExportSplinesAsSplines,
< OnFlag >) | False | Specifies to export all splines as polylines |
| View export options - Export views as blocks | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDxfExportViewAsBlock) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDxfExportViewAsBlock,
< OnFlag >) | Boolean value | Exports the geometry in the views as blocks |
| Multiple sheet drawing - Export active sheet only | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDxfMultiSheetOption) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDxfMultiSheetOption,
swDxfMultiSheet_e.swDxfActiveSheetOnly) | swDxfMultiSheet_e.swDxfActiveSheetOnly | See swDxfMultiSheet_e for all valid options |
| Multiple sheet drawing - Export all sheets to separate files | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDxfMultiSheetOption) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDxfMultiSheetOption,
swDxfMultiSheet_e.swDxfSeparateSheets) | swDxfMultiSheet_e.swDxfSeparateSheets | See swDxfMultiSheet_e for all valid options |
| Multiple sheet drawing - Export all sheets to one file | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDxfMultiSheetOption) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDxfMultiSheetOption,
swDxfMultiSheet_e.swDxfMultiSheet) | swDxfMultiSheet_e.swDxfMultiSheet | See swDxfMultiSheet_e for all valid options |
| Multiple sheet drawing - Export all
drawing sheets to paper space | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDxfExportAllSheetsToPaperSpace) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDxfExportAllSheetsToPaperSpace,
< OnFlag >) | Boolean | Specifies to export all sheets to
paper space |

Hidden Layers Enumerators

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Do you want to export entities on all layers? <Yes/No> | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDXFExportHiddenLayersOn) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDXFExportHiddenLayersOn,
< OnFlag >) | Boolean value | Specifies whether to export layers that are hidden in the drawing |
| Do not ask again | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDXFExportHiddenLayersWarnIsOn) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDXFExportHiddenLayersWarnIsOn,
< OnFlag >) | Boolean value | Specifies whether to dismiss the hidden layers warning dialog on
export; restore the dismissed dialog in System Options > Advanced |

Miscellaneous Enumerators

(Table)=========================================================

| Enumerator | Get/Set Methods | Return Value or < OnFlag > | Comment |
| --- | --- | --- | --- |
| swDxfMappingFileIndex | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDxfMappingFileIndex) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDxfMappingFileIndex,
< Value >) IMPORTANT : In addition to specifying the
custom map file, you must specify a custom map file index to indicate which
custom map file to use in the custom map file list. The following code snippet shows how to specify the custom map file index
when adding the first custom map file to the custom map file list: swApp.SetUserPreferenceStringListValue _ swDxfMappingFiles, mapFilePath index =
swApp.GetUserPreferenceIntegerValue _ swDxfMappingFileIndex) If (index = -1)
Then swApp.SetUserPreferenceIntegerValue _ swDxfMappingFileIndex, 0 End If result=
swModel.SaveAs4(outputPath,_ swSaveAsCurrentVersion, _ swSaveAsOptions_Silent, errors, warnings) | Integer value | Specifies a custom map file
index to indicate which custom map file to use in the custom map file list; index into list of custom map files or -1 |
| swDxfUseSolidworksLayers | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDxfUseSolidworksLayers) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDxfUseSolidworksLayers,
< OnFlag >) | Boolean value | Specifies whether to apply the mapping file settings only to those entities
whose layers are not defined and to preserve existing SOLIDWORKS drawing
file layers in the exported file or to have the mapping file definitions
overwrite all of the current SOLIDWORKS drawing file layers; this enumerator
is equivalent to the Keep existing SOLIDWORKS
drawing layer for entities option in the SOLIDWORKS to DXF/DWG
Mapping dialog |

Obsolete Enumerators

(Table)=========================================================

| Enumerator | Get/Set Method | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swDxfOutputScaleFactor | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swDxfOutputScaleFactor) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swDxfOutputScaleFactor,
< Value >) | Double value | Specifies value to scale DXF output |
