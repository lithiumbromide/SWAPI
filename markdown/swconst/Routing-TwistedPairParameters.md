---
title: "Twisted Pair Parameters"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/Routing-TwistedPairParameters.htm"
---

# Twisted Pair Parameters

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Twists per unit length - spin box | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swTwistCountValue, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger ( swUserPreferenceIntegerValue_e.swTwistCountValue , swUserPreferenceOption_e.swDetailingNoOptionSpecified, <Value> ) | Integer value | Specifies the number of twists per unit length that the wires require in an electrical route; see SOLIDWORKS Routing Help for details about twisted pairs |
| Twists per meter | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swTwistCountValuePerMeter, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble ( swUserPreferenceDoubleValue_e.swTwistCountValuePerMeter , swUserPreferenceOption_e.swDetailingNoOptionSpecified, <Value> ) | Double value For example: If s wTwistCountValue is... Desired unit is... Then swTwistCountValuePerMeter is... 10 per centimeter (cm) 1000 (1 m = 100 cm) per inch (inch) 393.7 (1 m = 39.37 in) per feet (ft) 32.8 (1 m = 3.28 ft) per meter (m) 10 | Specifies the number of twists per meter for the twisted pairs in an electrical route; see SOLIDWORKS Routing Help for details about twisted pairs |
| If s wTwistCountValue is... | Desired unit is... | Then swTwistCountValuePerMeter is... |  |
| 10 | per centimeter (cm) | 1000 (1 m = 100 cm) |  |
| per inch (inch) | 393.7 (1 m = 39.37 in) |  |  |
| per feet (ft) | 32.8 (1 m = 3.28 ft) |  |  |
| per meter (m) | 10 |  |  |
