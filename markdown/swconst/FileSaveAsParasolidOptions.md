---
title: "System Options > Export > Parasolid"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileSaveAsParasolidOptions.htm"
---

# System Options > Export > Parasolid

This topic contains two tables. The information in the table:

- appearing immediately after the screen capture corresponds to the settings on that dialog.
- titled [Obsolete Enumerators](#Obsolete) contains enumerators that previously appeared on the dialog but are now obsolete.

To display the dialog:

Click **Tools > Options > System Options > Export > Parasolid** in **File Format**.

- or -

1. Click **File > Save As**.
2. In **Save as type**, select **Parasolid** or **Parasolid Binary**.
3. Click **Options**.

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Output as - Version | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swParasolidOutputVersion) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swParasolidOutputVersion, swParasolidOutputVersion_e.< Value >) | See swParasolidOutputVersion_e for valid options |  |
| Flatten assembly hierarchy | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swXTAssemSaveFormat) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swXTAssemSaveFormat, < OnFlag >) | Boolean value | Specifies whether to flatten assembly hierarchy in Parasolid output; for assemblies only |
| Output coordinate system | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swExportOutputCoordinateSystem) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swExportOutputCoordinateSystem, < Value >) | String value |  |

Obsolete Enumerators

| Enumerator | Comment |
| --- | --- |
| swFileSaveAsCoordinateSystem | Obsolete |
