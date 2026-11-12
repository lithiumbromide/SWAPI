---
title: "File > Open > Files of type > SLDXML > Options"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileOpenOptionsSLDXML.htm"
---

# File > Open > Files of type > SLDXML > Options

| Setting | Get/Set Methods | Return Value or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Import sketch data | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportSLDXMLImportSketchData) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportSLDXMLImportSketchData, < OnFlag >) | Boolean value | Specifies whether to import sketch data |
| Import sketch objects in a mechanism sketch as blocks | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportSLDXMLImportMechanismSketchObjectsAsBlocks) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportSLDXMLImportMechanismSketchObjectsAsBlocks, < OnFlag >) | Boolean value | Specifies whether to import sketch objects in a mechanism sketch as blocks; swImportSLDXMLImportSketchData must be true for this option to be applicable |
| Import assembly mates data | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportSLDXMLImportAssemblyMatesData) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportSLDXMLImportAssemblyMatesData, < OnFlag >) | Boolean value | Specifies whether to import assembly mates data |
