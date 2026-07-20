---
title: "System Options > Export > IFC"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileSaveAsIFCOptions.htm"
---

# System Options > Export > IFC

This topic contains two tables. The information in the table:

- appearing immediately after the dialog corresponds to the settings on that dialog.
- titled

  [Obsolete
  Enumerators](#Obsolete)

  contains enumerators that previously appeared on
  the dialog but are now obsolete.

To display the dialog:

Click**Tools > Options > System Options > Export > IFC**in**File
Format**.

- or -

1. Click

  File > Save As

  .
2. In

  Save as type

  , select

  IFC 2x3

  or

  IFC 4

  .
3. Click

  Options

  .

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Output as - OmniClass ™ | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swIFCOmniClassPreference) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swIFCOmniClassPreference,
< OnFlag >) | Boolean value |  |
| Output as - UniClass2 | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swIFCUniClass2Preference) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swIFCUniClass2Preference,
< OnFlag >) | Boolean value |  |
| Output as - Custom Properties | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swIFCCustomPropsPreference) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swIFCCustomPropsPreference,
< OnFlag >) | Boolean value |  |
| Output as - Material and Mass Properties | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swIFCMaterialsMassPropertiesPreference) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swIFCMaterialsMassPropertiesPreference,
< OnFlag >) | Boolean value |  |
| Output as - Units | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swExportIFCUnits) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swExportIFCUnits,
swLengthUnit_e.< Value >) | Any of the following swLengthUnit_e values: 0 = swMM (millimeters) 1 = swCM (centimeters) 2 = swMETER 3 = swINCHES 4 = swFEET |  |
| Output as - Use Property Set mapping file | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swIFCExportUsePropertySetMappingFile) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swIFCExportUsePropertySetMappingFile,
< OnFlag >) | Boolean value |  |
| Property Set mapping file | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swIFCExportPropertySetMappingFile) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swIFCExportPropertySetMappingFile,
< Value >) | String value | See example XML mapping file(s) in install_dir \lang\< language >\IFC XML structure: <CustomPropertiesPSETMapping> <Schema
Version="1.0"/> <PropertySet Name="Pset_DoorCommon"> <AppliesTo ElementType="IFCDOOR"/> <PropertyMapping SOLIDWORKS="Reference" IFC="Reference"
Type="IfcIdentifier"/> <PropertyMapping SOLIDWORKS="FireRating" IFC="FireRating"
Type="IfcLabel"/> <PropertyMapping SOLIDWORKS="NoiseRating" IFC="AcousticRating"
Type="IfcLabel"/> <PropertyMapping SOLIDWORKS="Security" IFC="SecurityRating"
Type="IfcLabel"/> <PropertyMapping SOLIDWORKS="External" IFC="IsExternal"
Type="IfcBoolean"/> <PropertyMapping SOLIDWORKS="Infiltration" IFC="Infiltration"
Type="IfcVolumetricFlowRateMeasure"/> <PropertyMapping SOLIDWORKS="ThermalTransmit" IFC="ThermalTransmittance"
Type="IfcThermalTransmittanceMeasure"/> <PropertyMapping SOLIDWORKS="Verglasungsflächenanteil"
IFC="GlazingAreaFraction" Type="IfcPositiveRatioMeasure"/> <PropertyMapping SOLIDWORKS="Accessible" IFC="HandicapAccessible"
Type="IfcBoolean"/> <PropertyMapping SOLIDWORKS="FireDoor" IFC="FireExit" Type="IfcBoolean"/> <PropertyMapping SOLIDWORKS="StarTrekDoor" IFC="SelfClosing"
Type="IfcBoolean"/> <PropertyMapping SOLIDWORKS="SmokeStop" IFC="SmokeStop"
Type="IfcBoolean"/> </PropertySet> <PropertySet Name="ACME_CageCodes"> <AppliesTo ElementType="IFCDOOR"/> <AppliesTo
ElementType="IFCWINDOW"/> <PropertyMapping SOLIDWORKS="RefCode" IFC="CageCode" Type="IfcLabel"/> </PropertySet> </CustomPropertiesPSETMapping> |
| IFC4 Export - Save - BREP or Tessellation | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swIFCExportSaveType) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swIFCExportSaveType,
swIFCExportSaveType_e.< Value >) | swIFCExportSaveType_e .swIFCExportSaveType_BREP - or - swIFCExportSaveType_e.swIFCExportSaveType_Tessellation |  |
| Output coordinate system | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swExportOutputCoordinateSystem) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swExportOutputCoordinateSystem,
< Value >) | String value |  |

Obsolete Enumerators

(Table)=========================================================

| Enumerator | Comment |
| --- | --- |
| swIFCOmniUniClassPreference | Obsolete |
| swExportIFCUniClass2 | Obsolete |
| swExportIFCType | Obsolete |
