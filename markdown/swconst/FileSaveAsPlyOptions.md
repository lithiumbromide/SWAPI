---
title: "System Options > Export > PLY"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileSaveAsPlyOptions.htm"
---

# System Options > Export > PLY

To display the dialog:

Click **Tools > Options > System Options > Export > PLY** in **File Format**.

- or -

1. Click **File > Save As**.
2. In **Save as type**, select **Polygon File Format**.
3. Click **Options**.

| Setting | Get/Set Methods | Return Value or <Value> or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Output as | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPLYBinaryFormat) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPLYBinaryFormat, < OnFlag >) | Boolean value |  |
| Output as - Unit | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e. swExportPlyUnits ) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e. swExportPlyUnits , swLengthUnit_e.< Value >) | Integer value as defined in swLengthUnit_e |  |
| Resolution | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e. swPLYQuality ) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e. swPLYQuality , swPLYQuality_e.< Value >) | Integer value as defined in swPLYQuality_e |  |
| Resolution - Deviation Tolerance | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swPLYDeviation) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swPLYDeviation, < Value >) | Double value in meters | Valid only if swPLYQuality is set to swPLYQuality_e.swPLYQuality_CUSTOM; the value range varies by part or assembly. Inspect the dialog for the range of values for the opened model. |
| Resolution - Angle Tolerance | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e. swPLYAngleTolerance ) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e. swPLYAngleTolerance , < Value >) | 0.5236 >= Double value in radians >= 0.00873 | Valid only if swPLYQuality is set to swPLYQuality_e.swPLYQuality_CUSTOM |
| Resolution - Preview before saving file | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPLYPreview) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPLYPreview, < OnFlag >) | Boolean value |  |
| Include colors | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPLYIncludeColors) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPLYIncludeColors, < OnFlag >) | Boolean value |  |
