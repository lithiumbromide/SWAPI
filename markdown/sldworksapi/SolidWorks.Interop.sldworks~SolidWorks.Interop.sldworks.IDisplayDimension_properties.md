---
title: "IDisplayDimension Interface Properties"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension_properties"
member: ""
kind: "properties"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_properties.html"
---

# IDisplayDimension Interface Properties

For a list of all members of this type, see [IDisplayDimension members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html).

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

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html)
[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.html)
