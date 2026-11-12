---
title: "System Options > Export > AMF"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileSaveAsAMFOptions.htm"
---

# System Options > Export > AMF

This topic contains two tables. The information in the table:

- appearing immediately after the dialog corresponds to the settings on that dialog.
- titled [Obsolete Enumerators](#Obsolete) contains enumerators that previously appeared on the dialog but are now obsolete.

To display the dialog:

Click **Tools > Options > System Options > Export > AMF** in **File Format**.

- or -

1. Click **File > Save As**.
2. In **Save as type**, select **Additive Manufacturing File**.
3. Click **Options**.

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Output as - Compress file | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e, swAMFCompression) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e, swAMFCompression, < OnFlag >) | Boolean value | Specifies whether to compress the output file |
| Output as - Unit | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swExportStlUnits) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swExportStlUnits, swLengthUnit_e.< Value >) | Valid options as defined in swLengthUnit_e : 0 = swMM (millimeters) 1 = swCM (centimeters) 2 = swMETER 3 = swINCHES 4 = swFEET |  |
| Resolution - Coarse Fine Custom | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSTLQuality) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSTLQuality, swSTLQuality_e.< Value >) | See swSTLQuality_e for valid options | Specifies the resolution of the output for additive manufacturing files |
| Resolution - Deviation - Tolerance | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swSTLDeviation) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swSTLDeviation, < Value >) | Double value | Specifies the deviation tolerance, which controls whole-part tessellation; lower numbers generate files with greater whole-part accuracy |
| Resolution - Angle - Tolerance | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swSTLAngleTolerance) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swSTLAngleTolerance, < Value >) | Double value | Specifies the angle tolerance, which controls smaller detail tessellation; lower numbers generate files with greater small-detail accuracy, but those files take longer to generate |
| Resolution - Preview before saving file | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e, swSTLPreview) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e, swSTLPreview, < OnFlag >) | Boolean value | Specifies whether a faceted model preview is displayed in the graphics area |
| Include materials | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e, swAMFMaterials) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e, swAMFMaterials, < OnFlag >) | Boolean value | Specifies whether to include materials |
| Include colors | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e, swAMFColors) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e, swAMFColors, < OnFlag >) | Boolean value | Specifies whether to include colors |
| Output coordinate system | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swExportOutputCoordinateSystem) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swExportOutputCoordinateSystem, < Value >) | String value |  |

Obsolete Enumerators

| Enumerator | Comment |
| --- | --- |
| swFileSaveAsCoordinateSystem | Obsolete |
