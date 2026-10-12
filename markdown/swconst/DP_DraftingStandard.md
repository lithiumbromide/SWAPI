---
title: "Document Properties > Drafting Standard"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_DraftingStandard.htm"
---

# Document Properties > Drafting Standard

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comments |
| --- | --- | --- | --- |
| Overall drafting standard | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingDimensionStandard, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingDimensionStandard, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swDetailingStandard_e. < Value > ) | See swDetailingStandard_e for valid options | Specifies the base drafting standard to use |
| Uppercase - All uppercase for notes | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDraftingStandardUppercase, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDraftingStandardUppercase, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < OnFlag >) | Boolean value | Specifies whether to set the drafting standard to all uppercase for notes |
| Uppercase - All uppercase for tables | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDraftingStandardAllUppercaseForTable, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDraftingStandardAllUppercaseForTable, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < OnFlag >) | Boolean value | Specifies whether to set the drafting standard to all uppercase for tables |
| Uppercase - All uppercase for dimensions and hole callouts | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDraftingStandardAllUppercaseForDimensionsAndHoleCallouts, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDraftingStandardAllUppercaseForDimensionsAndHoleCallouts, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < OnFlag >) | Boolean value |  |
| Uppercase - Exclusion list | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swDraftStandardExclusionList, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceString (swUserPreferenceStringValue_e.swDraftStandardExclusionList, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | String value | Specifies the list of strings to exclude from making uppercase |
