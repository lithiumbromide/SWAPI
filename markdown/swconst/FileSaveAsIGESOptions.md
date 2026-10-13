---
title: "System Options > Export > IGES 5.3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileSaveAsIGESOptions.htm"
---

# System Options > Export > IGES 5.3

This topic contains two tables. The information in the table:

- appearing immediately after the screen capture corresponds to the settings on that dialog.
- titled [Obsolete Enumerators](#Obsolete) contains enumerators that previously appeared on the dialog but are now obsolete.

To display the dialog:

Click **Tools > Options > System Options > Export > IGES 5.3** in **File Format**.

- or -

1. Click **File > Save As**.
2. In **Save as type**, select **IGES**.
3. Click **Options**.

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Solid/Surface features - Output as - IGES solid/surface entities | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swIGESExportSolidAndSurface) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swIGESExportSolidAndSurface, < OnFlag >) | Boolean value | Specifies whether to export data as solid or surface entities |
| Solid/Surface features - Output as - IGES solid/surface entities < value > | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swIGESRepresentation) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swIGESRepresentation, swIGESRepresentation_e.< Value >) | See swIGESRepresentation_e for valid options | Specifies IGES representation type |
| Solid/Surface features - Output as - IGES wireframe (3D curves) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swIGESExportAsWireframe) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swIGESExportAsWireframe, < OnFlag >) | Boolean value | Specifies whether to convert solid body to a 3D wireframe representation in the IGES file |
| Solid/Surface features - Output as - IGES wireframe (3D curves) < value > | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swIGESCurveRepresentation) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swIGESCurveRepresentation, swIGESCurveRepresentation_e.< Value >) | See swIGESCurveRepresentation_e for valid options | Specifies the IGES curve representation |
| Solid/Surface features - Surface representation/System preference | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swIGESSystem) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swIGESSystem, swIGESPreferredSystem_e.< Value >) | See swIGESPreferredSystem_e for valid options | Specifies the IGES system setting |
| Export 3D Curve features | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swIGESExportFreeCurves) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swIGESExportFreeCurves, < OnFlag >) | Boolean value | Specifies whether to include 3D curve features in the exported file |
| Export sketch entities | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swIGESExportSketchEntities) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swIGESExportSketchEntities, < OnFlag >) | Boolean value | Specifies whether to export sketch entities |
| Use high trim curve accuracy | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swIGESHighTrimCurveAccuracy) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swIGESHighTrimCurveAccuracy, < OnFlag >) | Boolean value | Specifies whether to use high-trim curve accuracy |
| IGES assembly structure - Save all components of an assembly in one file | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swIGESComponentsIntoOneFile) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swIGESComponentsIntoOneFile, < OnFlag >) | Boolean value | Specifies whether to save all assembly components, sub-assemblies, and sub-assembly components in one file; for assemblies only |
| IGES assembly structure - Flatten assembly hierarchy | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swIGESFlattenAssemHierarchy) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swIGESFlattenAssemHierarchy, < OnFlag >) | Boolean value | Specifies whether to save assembly in flattened hierarchy (one level); for assemblies only |
| Split periodic faces | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swIGESExportSplitPeriodic) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swIGESExportSplitPeriodic, < OnFlag >) | Boolean value | Specifies whether to split periodic faces; for parts only |
| Output coordinate system | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swExportOutputCoordinateSystem) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swExportOutputCoordinateSystem, < Value >) | String value |  |

Obsolete Enumerators

| Enumerator | Comment |
| --- | --- |
| swIGESDuplicateEntities | Obsolete |
| swIGESNurbsSetting | Obsolete ; see swUserPreferenceIntegerValue_e.swIGESSystem |
| swIGESStandardSetting | Obsolete ; see swUserPreferenceIntegerValue_e.swIGESSystem |
| swFileSaveAsCoordinateSystem | Obsolete |
