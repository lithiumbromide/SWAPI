---
title: "Document Properties > Colors > Advanced"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_ColorsAdvanced.htm"
---

# Document Properties > Colors > Advanced

## Document Properties > Colors > Advanced Properties

The Advanced Properties dialog appears when you click Advanced... in Document Properties > Colors. The Advanced... button is enabled only when Shading is selected in the Model/feature colors combo box.

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Ambient | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDocumentColorAdvancedAmbient, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDocumentColorAdvancedAmbient, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value between 0 and 1 | Specifies how light is reflected and scattered by other objects |
| Diffuse | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDocumentColorAdvancedDiffuse, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDocumentColorAdvancedDiffuse, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value between 0 and 1 | Specifies how light is scattered equally in all directions on the surface |
| Specularity | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDocumentColorAdvancedSpecularity, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDocumentColorAdvancedSpecularity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value between 0 and 1 | Specifies how surfaces exhibit highlights |
| Shininess | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDocumentColorAdvancedShininess, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDocumentColorAdvancedShininess, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value between 0 and 1 | Specifies how solid objects alternate between a glossy, reflective surface and a dull, matte surface |
| Transparency | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDocumentColorAdvancedTransparency, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDocumentColorAdvancedTransparency, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value between 0 and 1 | Specifies how much light passes through the surface |
| Emission | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDocumentColorAdvancedEmission, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDocumentColorAdvancedEmission, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value between 0 and 1 | Specifies how light projects from the surface |
