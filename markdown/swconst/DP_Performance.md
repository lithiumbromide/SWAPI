---
title: "Document Properties > Performance"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_Performance.htm"
---

# Document Properties > Performance

The Performance tab appears only when a drawing is open.

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Detailing mode - Save model data | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingModeSaveModelData, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingModeSaveModelData, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < OnFlag >) | Boolean value | Valid only for drawings |
| Detailing mode - Include standard views in View Palette | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingModeIncludeStandardViewsInViewPalette, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingModeIncludeStandardViewsInViewPalette, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < OnFlag >) | Boolean value | Valid only for drawings and when Save model data is set to true |
