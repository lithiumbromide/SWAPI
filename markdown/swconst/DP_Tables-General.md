---
title: "Document Properties > Tables > General"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_Tables-General.htm"
---

# Document Properties > Tables > General

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Border - Box Border | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingGeneralTableBorderLineWeight, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingGeneralTableBorderLineWeight, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options |  |
| Border - Grid Border | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingGeneralTableGridLineWeight, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingGeneralTableGridLineWeight, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options |  |
| Text - Font... | IModelDocExtension::GetUserPreferenceTextFormat (swUserPreferenceTextFormat_e.swDetailingGeneralTableTextFormat, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceTextFormat (swUserPreferenceTextFormat_e.swDetailingGeneralTableTextFormat, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | See ITextFormat for font options | To set font property values, implement ITextFormat, set the appropriate ITextFormat member values, and pass the ITextFormat object in the API set method |
| Leading zeroes | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingLeadingZero, swUserPreferenceOption_e.swDetailingGeneralTable) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingLeadingZero, swUserPreferenceOption_e.swDetailingGeneralTable, swDetailingLeadingZero_e.< Value >) | See swDetailingLeadingZero_e for valid options |  |
| Trailing zeroes | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingDimTrailingZero, swUserPreferenceOption_e.swDetailingGeneralTable) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingDimTrailingZero, swUserPreferenceOption_e.swDetailingGeneralTable, swDetailingDimTrailingZero_e.< Value >) | Valid options in swDetailingDimTrailingZero_e : swDimShowTrailingZeroes swDimRemoveTrailingZeroes swDimRemoveOnlyOnZero |  |
| Layer | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swDetailingLayer, swUserPreferenceOption_e.swDetailingGeneralTable) IModelDocExtension::SetUserPreferenceString (swUserPreferenceStringValue_e.swDetailingLayer, swUserPreferenceOption_e.swDetailingGeneralTable, < Value >) | Valid options: "Border" "Dimensions" "Notes" "BOM" "FORMAT" "None" | This setting is available only on drawings; depending on drawing, some options may not apply |
