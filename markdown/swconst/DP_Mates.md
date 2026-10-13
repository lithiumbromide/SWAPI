---
title: "Document Properties > Mates"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_Mates.htm"
---

# Document Properties > Mates

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Misaligned mates - Maximum deviation | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swMatesMaximumDeviationForMisalignedMates, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e. swMatesMaximumDeviationForMisalignedMates , swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Valid only for assemblies |
| Misaligned mates - Default misalignment | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swMatesDefaultMisalignedType, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e. swMatesDefaultMisalignedType , swUserPreferenceOption_e.swDetailingNoOptionSpecified, swMatesDefaultMisalignment_e.< Value >) | Valid values as defined in swMatesDefaultMisalignment_e | Valid only for assemblies |
