---
title: "Document Properties > Plane Display"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_PlaneDisplay.htm"
---

# Document Properties > Plane Display

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Faces - Front Face Color... | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swPlaneDisplayFrontFaceColor, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swPlaneDisplayFrontFaceColor, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer RGB color value |  |
| Faces - Back Face Color... | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swPlaneDisplayBackFaceColor, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swPlaneDisplayBackFaceColor, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer RGB color value |  |
| Faces - Transparency | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swPlaneDisplayTransparency, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swPlaneDisplayTransparency, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer percentage value (0 - 100) |  |
| Intersections - Show intersections | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPlaneDisplayShowIntersections, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPlaneDisplayShowIntersections, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to display the line at which two planes intersect |
| Intersections - Line Color... | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swPlaneDisplayIntersectionLineColor, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swPlaneDisplayIntersectionLineColor, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer RGB color value |  |
