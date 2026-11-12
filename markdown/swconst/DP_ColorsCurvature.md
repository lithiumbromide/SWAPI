---
title: "Document Properties > Colors > Curvature"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_ColorsCurvature.htm"
---

# Document Properties > Colors > Curvature

The Curvature dialog appears when you click Curvature... in Document Properties > Colors. Click Help on the Curvature dialog to learn more about Curvature settings.

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Curvature value 1 | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swCurvatureValue1, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swCurvatureValue1, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value between 0.0005 and 1000, inclusive | Maps the greatest curvature value to red |
| Curvature value 2 | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swCurvatureValue2, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swCurvatureValue2, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value between 0.0005 and 1000, inclusive | Maps the second greatest curvature value to green |
| Curvature value 3 | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swCurvatureValue3, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swCurvatureValue3, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value between 0.0005 and 1000, inclusive | Maps the third greatest curvature value to blue |
| Curvature value 4 | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swCurvatureValue4, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swCurvatureValue4, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value between 0.0005 and 1000, inclusive | Maps the fourth greatest curvature value to gray |
| Curvature value 5 | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swCurvatureValue5, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swCurvatureValue5, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value between 0.0005 and 1000, inclusive | Maps the least curvature value to black |
