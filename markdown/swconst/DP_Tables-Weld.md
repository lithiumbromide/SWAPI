---
title: "Document Properties > Tables > Weld"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_Tables-Weld.htm"
---

# Document Properties > Tables > Weld

**NOTE:** Setting any of the following weld table values means that new weld tables added to the drawing use these default values. However, a weld table that uses a template table for insertion might not use these default values because the template table contains certain properties that take precedence over these default values.

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Border - Box Border | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingWeldTableBorderLineWeight, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingWeldTableBorderLineWeight, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options |  |
| Border - Grid Border | ModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingWeldTableGridLineWeight, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingWeldTableGridLineWeight, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options |  |
| Text - Font... | IModelDocExtension::GetUserPreferenceTextFormat (swUserPreferenceTextFormat_e.swDetailingWeldSymbolTextFormat, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceTextFormat (swUserPreferenceTextFormat_e.swDetailingWeldSymbolTextFormat, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | See ITextFormat for font options | To set font property values, implement ITextFormat, set the appropriate ITextFormat member values, and pass the ITextFormat object in the set method |
| Trailing zeroes | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingDimTrailingZero, swUserPreferenceOption_e.swDetailingWeldTable) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingDimTrailingZero, swUserPreferenceOption_e.swDetailingWeldTable, swDetailingDimTrailingZero_e.< Value >) | Valid options in swDetailingDimTrailingZero_e : swDimShowTrailingZeroes swDimRemoveTrailingZeroes swDimRemoveOnlyOnZero swDimSameAsSource |  |
| Layer | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swDetailingLayer, swUserPreferenceOption_e.swDetailingWeldTable) IModelDocExtension::SetUserPreferenceString (swUserPreferenceStringValue_e.swDetailingLayer, swUserPreferenceOption_e.swDetailingWeldTable, < Value >) | Valid options: "Border" "Dimensions" "Notes" "BOM" "FORMAT" "None" | This setting is available only on drawings; depending on drawing, some options may not apply |
