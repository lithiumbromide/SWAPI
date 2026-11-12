---
title: "System Options > Import > General"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileOpenOptionsGeneral.htm"
---

# System Options > Import > General

This topic contains two tables. The information in the table:

- appearing immediately after the dialog corresponds to the settings on that dialog.
- titled [Obsolete Enumerators](#Obsolete) contains enumerators that previously appeared on the dialog but are now obsolete.

To display the dialog:

Select **Tools > Options > System Options > Import > File Format > General**.

- or -

1. Select **File > Open.**
2. In **Files of type**, select:

- Parasolid
- IGES
- STEP AP203/214/242
- IFC 2x3
- ACIS
- VDAFS
- Unigraphics/NX
- Inventor Part
- Inventor Assembly

1. Click Options.

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Enable 3D Interconnect | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swMultiCAD_Enable3DInterconnect) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swMultiCAD_Enable3DInterconnect, < OnFlag >) | Boolean value | Valid only if swUserPreferenceToggle_e.swImportSolidSurface is false |
| Create 3D Interconnect links | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swMultiCAD_3DInterconnectMaintainLinks) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swMultiCAD_3DInterconnectMaintainLinks, < OnFlag >) | Boolean value | Valid only if swUserPreferenceToggle_e.swMultiCAD_Enable3DInterconnect is true |
| Create 3D Interconnect links options | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swMultiCAD_3DInterconnectLinksFlag) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swMultiCAD_3DInterconnectLinksFlag, < OnFlag >) | False = Feature and component level (default) True = Feature level | Valid only if swUserPreferenceToggle_e.swMultiCAD_3DInterconnectMaintainLinks is true |
| When manually breaking 3D Interconnect links: | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swMultiCAD_3DInterconnectManualBreakLink) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swMultiCAD_3DInterconnectManualBreakLink, < OnFlag >) | False = Create external files (default) True = Create virtual components | Valid only if swUserPreferenceToggle_e.swMultiCAD_Enable3DInterconnect is true |
| Automatically run Import Diagnostics (Healing) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportAutoRunImportDiagnostics) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportAutoRunImportDiagnostics, < OnFlag >) and ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportAutoRunImportDiagnosticsPersist) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportAutoRunImportDiagnosticsPersist, < OnFlag >) | Boolean value and Boolean value | Specifies whether import diagnostics (healing) are run automatically. If TRUE, they are; if FALSE, they are not and Specifies whether users are presented with a dialog asking them if the import diagnostics (healing) should run; if True, then users are not asked and automatic healing is done depending on the value of swUserPreferenceToggle_e.swImportAutoRunImportDiagnostics; if False, then users are asked |
| Perform full entity check and repair errors | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportCheckAndRepair) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportCheckAndRepair, < Value >) | 0 = Do not check and repair 1 = Check and repair |  |
| Unit - File specified unit | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportUnitPreference) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportUnitPreference, swGeneralImportUnitsOptions_e.swGeneralImportFileSpecifiedUnit) | swGeneralImportUnitsOptions_e.swGeneralImportFileSpecifiedUnit | See swGeneralImportUnitsOptions_e for all valid options |
| Unit - Document template specified unit | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportUnitPreference) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportUnitPreference, swGeneralImportUnitsOptions_e.swGeneralImportDocumentTemplateSpecifiedUnit) | swGeneralImportUnitsOptions_e.swGeneralImportDocumentTemplateSpecifiedUnit) | See swGeneralImportUnitsOptions_e for all valid options |
| Import Queue location | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swMultiCAD_ImportQueuePath) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swMultiCAD_ImportQueuePath, < Value >) | String value |  |
| Solid and Surface | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportSolidSurface) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportSolidSurface, < OnFlag >) | Boolean value | Valid only if swUserPreferenceToggle_e.swMultiCAD_Enable3DInterconnect is false; specifies whether to import surface and solid entities; you must also set ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swCreateBodyFromSurfacesOption, swGeneralImportSurfaceSolidEntityOptions_e.< Value >) |
| Try forming solid(s) | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swCreateBodyFromSurfacesOption) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swCreateBodyFromSurfacesOption, swGeneralImportSurfaceSolidEntityOptions_e.swGeneralImportTryFormingSolids) | swGeneralImportSurfaceSolidEntityOptions_e.swGeneralImportTryFormingSolids | See swGeneralImportSurfaceSolidEntityOptions_e for all valid options |
| B-Rep mapping | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportUseBrep) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swCreateBodyFromSurfacesOption, swGeneralImportSurfaceSolidEntityOptions_e.swImportUseBrep) and ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swCreateBodyFromSurfacesOption) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swCreateBodyFromSurfacesOption, swGeneralImportSurfaceSolidEntityOptions_e.swGeneralImportByBrep) | 0 = Import the model by directly mapping topologies using BREP data 1 = Do not import the model by directly mapping topologies using BREP data NOTE : You must set ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swCreateBodyFromSurfacesOption, swGeneralImportSurfaceSolidEntityOptions_e.swGeneralImportByBrep) for swGeneralImportSurfaceSolidEntityOptions_e.swImportUseBrep to have an affect. and swGeneralImportSurfaceSolidEntityOptions_e.swGeneralImportByBrep | See swGeneralImportSurfaceSolidEntityOptions_e for all valid options |
| Knit surface(s) | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swCreateBodyFromSurfacesOption) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swCreateBodyFromSurfacesOption, swGeneralImportSurfaceSolidEntityOptions_e.swGeneralImportKnitSurfaces) | swGeneralImportSurfaceSolidEntityOptions_e.swGeneralImportKnitSurfaces | See swGeneralImportSurfaceSolidEntityOptions_e for all valid options |
| Do not knit | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swCreateBodyFromSurfacesOption) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swCreateBodyFromSurfacesOption, swGeneralImportSurfaceSolidEntityOptions_e.swGeneralImportDoNotKnit) | wGeneralImportSurfaceSolidEntityOptions_e.swGeneralImportDoNotKnit | See swGeneralImportSurfaceSolidEntityOptions_e for all valid options |
| Merge Entities | See Comment | See Comment | Not currently available in SOLIDWORKS API |
| Free Curves/points entities | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportFreeCurves) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportFreeCurves, < OnFlag >) | Boolean value | Valid only if swMultiCAD_Enable3DInterconnect is false; specifies whether to import free points and free curve entities; must also specify an ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportCurvePreference, swGeneralImportFreePointCurveEntityOptions_e.< Value >) |
| Import as sketch(es) | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportCurvePreference) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportCurvePreference, swGeneralImportFreePointCurveEntityOptions_e.swGeneralImportAsSketches) | swGeneralImportFreePointCurveEntityOptions_e.swGeneralImportAsSketches | See swGeneralImportFreePointCurveEntityOptions_e for all valid options |
| Import as 3D curves | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportCurvePreference) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportCurvePreference, swGeneralImportFreePointCurveEntityOptions_e.swGeneralImportAs3dCurves) | swGeneralImportFreePointCurveEntityOptions_e.swGeneralImportAs3dCurves | See swGeneralImportFreePointCurveEntityOptions_e for all valid options |
| Import multiple bodies as parts | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportMultBodyAsPartData) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportMultBodyAsPartData, < OnFlag >) | Boolean value | Valid only if swMultiCAD_Enable3DInterconnect is false; specifies whether to import multibody part as an assembly document; for STEP and ACIS files only |
| Customize curve tolerance | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swUseCustomizedImportTolerance) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swUseCustomizedImportTolerance, < Value >) | 0 = Do not use customized import tolerance 1 = Use customized import tolerance | Valid only if swMultiCAD_Enable3DInterconnect is false; specifies whether customized curve tolerance for imported documents is enabled |
| Customize curve tolerance < n > | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swCustomizedImportTolerance) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swCustomizedImportTolerance, < Value >) | Double value in meters | Specifies customized curve tolerance for imported documents; swUserPreferenceIntegerValue_e.swUseCustomizedImportTolerance must be set to 1 to enable this setting |
| IGES - Show IGES levels | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swIGESImportShowLevel) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swIGESImportShowLevel, < OnFlag >) | Boolean value | Valid only if swMultiCAD_Enable3DInterconnect is false; specifies whether to displays the IGES-In Surfaces, Curves, and Levels dialog to the user where the user can specify levels and values |
| STEP - Map configuration data | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportStepConfigData) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportStepConfigData, < OnFlag >) | Boolean value | Valid only if swMultiCAD_Enable3DInterconnect is false; specifies whether to import STEP file configuration data plus geometric data or geometric data only; for STEP files only |

Obsolete Enumerators

| Enumerator | Comment |
| --- | --- |
| swImportUGToolBodies | Obsolete |
| swMultiCAD_ApplyOnlyToParts | Obsolete |
| swMultiCAD_CreateNewComponentsAsExternalFiles | Obsolete |
| swForceEnableImportDiagnosis | Obsolete |
