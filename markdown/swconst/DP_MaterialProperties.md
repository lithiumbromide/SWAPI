---
title: "Document Properties > Material Properties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_MaterialProperties.htm"
---

# Document Properties > Material Properties

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Density | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swMaterialPropertyDensity, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swMaterialPropertyDensity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value in kg/m^3 | For parts only; specifies material density |
| Area Hatch/Fill - Style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swMaterialPropertyAreaHatchFillStyle, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swMaterialPropertyAreaHatchFillStyle, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swAreaHatchFillStyle_e.< Value >) | See swAreaHatchFillStyle_e for valid options |  |
| Area Hatch/Fill - Pattern | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swMaterialPropertyCrosshatchPattern, swuserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceString (swUserPreferenceStringValue_e.swMaterialPropertyCrosshatchPattern, swuserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Valid string values: | For parts only; for hatch style only |
| Area Hatch/Fill - Scale | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swMaterialPropertyCrosshatchScale, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swMaterialPropertyCrosshatchScale, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | For parts only; for hatch style only; specifies value by which to scale crosshatch |
| Area Hatch/Fill - Angle | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swMaterialPropertyCrosshatchAngle, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swMaterialPropertyCrosshatchAngle, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | For parts only; for hatch style only; specifies angle for crosshatch |
