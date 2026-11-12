---
title: "System Options > Import > STEP/IGES/ACIS"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileOpenOptionsSTEPIGESACIS.htm"
---

# System Options > Import > STEP/IGES/ACIS

To display the dialog:

Select **Tools > Options > System Options > Import > File Format > STEP/IGES/ACIS**.

- or -

1. Select **File > Open**.
2. In **Files of type**, select **IGES**, **ACIS**, or **STEP AP203/214/242**.
3. Click **Options**.

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Entities to Import - Solids and Surfaces | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportNeutral_SolidandSurface) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportNeutral_SolidandSurface, < OnFlag >) | Boolean value |  |
| Entities to Import - Try forming solid(s) or Do not knit | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportNeutral_KnitOption) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportNeutral_KnitOption, swImportNeutralKnitOption_e.< Value >) | Integer value as defined in swImportNeutralKnitOption_e | Valid only if Entities to Import - Solids and Surfaces is set to true |
| Entities to Import - Free Curves and Points as Sketch | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportNeutral_FreeCurvesAndPoints) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportNeutral_FreeCurvesAndPoints, < OnFlag >) | Boolean value |  |
| Entities to Import - Reference Planes | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportNeutralReferencePlane) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportNeutralReferencePlane, < OnFlag >) | Boolean value |  |
| Entities to Import - User Define Attributes | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportNeutral_AttributesAndProperties) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportNeutral_AttributesAndProperties, < OnFlag >) | Boolean value |  |
| Options - Assembly Structure Mapping | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportNeutralAssemblyStructureMapping) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportNeutralAssemblyStructureMapping, swImportNeutralAssemblyStructureMapping_e.< Value >) | Integer value as defined in swImportNeutralAssemblyStructureMapping_e |  |
| Options - Automatically run Import Diagnostics (Healing) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportNeutralRunDiagnostics) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportNeutralRunDiagnostics, < OnFlag >) | Boolean value |  |
| Options - Create analytic faces (slower) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportNeutralAnalyticalConversion) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportNeutralAnalyticalConversion, < OnFlag >) | Boolean value |  |
| Options - Import STEP faceted components as graphic | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportAssemblyHybrid) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportAssemblyHybrid, < OnFlag >) | Boolean value |  |
| Options - Unit of Import | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportNeutralUnits) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportNeutralUnits, swImportNeutralUnits_e.< Value >) | Integer value as defined in swImportNeutralUnits_e |  |
