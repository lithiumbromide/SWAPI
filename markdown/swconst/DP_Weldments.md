---
title: "Document Properties > Weldments"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_Weldments.htm"
---

# Document Properties > Weldments

## Document Properties >Weldments

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < Value >
or < OnFlag > | Comments |
| --- | --- | --- | --- |
| Cut list options - Automatically create cut lists | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swWeldmentEnableAutomaticCutList) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swWeldmentEnableAutomaticCutList,
< OnFlag >) | Boolean value | Specifies whether to automatically create cut lists |
| Cut list options - Automatically update cut lists (may
affect performance with many bodies) | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swWeldmentEnableAutomaticUpdate) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swWeldmentEnableAutomaticUpdate,
< OnFlag >) | Boolean value | Specifies whether to automatically
update cut lists |
| Cut list options - Rename cut list folders with
Description property value | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swWeldmentRenameCutlistDescriptionPropertyValue) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swWeldmentRenameCutlistDescriptionPropertyValue,
< OnFlag >) | Boolean value | Specifies whether to automatically
rename cut list folders using the Description property value |
| Cut list options - Collect identical bodies | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swWeldmentCollectIdenticalBodies) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swWeldmentCollectIdenticalBodies,
< OnFlag >) | Boolean value | Specifies whether to collect identical bodies |
| Cut list options - Use English Description property name in Weldment Cut
list | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swWeldmentUseEnglishDescriptionNameInCutlist) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swWeldmentUseEnglishDescriptionNameInCutlist,
< OnFlag >) | Boolean value |  |
| Weldment options -
Create derived configurations | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisableDerivedConfigurations) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisableDerivedConfigurations,
< OnFlag >) | Boolean value | Specifies whether to create derived
configurations; affects newly added configurations only |
| Weldment options -
Assign configuration Description
strings | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisableWeldmentConfigStrings) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisableWeldmentConfigStrings,
< OnFlag >) | Boolean value | Specifies whether to assign
configuration Description strings; swDisableDerivedConfigurations must be true for this
setting to be applicable |
| Bounding Box Properties - Solid Bodies Description - Prefix | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swSolidBodiesBBoxDescriptionPrefix,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceString (swUserPreferenceStringValue_e. swSolidBodiesBBoxDescriptionPrefix ,
swUserPreferenceOption_e.swDetailingNoOptionSpecified,
< Value >) | String value | Valid only if Solid Bodies Description - Use default description is set to true |
| Bounding Box Properties - Solid Bodies Description - First property | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSolidBodiesDescriptionFirstPropertyIndex,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e. swSolidBodiesDescriptionFirstPropertyIndex ,
swUserPreferenceOption_e.swDetailingNoOptionSpecified,
swSolidBodiesDescriptionPropertyIndex.< Value >) | Integer value as defined in swSolidBodiesDescriptionPropertyIndex | Valid only if Solid Bodies Description - Use default description is set to true |
| Bounding Box Properties - Solid Bodies Description - First separator | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swSolidBodiesBBoxDescriptionFirstSeparator,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceString (swUserPreferenceStringValue_e. swSolidBodiesBBoxDescriptionFirstSeparator ,
swUserPreferenceOption_e.swDetailingNoOptionSpecified,
< Value >) | String value | Valid only if Solid Bodies Description - Use default description is set to true |
| Bounding Box Properties - Solid Bodies Description - Second property | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSolidBodiesDescriptionSecondPropertyIndex,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e. swSolidBodiesDescriptionSecondPropertyIndex ,
swUserPreferenceOption_e.swDetailingNoOptionSpecified,
swSolidBodiesDescriptionPropertyIndex.< Value >) | Integer value as defined in swSolidBodiesDescriptionPropertyIndex | Valid only if Solid Bodies Description - Use default description is set to true |
| Bounding Box Properties - Solid Bodies Description - Second separator | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swSolidBodiesBBoxDescriptionSecondSeparator,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceString (swUserPreferenceStringValue_e. swSolidBodiesBBoxDescriptionSecondSeparator ,
swUserPreferenceOption_e.swDetailingNoOptionSpecified,
< Value >) | String value | Valid only if Solid Bodies Description - Use default description is set to true |
| Bounding Box Properties - Solid Bodies Description - Third property | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSolidBodiesDescriptionThirdPropertyIndex,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e. swSolidBodiesDescriptionThirdPropertyIndex ,
swUserPreferenceOption_e.swDetailingNoOptionSpecified,
swSolidBodiesDescriptionPropertyIndex.< Value >) | Integer value as defined in swSolidBodiesDescriptionPropertyIndex | Valid only if Solid Bodies Description - Use default description is set to true |
| Bounding Box Properties - Solid Bodies Description - Suffix | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swSolidBodiesBBoxDescriptionSuffix,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceString (swUserPreferenceStringValue_e. swSolidBodiesBBoxDescriptionSuffix ,
swUserPreferenceOption_e.swDetailingNoOptionSpecified,
< Value >) | String value | Valid only if Solid Bodies Description - Use default description is set to true |
| Bounding Box Properties - Solid Bodies Description - Use default
description | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSolidBBoxDescriptionUseDefault) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSolidBBoxDescriptionUseDefault,
< OnFlag >) | Boolean value |  |
| Bounding Box Properties - Sheet Metal Bodies Description - Description | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swSheetMetalDescription,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceString (swUserPreferenceStringValue_e. swSheetMetalDescription ,
swUserPreferenceOption_e.swDetailingNoOptionSpecified,
< Value >) | String value | Valid only if Sheet Metal Bodies Description - Use default
description is set to true |
| Bounding Box Properties - Sheet Metal Bodies Description - Use default
description | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSheetMetalBodiesDescriptionUseDefault) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSheetMetalBodiesDescriptionUseDefault,
< OnFlag >) | Boolean value |  |
| Bounding Box Properties - Apply to | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swBBoxDescriptionApplyMethod,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e. swBBoxDescriptionApplyMethod ,
swUserPreferenceOption_e.swDetailingNoOptionSpecified,
swBBoxDescriptionApplyMethod_e.< Value >) | Integer value as defined in swBBoxDescriptionApplyMethod_e |  |
| Cut list IDs - Generate Cut list IDs | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swWeldmentGenerateCutlistIDs) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swWeldmentGenerateCutlistIDs,
< OnFlag >) | Boolean value | If set to true and a cut list is available, generates cut list IDs |
| Cut list IDs - Structure Cut list ID | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swWeldmentStructureCutlistID,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceString (swUserPreferenceStringValue_e. swWeldmentStructureCutlistID ,
swUserPreferenceOption_e.swDetailingNoOptionSpecified,
< Value >) | String values are properties that are listed in the Cut-List Properties
dialog: "%Description%" "%MATERIAL%" "%LENGTH%" "%ANGLE1%" "%ANGLE2%" "%Angle Direction%" "%Angle Rotation%" | Valid only if Cut list IDs - Generate Cut list IDs is set to true |
| Cut list IDs - Sheet Metal Cut list ID | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swWeldmentSheetmetalCutlistID,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceString (swUserPreferenceStringValue_e. swWeldmentSheetmetalCutlistID ,
swUserPreferenceOption_e.swDetailingNoOptionSpecified,
< Value >) | String values are properties that are listed in the Cut-List Properties
dialog : "%Description%" "%MATERIAL%" "%Bounding Box Length%" "%Bounding
Box Width%" "%Sheet Metal Thickness%" "%Bounding Box Area%" "%Bends%" "%Bend Radius%" | Valid only if Cut list IDs - Generate Cut list IDs is set to true |
| Cut list IDs - Generic Cut list ID | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swWeldmentGenericCutlistID,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceString (swUserPreferenceStringValue_e. swWeldmentGenericCutlistID ,
swUserPreferenceOption_e.swDetailingNoOptionSpecified,
< Value >) | String values are properties that are listed in the Cut-List Properties
dialog: "%Description%" "%MATERIAL%" | Valid only if Cut list IDs - Generate Cut list IDs is set to true |
| Cut list IDs - Use document unit settings (Converts Cut list IDs to
document's unit settings) | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swGenerateCutlistIDsInDocUnits) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swGenerateCutlistIDsInDocUnits,
< OnFlag >) | Boolean value | Valid only if Cut list IDs - Generate Cut list IDs is set to true |
