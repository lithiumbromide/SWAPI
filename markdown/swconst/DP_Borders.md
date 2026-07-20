---
title: "Document Properties > Borders ( drawings only )"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_Borders.htm"
---

# Document Properties > Borders ( drawings only )

HTML PUBLIC "-//W3C//DTD HTML 4.0 Frameset//EN"

(==============================================================)

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Border - Line Style of Border | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingBorderLeaderLineStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingBorderLeaderLineStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineStyles_e. < Value > ) | See swLineStyles_e for valid options | Specifies the style of border lines |
| Border - Line Width of Border | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingBorderLeaderLineThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingBorderLeaderLineThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e. < Value > ) | See swLineWeights_e for valid options | Specifies the thickness of border lines |
| Border - Custom thickness | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingBorderLeaderCustomLineThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingBorderLeaderCustomLineThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value > ) | Double value | Specifies custom thickness of border lines; sets Custom Thickness to the specified thickness and Line Width of Border to Custom Size |
| Border - Double-line border | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingBorderDoubleLine,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingBorderDoubleLine,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to use double-line borders |
| Zone Formatting - Show zone dividers | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingBorderShowZoneDividers,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingBorderShowZoneDividers,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to show zone dividers |
| Zone Formatting - Line Style of Zone Divider | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingBorderZoneDividerLineStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingBorderZoneDividerLineStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineStyles_e. < Value > ) | See swLineStyles_e for valid options | Specifies the style of zone divider lines |
| Zone Formatting - Line Width of Zone Divider | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingBorderZoneDividerLineThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingBorderZoneDividerLineThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e. < Value > ) | See swLineWeights_e for valid options | Specifies the thickness of zone divider lines |
| Zone Formatting - Custom thickness | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingBorderZoneDividerCustomLineThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingBorderZoneDividerCustomLineThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value > ) | Double value | Specifies custom thickness of zone divider lines; sets Custom Thickness to the specified thickness and Line Width of Zone Divider to Custom Size |
| Zone Divider - Length of Zone Divider | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingBorderZoneDividerLength,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingBorderZoneDividerLength,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value > ) | Double value | Specifies the length of zone dividers |
| Center Zone Divider - Length of outer Center Zone Divider | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingBorderOuterCenterZoneDividerLength,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingBorderOuterCenterZoneDividerLength,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value > ) | Double value | Specifies the length of outer center zone dividers |
| Center Zone Divider - Length of inner Center Zone Divider | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingBorderInnerCenterZoneDividerLength,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingBorderInnerCenterZoneDividerLength,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value > ) | Double value | Specifies the length of inner center zone dividers |
| Zone Labels - Show columns | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingBorderShowColumns,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingBorderShowColumns,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to show column zone labels |
| Zone Labels - Show rows | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingBorderShowRows,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingBorderShowRows,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to show row zone labels |
| Layer | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swBorderLayer,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceString (swUserPreferenceStringValue_e.swBorderLayer,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Valid Options: "Border" "Dimensions" "Notes" "BOM" "FORMAT" | Depending on the drawing, some options may not apply |
