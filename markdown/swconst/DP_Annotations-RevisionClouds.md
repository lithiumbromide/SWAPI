---
title: "Document Properties > Annotations > Revision Clouds"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_Annotations-RevisionClouds.htm"
---

# Document Properties > Annotations > Revision Clouds

S

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Overall drafting standard | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingDimensionStandard, swUserPreferenceOption_e.swDetailingRevisionCloud) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingDimensionStandard, swUserPreferenceOption_e.swDetailingRevisionCloud, swDetailingStandard_e.< Value >) | See swDetailingStandard_e for valid options | Specifies the overall drafting standard |
| Line style - Frame Style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingRevisionCloudLineStyle, swUserPreferenceOption_e.swDetailingRevisionCloud) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingRevisionCloudLineStyle, swUserPreferenceOption_e.swDetailingRevisionCloud, swLineStyles_e.< Value >) | See swLineStyles_e for valid options | Specifies the style of the frames of revision clouds |
| Line style - Frame Thickness | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingRevisionCloudLineThickness, swUserPreferenceOption_e.swDetailingRevisionCloud) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingRevisionCloudLineThickness, swUserPreferenceOption_e.swDetailingRevisionCloud, swLineWeights_e.< Value >) | See swLineWeights_e for valid options | Specifies the thickness of the frames of revision clouds |
| Line style - Custom Thickness | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingRevisionCloudLineThicknessCustom, swUserPreferenceOption_e.swDetailingRevisionCloud) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingRevisionCloudLineThicknessCustom, swUserPreferenceOption_e.swDetailingRevisionCloud, < Value >) | Double value | Specifies a custom thickness for the frames of revision clouds; sets Custom Thickness to the specified thickness and Frame Thickness to Custom Size |
| Maximum arc radius | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingRevisionCloudMaxArcRadius, swUserPreferenceOption_e.swDetailingRevisionCloud) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingRevisionCloudMaxArcRadius, swUserPreferenceOption_e.swDetailingRevisionCloud, < Value >) | Double value | Specifies the maximum radius of each frame arc |
| Layer | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swDetailingLayer, swUserPreferenceOption_e.swDetailingRevisionCloud) IModelDocExtension::SetUserPreferenceString (swUserPreferenceStringValue_e.swDetailingLayer, swUserPreferenceOption_e.swDetailingRevisionCloud, < Value >) | Valid Options: "Border" "Dimensions" "Notes" "BOM" "FORMAT" | This setting is available only on drawings; depending on drawing, some options may not apply |
