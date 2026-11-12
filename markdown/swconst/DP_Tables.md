---
title: "Document Properties > Tables"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_Tables.htm"
---

# Document Properties > Tables

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Text - Font... | IModelDocExtension::GetUserPreferenceTextFormat (swUserPreferenceTextFormat_e.swDetailingTableTextFormat, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceTextFormat (swUserPreferenceTextFormat_e.swDetailingTableTextFormat, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | See ITextFormat for font options | To set font property values, implement ITextFormat, set the appropriate ITextFormat member values, and pass the ITextFormat object in the API set method |
| Use template settings | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingTablesUseTemplateSettings, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingTablesUseTemplateSettings, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to override a table's document properties with the settings of an imported template |
| Cell paddings - Horizontal padding | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingTablesHorizontalPadding, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingTablesHorizontalPadding, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies the horizontal padding for table cells |
| Cell paddings - Vertical padding | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingTablesVerticalPadding, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingTablesVerticalPadding, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies the vertical padding for table cells |
