---
title: "Document Properties > Tables > Title Block"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_Tables-TitleBlock.htm"
---

# Document Properties > Tables > Title Block

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Border - Box Border | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingTitleBlockTableBorderLineWeight, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingTitleBlockTableBorderLineWeight, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options | For assemblies and parts only. |
| Border - Grid Border | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingTitleBlockTableGridLineWeight, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingTitleBlockTableGridLineWeight, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options | For assemblies and parts only. |
| Text - Font... | IModelDocExtension::GetUserPreferenceTextFormat (swUserPreferenceTextFormat_e.swDetailingTitleBlockTableTextFormat, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceTextFormat (swUserPreferenceTextFormat_e.swDetailingTitleBlockTableTextFormat, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | See ITextFormat for font options | To set font property values, implement ITextFormat, set the appropriate ITextFormat member values, and pass the ITextFormat object in the API set method. For assemblies and parts only. |
