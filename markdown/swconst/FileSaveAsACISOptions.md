---
title: "System Options > Export > ACIS"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileSaveAsACISOptions.htm"
---

# System Options > Export > ACIS

To display the dialog:

Click **Tools > Options > System Options > Export > ACIS** in **File Format**.

- or -

1. Click **File > Save As**.
2. In **Save as type**, select **ACIS**.
3. Click **Options**.

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Output as - Solid/Surface geometry | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAcisOutputGeometryPreference) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAcisOutputGeometryPreference, swAcisOutputGeometryPreference_e.swAcisOutputAsSolidAndSurface) | swAcisOutputGeometryPreference_e.swAcisOutputAsSolidAndSurface |  |
| Output as - 3D curves | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAcisOutputGeometryPreference) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAcisOutputGeometryPreference, swAcisOutputGeometryPreference_e.swAcisOutputAs3DCurves) | swAcisOutputGeometryPreference_e.swAcisOutputAs3DCurves |  |
| Output as - Export sketch entities | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAcisOutputGeometryPreference) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAcisOutputGeometryPreference, swAcisOutputGeometryPreference_e.swAcisOutputAs3DCurves_IncludeSketchEnts) | swAcisOutputGeometryPreference_e.swAcisOutputAs3DCurves_IncludeSketchEnts |  |
| Output as - Version | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAcisOutputVersion) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAcisOutputVersion, swAcisOutputVersion_e.< Value >) | See swAcisOutputVersion_e for valid options |  |
| Output as - Unit | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAcisOutputUnits) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAcisOutputUnits, swLengthUnit_e.< Value >) | See swLengthUnit_e for valid options |  |
| Export face/edge properties | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSATExportFaceEdgeProps) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSATExportFaceEdgeProps, < OnFlag >) | Boolean value | Specifies whether to export face and edge properties |
| Split periodic faces | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSATExportSplitPeriodic) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSATExportSplitPeriodic, < OnFlag >) | Boolean value | Specifies whether to split periodic faces on export |
| Write multi body part into a single ACIS body | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSATExportMultLumpsToSingleBody) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSATExportMultLumpsToSingleBody, < OnFlag >) | Boolean value |  |
| Output coordinate system | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swExportOutputCoordinateSystem) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swExportOutputCoordinateSystem, < Value >) | String value |  |
