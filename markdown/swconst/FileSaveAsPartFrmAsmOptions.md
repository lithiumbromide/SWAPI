---
title: "System Options > Export > SLDPRT from assembly"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileSaveAsPartFrmAsmOptions.htm"
---

# System Options > Export > SLDPRT from assembly

To display the dialog:

Click **Tools > Options > System Options > Export > SLDPRT from assembly** in **File Format**.

- or -

1. Click **File > Save As**.
2. In **Save as type**, select **Part (*.prt, *.sldprt)**.
3. Click **Options**.

| Setting | Get/Set Methods | Return Value or <Value> or < O nFlag > | Comment |
| --- | --- | --- | --- |
| Specified components - Remove - Visibility threshold (internal components) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swASMSLDPRT_ExcludeComponentsByVisibility) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swASMSLDPRT_ExcludeComponentsByVisibility, <OnFlag> ) | Boolean value | Specifies whether to remove from the export list those internal components whose visibility is less than the threshold specified by swASMSLDPRT_ExcludeComponentsByVisibilityThreshold |
| Specified components - Remove - Visibility threshold (internal components) - (slider amount) | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swASMSLDPRT_ExcludeComponentsByVisibilityThreshold) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swASMSLDPRT_ExcludeComponentsByVisibilityThreshold, < Value >) | Double value in meters-cubed | Valid only if swASMSLDPRT_ExcludeComponentsByVisibility is set to true |
| Specified components - Remove - Bounding box volume less than: | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swExcludeComponentsByBBoxVolume) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swExcludeComponentsByBBoxVolume, <OnFlag> ) | Boolean value | Specifies whether to remove from the export list those components whose bounding box volumes are less than the threshold specified by swASMSLDPRT_ExcludeComponentsByBBoxVolumeThreshold |
| Specified components - Remove - Bounding box volume less than: (amount) | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swASMSLDPRT_ExcludeComponentsByBBoxVolumeThreshold) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swASMSLDPRT_ExcludeComponentsByBBoxVolumeThreshold, < Value >) | Double value in meters-cubed | Valid only if swExcludeComponentsByBBoxVolume is set to true |
| Specified components - Remove - Fastener components | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swASMSLDPRT_ExcludeIfToolboxComponents) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swASMSLDPRT_ExcludeIfToolboxComponents, <OnFlag> ) | Boolean value | Specifies whether to remove from the export list fastener components |
| Specified components - Include - Mass properties | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swASMSLDPRT_IncludeMassProperties) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swASMSLDPRT_IncludeMassProperties, <OnFlag> ) | Boolean value | Specifies whether to override the mass properties of the part with the mass properties from the assembly |
| Output coordinate system | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swExportOutputCoordinateSystem) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swExportOutputCoordinateSystem, < Value >) | String value |  |
