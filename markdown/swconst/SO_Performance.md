---
title: "System Options > Performance"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_Performance.htm"
---

# System Options > Performance

## System Options - Performance

This topic contains two tables. The information in the table:

- appearing immediately after the screen capture
  of the dialog corresponds to the settings
  on that dialog.
- titled

  [Obsolete
  Enumerators](#Obsolete)

  contains enumerators that previously appeared on
  the dialog but are now obsolete.

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Verification on rebuild | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPerformanceVerifyOnRebuild) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPerformanceVerifyOnRebuild,
< OnFlag >) | Boolean value | Controls the level of error checking when you create or modify features.
For most applications, the default setting (cleared) is adequate and results
in a faster rebuild of the model |
| Ignores self-intersection check for some sheet metal features | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPerformanceSheetMetalIgnoreSelfIntersect) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPerformanceSheetMetalIgnoreSelfIntersect,
< OnFlag >) | Boolean value | Specifies whether to suppress warning messages for certain sheet metal
parts; for example, when flanges share a common edge and the part flattens
correctly but displays a warning message |
| Transparency - High quality for normal view mode | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swUseAlphaTransparency) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swUseAlphaTransparency,
< OnFlag >) | Boolean value | Specifies whether to change transparency quality from high to low when
part or assembly is moving |
| Transparency - High quality for dynamic view mode | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swTransparencyHighQualityDynamic) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swTransparencyHighQualityDynamic,
< OnFlag >) | Boolean value | Specifies whether high-quality transparency is retained while moving
or rotating model with pan or rotate tools |
| Curvature generation | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPerformanceAlwaysGenerateCurvature) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPerformanceAlwaysGenerateCurvature,
< OnFlag >) | Boolean value: True = Always (for every shaded model) False = Only on demand | Specifies whether to always display curvature for shaded models |
| Level of detail | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swLevelOfDetail) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swLevelOfDetail,
< Value >) | Integer value ranging from 0 to 20 | Target frame rates ranging from 0 (off) to 20 (maximum level of detail
removed); for example, if set at 20, then try and get 20FPS on spin dynamics
by dropping detail until rate is achieved |
| Assembly loading - Automatically load component data on demand - or - Manually manage resolved and lightweight modes | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAssemblyLoadComponents) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAssemblyLoadComponents,
swAssemblyLoadComponents_e.< Value >) | See swAssemblyLoadComponents_e for options |  |
| Assembly loading - Auto resolve sub-assemblies upon expansion in tree | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swAutoResolveSubAssembliesUponExpansionInTree) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swAutoResolveSubAssembliesUponExpansionInTree,
< OnFlag >) | Boolean value | Valid only if Assembly loading - Manually manage resolved and lightweight
modes is selected |
| Assembly loading - Load component lightweight | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swAutoLoadPartsLightweight) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swAutoLoadPartsLightweight,
< OnFlag >) | Boolean value | Valid only if Assembly loading - Manually manage resolved and lightweight
modes is selected |
| Assembly loading - Always resolve subassemblies | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPerformanceAlwaysResolveSubassemblies) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPerformanceAlwaysResolveSubassemblies,
< OnFlag >) | Boolean value | Specifies whether to always resolve subassemblies when an assembly opens
lightweight; Valid only if Assembly loading - Manually manage resolved and
lightweight modes is selected |
| Assembly loading - Check out-of-date lightweight components | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swCheckForOutOfDateLightweightComponents) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swCheckForOutOfDateLightweightComponents,
swCheckOutOfDate_e.< Value >) | See swCheckOutOfDate_e for valid options | Valid only if Assembly loading - Manually manage resolved and lightweight
modes is selected |
| Assembly loading - Resolve lightweight components | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swResolveLightweight) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swResolveLightweight,
swPromptAlwaysNever_e.< Value >) | Boolean value: 0 = Prompt 1 = Always | Valid only if Assembly loading - Manually manage resolved and lightweight
modes is selected |
| Assembly loading - Rebuild assembly on load: | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPerformanceAssemRebuildOnLoad) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPerformanceAssemRebuildOnLoad,
swPromptAlwaysNever_e.< Value >) | See swPromptAlwaysNever_e for valid options | Valid only if Assembly loading - Manually manage resolved and lightweight
modes is selected |
| Mates - Mate animation speed | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swMateAnimationSpeed) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swMateAnimationSpeed,
< Value >) | Double value: 0 = off >0 = animation speed in seconds | Specifies speed of animation for mates |
| Mates - SmartMate Sensitivity | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swSmartMateSensitivity) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swSmartMateSensitivity,
< Value >) | Double value: 0 = off >0 = animation speed in seconds | Specifies the speed at which SmartMates are applied |
| Mates -
Magnetic mate pre-alignment | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swMagMatePreAlign) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swMagMatePreAlign,
< OnFlag >) | Boolean value | Specifies whether to enable magnetic
mates pre-alignment |
| Save - Purge cached configuration data | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPurgeAllBodiesForNonActiveConfigurations) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPurgeAllBodiesForNonActiveConfigurations,
< OnFlag >) | Boolean value | Specifies whether to purge cached configuration data to reduce file size and
save time |
| Save - Update mass properties while saving document | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swUpdateMassPropsDuringSave) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swUpdateMassPropsDuringSave,
< OnFlag >) | Boolean value | Specifies whether to update mass properties information when saving
document |
| Use shaded preview | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swUseShadedPreview) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swUseShadedPreview,
< OnFlag >) | Boolean value | Specifies whether to use shaded preview |
| Use software OpenGL | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swUseSimpleOpenGL) | Read-only Boolean value | Specifies whether graphics adapter hardware acceleration is disabled
and graphics rendering using only software is enabled |
| Enhanced graphics performance (requires SOLIDWORKS restart) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEnablePerformancePipeline) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEnablePerformancePipeline,
< OnFlag >) | Boolean value |  |
| Hardware accelerated silhouette edges | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swHardwareAccSilhouetteEdges) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swHardwareAccSilhouetteEdges,
< OnFlag >) | Boolean value |  |

Obsolete Enumerators

(Table)=========================================================

| Enumerator | Comment |
| --- | --- |
| swPerformanceRemoveDetailDuringZoomPanRotate | Obsolete; specified
whether to remove small components and faces (both interior and exterior)
from graphics area when zooming, panning, or rotating model to improve
system performance |
| swPerformanceSave | Obsolete |
| swPerformancePreviewDuringOpen | Obsolete; specified whether to
preview the model while opening it |
