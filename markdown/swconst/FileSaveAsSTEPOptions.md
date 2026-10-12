---
title: "System Options > Export > STEP"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileSaveAsSTEPOptions.htm"
---

# System Options > Export > STEP

This topic contains two tables. The information in the table:

- appearing immediately after the screen capture corresponds to the settings on that dialog.
- titled [Miscellaneous Enumerators](#Miscellaneous) contains enumerators related to saving STEP data.
- titled [Obsolete Enumerators](#Obsolete) contains enumerators that previously appeared on the dialog but are now obsolete.

To display the dialog:

Click **Tools > Options > System Options > Export > STEP** in **File Format**.

- or -

1. Click **File > Save As**.
2. In **Save as type**, select **STEP AP203** or **STEP AP214**.
3. Click **Options**.

| Setting | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| Output as - Solid/Surface geometry | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swStepExportPreference) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swStepExportPreference, swAcisOutputGeometryPreference_e.swAcisOutputAsSolidAndSurface) | swAcisOutputGeometryPreference_e.swAcisOutputAsSolidAndSurface |  |
| Output as - Wireframe | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swStepExportPreference) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swStepExportPreference, swAcisOutputGeometryPreference_e.swAcisOutputAs3DCurves) | swAcisOutputGeometryPreference_e.swAcisOutputAs3DCurves |  |
| Output as - Wireframe - Export sketch entities | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swStepExportPreference) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swStepExportPreference, swAcisOutputGeometryPreference_e.swAcisOutputAs3DCurves_IncludeSketchEnts) | swAcisOutputGeometryPreference_e.swAcisOutputAs3DCurves_IncludeSketchEnts |  |
| Set STEP configuration data | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swStepExportConfigurationData, swUserPreferenceOption_e.swDetailingNoOptionSpecified) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swStepExportConfigurationData, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to export STEP configuration data |
| Export face/edge properties | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swStepExportFaceEdgeProps) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swStepExportFaceEdgeProps, < OnFlag >) | Boolean value | Specifies whether to export face and edge properties |
| Export appearances | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swStepExportAppearances) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swStepExportAppearances, < OnFlag >) | Boolean value |  |
| Split periodic faces | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swStepExportSplitPeriodic) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swStepExportSplitPeriodic, < OnFlag >) | Boolean value | Specifies whether to split periodic faces on export |
| Export 3D Curve features | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swStepExport3DCurveFeatures) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swStepExport3DCurveFeatures, < OnFlag >) | Boolean value | Specifies whether to include 3D curve features in the exported file |
| Export assembly components as separate STEP files (recommended for large assemblies) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swStepExportAtomicSave) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swStepExportAtomicSave, < OnFlag >) | Boolean value |  |
| Output coordinate system | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swExportOutputCoordinateSystem) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swExportOutputCoordinateSystem, < Value >) | String value |  |

Miscellaneous Enumerators

| Enumerator | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swStepAP | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swStepAP) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swStepAP, < Value >) | Integer value: 203 = STEP AP203 format 214 = STEP AP214 format | Specifies STEP version number for files saved as STEP |

Obsolete Enumerators

| Enumerator | Comment |
| --- | --- |
| swFileSaveAsCoordinateSystem | Obsolete |
