---
title: "File > Save As"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileSaveAs.htm"
---

# File > Save As

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Save without Costing data | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSaveWithoutCostingData) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSaveWithoutCostingData, < OnFlag >) | Boolean value | Specifies whether to save the sheet metal part without any Costing data |
| Geometry to save: Exterior faces Exterior components All components | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSaveAssemblyAsPartOptions) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSaveAssemblyAsPartOptions, swSaveAsmAsPartOptions_e.< Value >) | See swSaveAsmAsPartOptions_e for valid options | Specifies the geometry of an assembly to save as a multi-body part |
| Preserve geometry references | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSaveAsmAsPartPreserveIDs) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSaveAsmAsPartPreserveIDs, < OnFlag >) | Boolean value | Specifies whether to preserve geometry reference IDs when saving an assembly as a part |
| Save as type - IFC 2x3 or IFC 4 | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSaveIFCFormat) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSaveIFCFormat, < Value >) | 23 = IFC 2x3 4 = IFC 4 | Specifies the IFC format in which to save a part |
