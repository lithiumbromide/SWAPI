---
title: "View > Display"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/ViewDisplay.htm"
---

# View > Display

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Shadows in Shaded Mode | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayShadowsInShadedMode) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e. swDisplayShadowsInShadedMode ,
< OnFlag>) | Boolean value | Specifies whether to display a shadow under the model |
| Ambient Occlusion | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayAmbientOcclusionShadows) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e. swDisplayAmbientOcclusionShadows ,
< OnFlag>) | Boolean value | Specifies whether to use global
lighting that adds realism to models by controlling the attenuation of ambient
light due to occluded areas; available in all scenes when you use RealView
graphics |
| RealView Graphics | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayRealViewGraphics) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e. swDisplayRealViewGraphics ,
< OnFlag>) | Boolean value | Specifies whether to display a model with hardware accelerated shaders |
| Cartoon | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayCartoon) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e. swDisplayCartoon ,
< OnFlag>) | Boolean value | Specifies whether to apply a cartoon effect to model edges and faces |
