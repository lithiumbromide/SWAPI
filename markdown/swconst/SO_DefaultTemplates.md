---
title: "System Options > Default Templates"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_DefaultTemplates.htm"
---

# System Options > Default Templates

| Setting | Get/Set Methods | Return Value or <Value> or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Parts | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swDefaultTemplatePart) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swDefaultTemplatePart, < Value >) | String value |  |
| Assemblies | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swDefaultTemplateAssembly) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swDefaultTemplateAssembly, < Value >) | String value |  |
| Drawings | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swDefaultTemplateDrawing) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swDefaultTemplateDrawing, < Value >) | String value |  |
| Always use these default document templates | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swAlwaysUseDefaultTemplates) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swAlwaysUseDefaultTemplates, < OnFlag >) | True | Specifies whether to use default template or prompt for name of template |
| Prompt user to select document template | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swAlwaysUseDefaultTemplates) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swAlwaysUseDefaultTemplates, < OnFlag >) | False | Specifies whether to prompt for name of template |
