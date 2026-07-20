---
title: "Document Properties > Annotations > Surface Finishes"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_Annotations-SurfaceFinishes.htm"
---

# Document Properties > Annotations > Surface Finishes

HTML PUBLIC "-//W3C//DTD HTML 4.0 Frameset//EN"

(==============================================================)

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Base surface finish standard | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingDimensionStandard,
swUserPreferenceOption_e.swDetailingSurfaceFinishSymbol) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingDimensionStandard,
swUserPreferenceOption_e.swDetailingSurfaceFinishSymbol, swDetailingStandard_e.< Value >) | See swDetailingStandard_e for valid options | Specifies the base surface finish standard to use |
| Surface symbol standard | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingSFSymbolStandard,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingSFSymbolStandard,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swDetailingSFSymbolStandard_e.< Value >) | See swDetailingSFSymbolStandard_e for valid options |  |
| Leader style - Leader Style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingSFSymbolLeaderLineStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingSFSymbolLeaderLineStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineStyles_e.< Value >) | See swLineStyles_e for valid options |  |
| Leader style - Leader Thickness | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingSFSymbolLeaderLineThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingSFSymbolLeaderLineThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options |  |
| Leader style - Custom thickness | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingSFSymbolLeaderLineThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingSFSymbolLeaderLineThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies custom thickness of surface finish symbol leader lines; sets Custom Thickness to the specified thickness and Leader Thickness to Custom Size |
| Text - Font... | IModelDocExtension::GetUserPreferenceTextFormat (swUserPreferenceTextFormat_e.swDetailingSurfaceFinishTextFormat,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceTextFormat (swUserPreferenceTextFormat_e.swDetailingSurfaceFinishTextFormat,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | See ITextFormat for font options | To set font property values, implement ITextFormat, set the appropriate
ITextFormat member values, and pass the ITextFormat object in the API
set method |
| Leader display - Straight or Bent | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingSFSymbolLeaderStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingSFSymbolLeaderStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLeaderStyle_e.< Value >) | See swLeaderStyle_e for valid options | Specifies notes leader style |
| Leader display - Use document leader length | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingSFSymbolUseDocBentLeaderLength,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingSFSymbolUseDocBentLeaderLength,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to use document bent leader lengths for annotations |
| Leader display - Leader length | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingSFSymbolBentLeaderLength,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingSFSymbolBentLeaderLength,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies the length of surface finish symbol leader lines in a drawing
document |
| Display symbols per 2002 | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDisplaySFSymbolsPer2002,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDisplaySFSymbolsPer2002,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to use 2002 standard to display surface finish symbols |
| Layer | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swDetailingLayer,
swuserPreferenceOption_e.swDetailingSurfaceFinishSymbol) IModelDocExtension::SetUserPreferenceString (swUserPreferenceStringValue_e.swDetailingLayer,
swuserPreferenceOption_e.swDetailingSurfaceFinishSymbol, < Value >) | String value | Specifies the name of the layer to apply settings to; this setting is
available only on drawings |
