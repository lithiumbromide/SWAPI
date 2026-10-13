---
title: "View > Modify > Filter Modified Components"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/ViewModifyQuickViewTransparency.htm"
---

# View > Modify > Filter Modified Components

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Transparency level - Enable | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swQuickViewTransparencyEnabled) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swQuickViewTransparencyEnabled, < OnFlag>) | Boolean value | Specifies whether to activate the transparency for unmodified components of assemblies opened in Large Design Review |
| Transparency level - Dynamic | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swQuickViewTransparencyDynamic) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swQuickViewTransparencyDynamic, < OnFlag>) | Boolean value | Specifies whether to update the transparency level in the graphics area when the slider is moved in the Transparency Level PropertyManager page |
| Transparency level - Level ranges from 0 to 1 | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swQuickViewTransparencyLevel) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swQuickViewTransparencyLevel, < Value >) | Double value | Specifies the value to which to adjust the transparency for unmodified components in assemblies opened in Large Design Review |
