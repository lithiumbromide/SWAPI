---
title: "System Options > Export > STL"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileSaveAsSTLOptions.htm"
---

# System Options > Export > STL

This topic contains two tables. The information in the table:

- appearing immediately after the dialog corresponds to the settings on that dialog.
- titled [Obsolete Enumerators](#Obsolete) contains enumerators that previously appeared on the dialog but are now obsolete.

To display the dialog:

Click **Tools > Options > System Options > Export > STL** in **File Format**.

- or -

1. Click **File > Save As**.
2. In **Save as type**, select **STL**.
3. Click **Options**.

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Output as - Binary | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSTLBinaryFormat) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSTLBinaryFormat, < OnFlag >) | True |  |
| Output as - ASCII | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSTLBinaryFormat) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSTLBinaryFormat, < OnFlag >) | False |  |
| Output as - Unit | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swExportStlUnits) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swExportStlUnits, swLengthUnit_e.< Value >) | Valid options as defined in swLengthUnit_e : 0 = swMM (millimeters) 1 = swCM (centimeters) 2 = swMETER 3 = swINCHES 4 = swFEET |  |
| Resolution - Coarse Fine Custom | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSTLQuality) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSTLQuality, swSTLQuality_e.< Value >) | See swSTLQuality_e for valid options | Specifies the resolution of the output for STL files |
| Resolution - Deviation - Tolerance | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swSTLDeviation) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swSTLDeviation, < Value >) | Double value | Specifies deviation tolerance, which controls whole-part tessellation; lower numbers generate files with greater whole-part accuracy |
| Resolution - Angle - Tolerance | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swSTLAngleTolerance) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swSTLAngleTolerance, < Value >) | Double value | Specifies angle tolerance, which controls smaller detail tessellation; lower numbers generate files with greater small-detail accuracy, but those files take longer to generate |
| Resolution - Show STL info before file saving | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSTLShowInfoOnSave) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSTLShowInfoOnSave, < OnFlag >) | Boolean value | Specifies whether to show STL information before saving the file |
| Resolution - Preview before saving file | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSTLPreview) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSTLPreview, < OnFlag >) | Boolean value | Specifies whether faceted model preview is displayed in the graphics area |
| Do not translate STL output data to positive space | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSTLDontTranslateToPositive) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSTLDontTranslateToPositive, < OnFlag >) | Boolean value | Specifies whether exported parts maintain original position in global space, relative to origin |
| Save all components of an assembly in a single file | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSTLComponentsIntoOneFile) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSTLComponentsIntoOneFile, < OnFlag >) | Boolean value | Specifies whether to save the assembly and its components to a single file |
| Check for interferences | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSTLCheckForInterference) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSTLCheckForInterference, < OnFlag >) | Boolean value | Specifies whether to check for interference prior to saving assembly document; swUserPreferenceToggle_e.swSTLComponentsIntoOneFile must be set to true |
| Output coordinate system | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swExportOutputCoordinateSystem) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swExportOutputCoordinateSystem, < Value >) | String value |  |

Obsolete Enumerators

| Enumerator | Comment |
| --- | --- |
| swFileSaveAsCoordinateSystem | Obsolete |
