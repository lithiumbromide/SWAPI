---
title: "IDisplayDimension Interface Members"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html"
---

# IDisplayDimension Interface Members

The following tables list the members exposed by[IDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | ArcExtensionLineOrOppositeSide | Gets or sets whether to attach or extend the radial dimension leader on this radial display dimension. |
| Property | ArrowSide | Gets or sets the position of the dimension arrows. |
| Property | CenterText | Gets or sets whether the text of this display dimension should be automatically centered. |
| Property | ChamferPrecision | Gets or sets the precision of the length and angle values in a chamfer display dimension. |
| Property | ChamferTextStyle | Gets or sets the text style for chamfer dimensions. |
| Property | Diametric | Gets or sets whether this display dimension is radial/single distance or diameter/doubled distance. |
| Property | DimensionToInside | Gets or sets whether dimensions to arcs are always to the inside of the arc. |
| Property | DisplayAsChain | Gets or sets whether the extension lines of every dimension in this set of angular running or ordinate dimensions are chained together. |
| Property | DisplayAsLinear | Gets or sets whether this diameter dimension is displayed as a linear dimension. |
| Property | Elevation | Gets or sets whether to display an elevation symbol, which is controlled by IDisplayDimension::EndSymbol , at the end of ordinate dimension extension lines. |
| Property | EndSymbol | Gets or sets the ordinate dimension end symbol. |
| Property | ExtensionLineExtendsFromCenterOfSet | Gets or sets whether extension lines extend from the center of this set of angular running dimensions. |
| Property | ExtensionLineSameAsLeaderStyle | Gets or sets whether to use leader line styles for extension line styles. |
| Property | ExtensionLineUseDocumentDisplay | Gets or sets whether to use the document settings for extension lines. |
| Property | Foreshortened | Gets or sets whether a linear dimension is foreshortened in a drawing. |
| Property | GridBubble | Gets or sets whether to display a grid bubble at the end of ordinate dimension extension lines. |
| Property | HorizontalJustification | Gets or sets the dimension text's horizontal justification. |
| Property | Inspection | Gets or sets whether a display dimension above the dimension line is displayed as an inspection dimension. |
| Property | IsLinked | Gets whether the dimension has text linked to it. |
| Property | Jogged | Gets or sets whether this ordinate or angular running dimension is jogged. |
| Property | LeaderVisibility | Gets or sets which leader lines (dimension lines) are visible on a display dimension. |
| Property | LowerInspection | Gets or sets whether a display dimension below the dimension line is displayed as an inspection dimension. |
| Property | MarkedForDrawing | Gets or sets whether this display dimension is marked to include in a drawing document. |
| Property | MaxWitnessLineLength | Gets or sets the maximum length of dimension extension lines. |
| Property | OffsetText | Gets or sets whether or not to offset the text of a dimension. |
| Property | RunBidirectionally | Gets or sets whether each dimension runs in a direction closest to the baseline in this angular running dimension. |
| Property | Scale2 | Gets or sets the scale value that is applied to the dimension value of this non-associative distance dimension. |
| Property | ShortenedRadius | Gets or sets whether to display this radius display dimension with a foreshortened radius. |
| Property | ShowDimensionValue | Gets or sets whether the dimension value is displayed as part of the dimension text. |
| Property | ShowLowerParenthesis | Gets or sets whether to enclose the text below the dimension line of the display dimension in parentheses. |
| Property | ShowParenthesis | Gets or sets whether to enclose the text above the dimension line of the display dimension in parentheses. |
| Property | ShowTolParenthesis | Obsolete. Superseded by IDisplayDimension::ShowParenthesis . |
| Property | SmartWitness | Gets or sets the smart display of extension lines. |
| Property | SolidLeader | Gets or sets whether this display dimension is displayed with a solid leader for arc and radial dimensions. |
| Property | Split | Gets or sets whether to split a dual dimension above and below an unbroken dimension line (also called a leader). |
| Property | Type2 | Gets the type of dimension. |
| Property | VerticalJustification | Gets the dimension text's vertical justification. |
| Property | WitnessVisibility | Gets or sets which extension lines are visible. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddDisplayEnt | Overrides the display graphics of objects. |
| Method | AddDisplayText | Overrides the display text. |
| Method | AlignToEdge | Aligns this linear dimension with the specified edge. |
| Method | AutoJogOrdinate | Sets the auto-jog for this ordinate dimension. |
| Method | ExplementaryAngle | Flips an angular dimension to its explementary angle. |
| Method | GetAlternatePrecision | Obsolete. Superseded by IDisplayDimension::GetAlternatePrecision2 . |
| Method | GetAlternatePrecision2 | Gets the displayed precision for the dual portion of this dimension. |
| Method | GetAlternateTolPrecision | Obsolete. Superseded by IDisplayDimension::GetAlternateTolPrecision . |
| Method | GetAlternateTolPrecision2 | Gets the displayed precision for the dual tolerance portion of this dimension. |
| Method | GetAnnotation | Gets the IAnnotation object for this specific annotation. |
| Method | GetArcLengthLeader | Gets the leader style of this arc length dimension. |
| Method | GetArrowHeadStyle | Obsolete. Superseded by IDisplayDimension::GetArrowHeadStyle2 . |
| Method | GetArrowHeadStyle2 | Gets the arrowhead style used by this display dimension. |
| Method | GetAutoArcLengthLeader | Gets whether the leader style of this arc-length dimension is being automatically selected or selected by the user. |
| Method | GetBentLeaderLength | Gets the length of the bent leader to use when displaying this dimension. |
| Method | GetBrokenLeader2 | Gets whether this display dimension has a broken or split leader. |
| Method | GetChamferUnits | Gets the local units of measurement for a chamfer display dimension. |
| Method | GetDefinitionTransform | Gets the transform for this dimension. |
| Method | GetDimension | Obsolete. Superseded by IDisplayDimension::GetDimension2 . |
| Method | GetDimension2 | Gets the model dimension used to create this display dimension. |
| Method | GetDisplayData | Gets the display data for this display dimension. |
| Method | GetExtensionLineAsCenterline | Gets whether the specified extension line is a centerline. |
| Method | GetFractionBase | Gets whether this display dimension is displayed as a decimal value or a fraction. |
| Method | GetFractionValue | Gets the largest fraction denominator to be used when this display dimension is displayed in fraction format. |
| Method | GetHoleCalloutVariables | Gets access to hole callout variables in a hole callout. |
| Method | GetJogParameters | Gets the jog in a linear dimension extension line. |
| Method | GetLinkedText | Gets the text linked to this display dimension. |
| Method | GetLowerText | Gets the text below the dimension line in a display dimension. |
| Method | GetNameForSelection | Gets the name of the selected display dimension needed by IModelDocExtension::SelectByID2 . |
| Method | GetNext | Obsolete. Superseded by IDisplayDimension::GetNext5 . |
| Method | GetNext2 | Obsolete. Superseded by IDisplayDimension::GetNext5 . |
| Method | GetNext3 | Obsolete. Superseded by IDisplayDimension::GetNext5 . |
| Method | GetNext4 | Obsolete. Superseded by IDisplayDimension::GetNext5 . |
| Method | GetNext5 | Gets the next display dimension. |
| Method | GetOrdinateDimensionArrowSize | Gets the diameter of the circle for the arrow of the base ordinate dimension. |
| Method | GetOverride | Gets whether to display the actual dimension value or to override it with another value. |
| Method | GetOverrideValue | Gets the value to display instead of the actual dimension value. |
| Method | GetPrimaryPrecision | Obsolete. Superseded by IDisplayDimension::GetPrimaryPrecision2 . |
| Method | GetPrimaryPrecision2 | Gets the primary dimension precision setting for this display dimension. |
| Method | GetPrimaryTolPrecision | Obsolete. Superseded by IDisplayDimension::GetPrimaryTolPrecision2 . |
| Method | GetPrimaryTolPrecision2 | Gets the primary tolerance precision setting for this display dimension. |
| Method | GetRoundToFraction | Gets whether the displayed dimension value is rounded off so that SOLIDWORKS can display it as a fraction. |
| Method | GetSecondArrow | Gets whether this diameter display dimension has the second arrow enabled. |
| Method | GetSupportsGenericText | Gets whether the display dimension was created in SOLIDWORKS 2011 or later, which, if so, indicates that the display dimension is generic text. |
| Method | GetText | Gets the text above the dimension line in a display dimension. |
| Method | GetTextFormat | Obsolete. Superseded by IAnnotation::GetTextFormat . |
| Method | GetTextFormatItems | Gets the format tokens of the specified text portion of a multi-value display dimension. |
| Method | GetType | Obsolete. Superseded by IDisplayDimension::Type2 . |
| Method | GetUnits | Gets the units used by this display dimension. |
| Method | GetUseDocArrowHeadStyle | Gets whether this display dimension uses the document default setting for dimension arrowhead style. |
| Method | GetUseDocBentLeaderLength | Gets whether this dimension is using the document default for bent leader length or not. |
| Method | GetUseDocBrokenLeader | Gets whether this display dimension uses the document default setting for displaying leaders as broken. |
| Method | GetUseDocDual | Gets whether this display dimension uses the document setting for positioning dual dimensions. |
| Method | GetUseDocPrecision | Obsolete. Not superseded. |
| Method | GetUseDocSecondArrow | Gets whether this diameter display dimension uses the document default setting for the display of the second outside arrow. |
| Method | GetUseDocTextFormat | Obsolete. Superseded by IAnnotation::GetUseDocTextFormat . |
| Method | GetUseDocUnits | Gets whether this display dimension uses the document default setting for units. |
| Method | GetWitnessLineGap | Gets the gap of the specified dimension extension line. |
| Method | IAddDisplayEnt | Overrides the display graphics of objects for this display dimension. |
| Method | IAddDisplayText | Overrides the display text for this display dimension. |
| Method | IGetAnnotation | Gets the IAnnotation object for this specific annotation. |
| Method | IGetDimension | Obsolete. Superseded by IDisplayDimension::GetDimension2 . |
| Method | IGetDisplayData | Gets the display data for this display dimension. |
| Method | IGetNext | Obsolete. Superseded by IDisplayDimension::GetNext5 . |
| Method | IGetNext2 | Obsolete. Superseded by IDisplayDimension::GetNext5 . |
| Method | IGetNext3 | Obsolete. Superseded by IDisplayDimension::GetNext5 . |
| Method | IGetTextFormat | Obsolete. Superseded by IAnnotation::IGetTextFormat . |
| Method | IsDimXpert | Obsolete. Superseded by IAnnotation::IsDimXpert . |
| Method | ISetTextFormat | Obsolete. Superseded by IAnnotation::ISetTextFormat . |
| Method | IsHoleCallout | Gets whether this display dimension is a hole callout. |
| Method | IsReferenceDim | Gets whether this display dimension is a reference dimension. |
| Method | ResetExtensionLineStyle | Resets the style of the specified extension line. |
| Method | SetArcLengthLeader | Sets the leader style of this arc-length dimension. |
| Method | SetArrowHeadStyle | Obsolete. Superseded by IDisplayDimension::SetArrowHeadStyle2 . |
| Method | SetArrowHeadStyle2 | Sets the arrowhead style of this display dimension. |
| Method | SetBentLeaderLength | Sets the bent leader length to use for this dimension. |
| Method | SetBrokenLeader2 | Sets the broken leader display characteristic of this display dimension. |
| Method | SetDual | Obsolete. Superseded by IDisplayDimension::SetDual2 . |
| Method | SetDual2 | Controls the display of dual dimensions of this display dimension. |
| Method | SetExtensionLineAsCenterline | Sets whether the specified extension line is a centerline. |
| Method | SetHorizontal | Displays this linear dimension on the horizontal. |
| Method | SetJogParameters | Set the linear dimension extension line to be jogged. |
| Method | SetLineFontDimensionStyle | Sets the style of leader for this display dimension. |
| Method | SetLineFontDimensionThickness | Sets the thickness of leaders of this display dimension. |
| Method | SetLineFontExtensionStyle | Sets the line font style for the extension lines of this display dimension. |
| Method | SetLineFontExtensionThickness | Sets the thickness of the extension lines of this display dimension. |
| Method | SetLinkedText | Sets the text to link to this display dimension. |
| Method | SetLowerText | Sets the text below the dimension line in a display dimension. |
| Method | SetOrdinateDimensionArrowSize | Sets the diameter of the circle for the arrow of the base ordinate dimension if the base ordinate dimension standard is set to DIN. |
| Method | SetOverride | Sets whether to display the actual dimension value or to display another value, and, if so, that value. |
| Method | SetPrecision | Obsolete. Superseded by IDisplayDimension::SetPrecision2 . |
| Method | SetPrecision2 | Obsolete. Superseded by IDisplayDimension::SetPrecision3 . |
| Method | SetPrecision3 | Sets the number of digits to display after the decimal point for precision and tolerance values in this display dimension. |
| Method | SetSecondArrow | Sets the second arrow characteristics of this diameter display dimension. |
| Method | SetText | Sets the text above the dimension line in a display dimension. |
| Method | SetTextFormat | Obsolete. Superseded by IAnnotation::ISetTextFormat . |
| Method | SetUnits | Obsolete. Superseded by IDisplayDimension::SetUnits2 . |
| Method | SetUnits2 | Sets the unit display characteristics of this display dimension. |
| Method | SetVertical | Displays this linear dimension on the vertical. |
| Method | SetWitnessLineGap | Sets the gap for the specified dimension extension line. |
| Method | SupplementaryAngle | Changes the angle in the selected angular dimension to its supplementary angle. |
| Method | Unlink | Unlinks a previously linked display dimension. |
| Method | VerticallyOppositeAngle | Flips an angular dimension to its vertically opposite angle. |

[Top](#topBookmark)

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html)

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.html)
