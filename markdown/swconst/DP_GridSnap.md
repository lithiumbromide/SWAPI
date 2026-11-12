---
title: "Document Properties > Grid/Snap"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_GridSnap.htm"
---

# Document Properties > Grid/Snap

## Document Properties > Grip/Snap

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Display grid | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swGridDisplay, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swGridDisplay, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to display sketch grid |
| Dash | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swGridDisplayDashed, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swGridDisplayDashed, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to use solid or dashed grid lines; does not affect current document; only affects future documents |
| Automatic scaling | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swGridAutomaticScaling, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swGridAutomaticScaling, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to automatically adjust display of grid when zooming in and out |
| Major grid spacing | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swGridMajorSpacing, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swGridMajorSpacing, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value in meters | Specifies space between major grid lines |
| Minor-lines per major | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swGridMinorLinesPerMajor, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swGridMinorLinesPerMajor, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer value | Specifies the number of minor grid lines between major grid lines |
| Snap points per minor | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSnapPointsPerMinor, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSnapPointsPerMinor, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer value | Specifies the number of snap points between minor grid lines |
