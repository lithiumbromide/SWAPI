---
title: "Document Properties > DimXpert"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_DraftingDimXPert.htm"
---

# Document Properties > DimXpert

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Chamfer dimension scheme | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingDimXpertChamferScheme, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingDimXpertChamferScheme, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swDetailingDimXpertChamferStyle_e.< Value >) | See swDetailingDimXpertChamferStyle_e for valid options | Specifies chamfer dimension scheme |
| Slot dimension scheme | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingDimXpertSlotScheme, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingDimXpertSlotScheme, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swDetailingDimXpertSlotStyle_e.< Value >) | See swDetailingDimXpertSlotStyle_e for valid options | Specifies slot dimension scheme |
| Fillet options | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingDimXpertFilletOptions, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingDimXpertFilletOptions, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swDetailingDimXpertFilletInstanceStyle_e.< Value >) | See swDetailingDimXpertFilletInstanceStyle_e for valid options | Specifies fillet options |
| Chamfer options | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingDimXpertChamferOptions, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingDimXpertChamferOptions, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swDetailingDimXpertChamferInstanceStyle_e.< Value >) | See swDetailingDimXpertChamferInstanceStyle_e for valid options | Specifies chamfer options |
