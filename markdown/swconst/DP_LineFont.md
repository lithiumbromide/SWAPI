---
title: "Document Properties > Line Font"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_LineFont.htm"
---

# Document Properties > Line Font

HTML PUBLIC "-//W3C//DTD HTML 4.0 Frameset//EN"

(==============================================================)

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Visible Edges - Style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontVisibleEdgesStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontVisibleEdgesStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineStyles_e.< Value >) | See swLineStyles_e for valid options except swLineDEFAULT | Specifies style of visible edges |
| Visible Edges - Thickness | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontVisibleEdgesThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontVisibleEdgesThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options | Specifies thickness of visible edges |
| Visible Edges - Custom thickness | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontVisibleEdgesThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontVisibleEdgesThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies a custom thickness for visible edges |
| Visible Edges - End cap style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontVisibleEdgesEndCap,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontVisibleEdgesEndCap,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineEndCaps_e.< Value >) | See swLineEndCaps_e for valid options | Specifies style of visible edge end caps |
| Hidden Edges - Style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontHiddenEdgesStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontHiddenEdgesStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineStyles_e.< Value >) | See swLineStyles_e for valid options except swLineDEFAULT | Specifies style of hidden edges |
| Hidden Edges - Thickness | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontHiddenEdgesThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontHiddenEdgesThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options | Specifies thickness of hidden edges |
| Hidden Edges - Custom thickness | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontHiddenEdgesThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontHiddenEdgesThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies a custom thickness for hidden edges |
| Hidden Edges - End cap style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontHiddenEdgesEndCap,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontHiddenEdgesEndCap,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineEndCaps_e.< Value >) | See swLineEndCaps_e for valid options | Specifies style of hidden edge end caps |
| Sketch Curves - Style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontSketchCurvesStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontSketchCurvesStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineStyles_e.< Value >) | See swLineStyles_e for valid options except swLineDEFAULT | Specifies style of sketch curves |
| Sketch Curves - Thickness | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontSketchCurvesThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontSketchCurvesThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options | Specifies thickness of sketch curves |
| Sketch Curves - Custom thickness | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontSketchCurvesThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontSketchCurvesThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies a custom thickness for sketch curves |
| Sketch Curves - End cap style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontSketchCurvesEndCap,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontSketchCurvesEndCap,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineEndCaps_e.< Value >) | See swLineEndCaps_e for valid options | Specifies style of sketch curve end caps |
| Construction Curves - Style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontConstructionCurvesStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontConstructionCurvesStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineStyles_e.< Value >) | See swLineStyles_e for valid options except swLineDEFAULT | Specifies style of construction curves |
| Construction Curves - Thickness | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontConstructionCurvesThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontConstructionCurvesThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options | Specifies thickness of construction curves |
| Construction Curves - Custom thickness | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontConstructionCurvesThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontConstructionCurvesThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies a custom thickness for construction curves |
| Area Hatch/Fill - Style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontCrosshatchStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontCrosshatchStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineStyles_e.< Value >) | See swLineStyles_e for valid options except swLineDEFAULT | Specifies style of hatch/fills |
| Area Hatch/Fill - Thickness | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontCrosshatchThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontCrosshatchThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options | Specifies thickness of hatch/fills |
| Area Hatch/Fill - Custom thickness | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontCrosshatchThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontCrosshatchThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies a custom thickness for hatch/fills |
| Tangent Edges - Style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontTangentEdgesStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontTangentEdgesStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineStyles_e.< Value >) | See swLineStyles_e for valid options except swLineDEFAULT | Specifies style of tangent edges |
| Tangent Edges - Thickness | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontTangentEdgesThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontTangentEdgesThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options | Specifies thickness of tangent edges |
| Tangent Edges - Custom thickness | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontTangentEdgesThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontTangentEdgesThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies a custom thickness for tangent edges |
| Cosmetic Thread - Style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontCosmeticThreadStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontCosmeticThreadStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineStyles_e.< Value >) | See swLineStyles_e for valid options | Specifies style of cosmetic threads |
| Cosmetic Thread - Thickness | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontCosmeticThreadThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontCosmeticThreadThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options | Specifies thickness of cosmetic threads |
| Cosmetic Thread - Custom thickness | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontCosmeticThreadThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontCosmeticThreadThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies a custom thickness for cosmetic threads |
| Hidden Tangent Edges - Style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontHideTangentEdgeStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontHideTangentEdgeStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineStyles_e.< Value >) | See swLineStyles_e for valid options except swLineDEFAULT | Specifies style of hidden tangent edges |
| Hidden Tangent Edges - Thickness | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontHideTangentEdgeThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontHideTangentEdgeThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options | Specifies thickness of hidden tangent edges |
| Hidden Tangent Edges - Custom thickness | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontHideTangentEdgeThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontHideTangentEdgeThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies a custom thickness for hidden tangent edges |
| Explode Lines - Style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontExplodedLinesStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontExplodedLinesStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineStyles_e.< Value >) | See swLineStyles_e for valid options except swLineDEFAULT | Specifies style of exploded lines |
| Explode Lines - Thickness | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontExplodedLinesThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontExplodedLinesThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options | Specifies thickness of exploded lines |
| Explode Lines - Custom thickness | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontExplodedLinesThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontExplodedLinesThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies a custom thickness for exploded lines |
| Break Lines - Style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontBreakLineStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontBreakLineStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineStyles_e.< Value >) | See swLineStyles_e for valid options except swLineDEFAULT | Specifies style of break lines |
| Break Lines - Thickness | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontBreakLineThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontBreakLineThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options | Specifies thickness of break lines |
| Break Lines - Custom thickness | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontBreakLineThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontBreakLineThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies a custom thickness for break lines |
| Visible Edges (SpeedPak) - Style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontSpeedPakDrawingsModelEdgesStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontSpeedPakDrawingsModelEdgesStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineStyles_e.< Value >) | See swLineStyles_e for valid options except swLineDEFAULT | Specifies style of SpeedPak drawing model edges |
| Visible Edges (SpeedPak) - Thickness | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontSpeedPakDrawingsModelEdgesThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontSpeedPakDrawingsModelEdgesThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options | Specifies thickness of SpeedPak drawing model edges |
| Visible Edges (SpeedPak) - Custom thickness | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontSpeedPakDrawingsModelEdgesThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontSpeedPakDrawingsModelEdgesThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies a custom thickness for model edges in a SpeedPak drawing document |
| Adjoining Component - Style | ModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontAdjoiningComponentStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontAdjoiningComponentStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineStyles_e.< Value >) | See swLineStyles_e for valid options except swLineDEFAULT | Specifies style of the edges of
adjoining components in drawing documents |
| Adjoining Component - Thickness | ModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontAdjoiningComponent,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontAdjoiningComponent,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options | Specifies thickness of the edges of
adjoining components in drawing documents |
| Adjoining Component - Custom
thickness | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontAdjoiningComponentCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontAdjoiningComponentCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies a custom thickness of the
edges of adjoining components in drawing documents |
| Bend Up, Flat Pattern - Style | ModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontBendLineUpStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontBendLineUpStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineStyles_e.< Value >) | See swLineStyles_e for valid options except swLineDEFAULT | Specifies style of the bend lines
indicating where to bend the sheet metal up in flat patterns in drawing documents |
| Bend Up, Flat Pattern - Thickness | ModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontBendLineUpThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontBendLineUpThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options | Specifies thickness of the bend
lines indicating where to bend the sheet metal up in flat patterns in drawing documents |
| Bend Up, Flat Pattern - Custom
thickness | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontBendLineUpThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontBendLineUpThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies a custom thickness of the
bend lines indicating where to bend the sheet metal up in flat patterns in drawing documents |
| Bend Down, Flat Pattern - Style | ModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontBendLineDownStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontBendLineDownStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineStyles_e.< Value >) | See swLineStyles_e for valid options except swLineDEFAULT | Specifies style of the bend lines
indicating where to bend the sheet metal down in flat patterns in drawing documents |
| Bend Down, Flat Pattern - Thickness | ModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontBendLineDownThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontBendLineDownThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options | Specifies thickness of the bend
lines indicating where to bend the sheet metal down in flat patterns in drawing documents |
| Bend Down, Flat Pattern - Custom
thickness | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontBendLineDownThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontBendLineDownThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies a custom thickness of the
bend lines indicating where to bend the sheet metal down in flat patterns in drawing documents |
| Envelope Components - Style | ModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontEnvelopeComponentStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontEnvelopeComponentStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineStyles_e.< Value >) | See swLineStyles_e for valid options except swLineDEFAULT | Specifies style of the edges of
envelope components |
| Envelope Components - Thickness | ModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontEnvelopeComponentThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontEnvelopeComponentThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options | Specifies thickness of the edges of
envelope components |
| Envelope Components - Custom
thickness | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontEnvelopeComponentThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontEnvelopeComponentThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies a custom thickness of the
edges of envelope components |
| Emphasized Section Outline - Style | ModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontEmphasizedSectionOutlineStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontEmphasizedSectionOutlineStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineStyles_e.< Value >) | See swLineStyles_e for valid options except swLineDEFAULT | Specifies style of the outline of an emphasized section |
| Emphasized Section Outline - Thickness | ModelDocExtension::GetUserPreferenceInteger (swUserPreferenceDoubleValue_e.swLineFontEmphasizedSectionThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceDoubleValue_e.swLineFontEmphasizedSectionThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value > ) | See swLineWeights_e for valid options | Specifies the thickness of the outline of an emphasized section |
| Emphasized Section Outline - Custom thickness | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontEmphasizedSectionThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swLineFontEmphasizedSectionThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies a custom thickness of the
outline of an emphasized section |
| Emphasized Section Outline - End cap style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontEmphasizedSectionEndCapStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swLineFontEmphasizedSectionEndCapStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineEndCaps_e.< Value >) | See swLineEndCaps_e for valid options | Specifies style of emphasized section outline end caps |
