---
title: "Document Properties > Tables > Revision"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_Tables-Revision.htm"
---

# Document Properties > Tables > Revision

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Border - Box Border | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingRevisionTableBorderLineWeight, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingRevisionTableBorderLineWeight, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options |  |
| Border - Grid Border | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingRevisionTableGridLineWeight, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingRevisionTableGridLineWeight, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options |  |
| Text - Font... | IModelDocExtension::GetUserPreferenceTextFormat (swUserPreferenceTextFormat_e.swDetailingRevisionTableTextFormat, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceTextFormat (swUserPreferenceTextFormat_e.swDetailingRevisionTableTextFormat, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | See ITextFormat for font options | To set font property values, implement ITextFormat, set the appropriate ITextFormat member values, and pass the ITextFormat object in the API set method |
| Symbol shapes | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swRevisionTableSymbolShape, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swRevisionTableSymbolShape, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swRevisionTableSymbolShape_e.< Value >) | See swRevisionTableSymbolShape_e for valid options |  |
| Alpha/numerical control | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swRevisionTableTagStyle, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swRevisionTableTagStyle, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swRevisionTableTagStyle_e.< Value >) | See swRevisionTableTagStyle_e for valid options |  |
| Alpha/numerical control - Start from where user left or Change all | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swRevisionTableUpdateAllLabels, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swRevisionTableUpdateAllLabels, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value: True to apply format of all revisions, previous and future False to apply format only to revisions from now on |  |
| Multiple sheet style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swRevisionTableMultipleSheetStyle, swUserPreferenceOption_e.swDetailingRevisionTable) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swRevisionTableMultipleSheetStyle, swUserPreferenceOption_e.swDetailingRevisionTable, swRevisionTableMultipleSheetStyle_e.< Value >) | See swRevisionTableMultipleSheetStyle_e for valid options |  |
| Layer | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swDetailingLayer, swUserPreferenceOption_e.swDetailingRevisionTable) IModelDocExtension::SetUserPreferenceString (swUserPreferenceStringValue_e.swDetailingLayer, swUserPreferenceOption_e.swDetailingRevisionTable, < Value >) | Valid options: "Border" "Dimensions" "Notes" "BOM" "FORMAT" "None" | This setting is available only on drawings; depending on drawing, some options may not apply |
