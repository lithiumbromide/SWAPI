---
title: "Route Properties PropertyManager"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/Routing-RouteProperties.htm"
---

# Route Properties PropertyManager

|  |  |  |  |
| --- | --- | --- | --- |

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Cable Tray - component path and file name | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swElecCableTrayDuctName, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceString ( swUserPreferenceStringValue_e. swElecCableTrayDuctName , swUserPreferenceOption_e.swDetailingNoOptionSpecified, <Value> ) | String value | See SOLIDWORKS Routing Help for details about the electrical cable tray sub-route type |
| Bends - Elbows - component path and file name for Cable Tray | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swElecCableTrayElbowName, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceString ( swUserPreferenceStringValue_e.swElecCableTrayElbowName , swUserPreferenceOption_e.swDetailingNoOptionSpecified, <Value> ) | String value | See SOLIDWORKS Routing Help for details about the electrical cable tray sub-route type |
| Ducting/Trunking - component path and file name | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swElecDuctingDuctName, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceString ( swUserPreferenceStringValue_e.swElecDuctingDuctName , swUserPreferenceOption_e.swDetailingNoOptionSpecified, <Value> ) | String value | See SOLIDWORKS Routing Help for details about the electrical ducting/trunking sub-route type |
| Bends - Elbows - component path and file name for Ducting/Trunking | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swElecDuctingElbowName, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceString ( swUserPreferenceStringValue_e.swElecDuctingElbowName , swUserPreferenceOption_e.swDetailingNoOptionSpecified, <Value> ) | String value | See SOLIDWORKS Routing Help for details about the electrical ducting/trunking sub-route type |
| Circular - component path and file name | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swHvacCirDuctName, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceString ( swUserPreferenceStringValue_e.swHvacCirDuctName , swUserPreferenceOption_e.swDetailingNoOptionSpecified, <Value> ) | String value | See SOLIDWORKS Routing Help for details about the user-defined circular cross-section sub-route type |
| Bends - Elbows - component path and file name for Circular | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swHvacCirElbowName, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceString ( swUserPreferenceStringValue_e.swHvacCirElbowName , swUserPreferenceOption_e.swDetailingNoOptionSpecified, <Value> ) | String value | See SOLIDWORKS Routing Help for details about the user-defined circular cross-section sub-route type |
| HVAC Ducting - component path and file name | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swHvacRectDuctName, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceString ( swUserPreferenceStringValue_e.swHvacRectDuctName , swUserPreferenceOption_e.swDetailingNoOptionSpecified, <Value> ) | String value | See SOLIDWORKS Routing Help for details about the user-defined rectangular cross-section sub-route type |
| Bends - Elbows - component path and file name for HVAC Ducting | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swHvacRectElbowName, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceString ( swUserPreferenceStringValue_e.swHvacRectElbowName , swUserPreferenceOption_e.swDetailingNoOptionSpecified, <Value> ) | String value | See SOLIDWORKS Routing Help for details about the user-defined rectangular cross-section sub-route type |
