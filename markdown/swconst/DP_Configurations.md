---
title: "Document Properties > Configurations"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_Configurations.htm"
---

# Document Properties > Configurations

HTML PUBLIC "-//W3C//DTD HTML 4.0 Frameset//EN"

(==============================================================)

Configurations settings are not supported in SOLIDWORKS Connected.

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Add Rebuild/Save mark to new configurations (Not supported in SOLIDWORKS
Connected) | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swRebuildSaveNewConfig,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swRebuildSaveNewConfig,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to apply the Rebuild/Save mark to new configurations. |
| Add Display Data Mark to new configurations (Not supported in SOLIDWORKS
Connected) | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayDataMarkNewConfig,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayDataMarkNewConfig,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value |  |
| Default Bill Of Materials part number for new configurations | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDefaultBOMPartNumberForNewConfig,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDefaultBOMPartNumberForNewConfig,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swDefaultBOMPartNumberSource_e. < Value > ) | swDefaultBOMPartNumberSource_e .swDefaultBOMPartNumberSource_DocumentName -
or - swDefaultBOMPartNumberSource_e.swDefaultBOMPartNumberSource_ConfigurationName |  |
