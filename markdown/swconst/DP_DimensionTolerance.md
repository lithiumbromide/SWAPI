---
title: "Document Properties > Dimensions > Dimension Tolerance"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_DimensionTolerance.htm"
---

# Document Properties > Dimensions > Dimension Tolerance

The dialog above appears when the Tolerance button is clicked on the following document property pages:

| Document Properties page | < UserPrefOption > |
| --- | --- |
| Dimensions | swDetailingDimension |
| Dimensions > Angle | swDetailingAngleDimension |
| Dimensions > Angular Running | swDetailingAngularRunningDimension |
| Dimensions > Arc Length | swDetailingArcLengthDimension |
| Dimensions > Chamfer | swDetailingChamferDimension |
| Dimensions > Diameter | swDetailingDiameterDimension |
| Dimensions > Hole Callout | swDetailingHoleDimension |
| Dimensions > Linear | swDetailingLinearDimension |
| Dimensions > Ordinate | swDetailingOrdinateDimension |
| Dimensions > Radius | swDetailingRadiusDimension |

Substitute <UserPrefOption> in the methods following to get and set the dimension tolerance settings for a given dimension document property.

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Tolerance type | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingToleranceStyle, swUserPreferenceOption_e.< UserPrefOption >) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingToleranceStyle, swUserPreferenceOption_e.< UserPrefOption >, swTolType_e.< Value >) | See swTolType_e for valid options |  |
| + Maximum tolerance value | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingMaxToleranceValue, swUserPreferenceOption_e.< UserPrefOption >) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingMaxToleranceValue, swUserPreferenceOption_e.< UserPrefOption >, < Value >) | Double value | Specifies the maximum tolerance for dimensions in a drawing document |
| — Minimum tolerance value | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingMinToleranceValue, swUserPreferenceOption_e.< UserPrefOption >) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingMinToleranceValue, swUserPreferenceOption_e.< UserPrefOption >, < Value >) | Double value | Specifies the minimum tolerance for dimensions in a drawing document |
| Dual dimension tolerance - Inward rounding of secondary unit tolerance extents | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDimensionsToleranceInwardRounding, swUserPreferenceOption_e.< UserPrefOption >) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDimensionsToleranceInwardRounding, swUserPreferenceOption_e.< UserPrefOption >, < Value >) | Boolean value | Specifies whether to set the limits of the secondary unit's tolerance range to fit within the tolerance range of the primary unit by using inward rounding so that the dual dimension does not conflict with the primary dimension |
| Font - Use dimension font | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDimensionsToleranceUseDimensionFont, swUserPreferenceOption_e.< UserPrefOption >) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDimensionsToleranceUseDimensionFont, swUserPreferenceOption_e.< UserPrefOption >, < Value >) | Boolean value | Specifies whether to change font size for dimension tolerance text |
| Font - Size by scale or height | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingToleranceTextSizing, swUserPreferenceOption_e.< UserPrefOption >) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingToleranceTextSizing, swUserPreferenceOption_e.< UserPrefOption >, swDetailingToleranceTextSizing_e.< Value >) | See swDetailingToleranceTextSizing_e for valid options; depending on the option chosen, also set either font scale value or font height value | Specifies how to size the tolerance text |
| Font - Font scale value | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingToleranceTextScale, swUserPreferenceOption_e.< UserPrefOption >) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingToleranceTextScale, swUserPreferenceOption_e.< UserPrefOption >, < Value >) | Double value (0 - 10.0) | Specifies value to scale tolerance font |
| Font - Font height value | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingToleranceTextHeight, swUserPreferenceOption_e.< UserPrefOption >) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingToleranceTextHeight, swUserPreferenceOption_e.< UserPrefOption >, < Value >) | Double value in meters | Specifies height of tolerance font |
| Fit tolerance font - Use dimension font | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDimensionsToleranceFitToUseDimensionFont, swUserPreferenceOption_e.< UserPrefOption >) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDimensionsToleranceFitToUseDimensionFont, swUserPreferenceOption_e.< UserPrefOption >, < Value >) | Boolean value | For Fit and Fit-with-tolerance tolerance types only; specifies whether to use dimension tolerance text |
| Fit tolerance font - Size by scale or height | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingToleranceFitTolTextSizing, swUserPreferenceOption_e.< UserPrefOption >) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingToleranceFitTolTextSizing, swUserPreferenceOption_e.< UserPrefOption >, swDetailingToleranceTextSizing_e.< Value >) | See swDetailingToleranceTextSizing_e for valid options; depending on the option chosen, also set either fit tolerance font scale value or font height value | For Fit and Fit-with-tolerance tolerance types only; specifies how to size the fit tolerance text |
| Fit tolerance font - Font scale | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingToleranceFitTolTextScale, swUserPreferenceOption_e.< UserPrefOption >) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingToleranceFitTolTextScale, swUserPreferenceOption_e.< UserPrefOption >, < Value >) | Double value (0 - 10.0) | For Fit and Fit-with-tolerance tolerance types only; specifies scale for fit tolerance font |
| Fit tolerance font - Font height | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingToleranceFitTolTextHeight, swUserPreferenceOption_e.< UserPrefOption >) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingToleranceFitTolTextHeight, swUserPreferenceOption_e.< UserPrefOption >, < Value >) | Double value in meters | For Fit and Fit-with-tolerance tolerance types only; specifies height of fit tolerance font |
| Show parentheses | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDimensionsToleranceUseParentheses, swUserPreferenceOption_e.< UserPrefOption >) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDimensionsToleranceUseParentheses, swUserPreferenceOption_e.< UserPrefOption >, < Value >) | Boolean value | For Bilateral, Symmetric, or Fit-with-tolerance tolerance types only; specifies whether to show parentheses around linear tolerances |
| Fit tolerance display | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingToleranceFitTolDisplay, swUserPreferenceOption_e.< UserPrefOption >) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingToleranceFitTolDisplay, swUserPreferenceOption_e.< UserPrefOption >, swFitTolDisplay_e.< Value >) | See swFitTolDisplay_e for valid options | For Fit and Fit-with-tolerance tolerance types only |
