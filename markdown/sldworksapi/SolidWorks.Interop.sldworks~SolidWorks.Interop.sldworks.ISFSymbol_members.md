---
title: "ISFSymbol Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html"
---

# ISFSymbol Interface Members

The following tables list the members exposed by [ISFSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | GOSTDefaultSymbol | Gets whether the GOST Add default symbol option is set. |
| Property | GOSTNotation | Gets whether the GOST Use for notation option is set. |
| Property | Grinding | Obsolete. Superseded by ISFSymbol::GetSymbolSurfaceTexture . |
| Property | Orientation | Gets whether the orientation of this surface finish symbol is relative to the model or entity to which it is attached. |
| Property | ProfileAngle | Gets or sets the profile angle of this surface finish symbol. |
| Property | ProfileDirection | Gets or sets the profile direction of this surface finish symbol. |
| Property | Rotated | Obsolete. Superseded by ISFSymbol::Orientation . |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetAngle | Gets the angle of this surface finish symbol. |
| Method | GetAnnotation | Gets the annotation for this surface finish symbol. |
| Method | GetArcAtIndex | Gets information for the specified arc. |
| Method | GetArcCount | Gets the number of arcs in this surface finish symbol. |
| Method | GetArrowHeadAtIndex | Gets information on the specified arrow head in this surface finish symbol. |
| Method | GetArrowHeadCount | Gets the number of arrow heads in the surface finish symbol. |
| Method | GetArrowHeadInfo | Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line. |
| Method | GetDirectionOfLay | Gets the direction of lay value for this surface finish symbol. |
| Method | GetLeaderAtIndex | Gets information about the specified leader on this surface finish symbol. |
| Method | GetLeaderCount | Gets the number of leaders on this surface finish symbol. |
| Method | GetLineAtIndex | Gets information for the specified line. |
| Method | GetLineCount | Gets number of line items in this surface finish symbol. |
| Method | GetNext | Gets the next surface finish symbol in the view. |
| Method | GetSymbol | Gets the type of symbol for this surface finish symbol. |
| Method | GetSymbolAllAround | Gets whether this symbol is All Around or Local for this surface finish symbol. |
| Method | GetSymbolSurfaceTexture | Gets the symbol surface texture type for this surface finish symbol. |
| Method | GetSymbolType | Obsolete. Superseded by ISFSymbol::GetSymbol . |
| Method | GetText | Gets the specified text string in this surface finish symbol. |
| Method | GetTextAngleAtIndex | Gets the text angle for the specified text in this surface finish symbol. |
| Method | GetTextAtIndex | Gets the specified text string from this surface finish symbol. |
| Method | GetTextCount | Gets the number of text items in the surface finish symbol. |
| Method | GetTextFontAtIndex | Gets the font used by the specified text item in this surface finish symbol. |
| Method | GetTextHeightAtIndex | Gets the text height for the specified piece of text in this surface finish symbol. |
| Method | GetTextInvertAtIndex | Gets the specified text item's invert flag. |
| Method | GetTextPositionAtIndex | Gets the text item's offset relative to note's text point. |
| Method | GetTextRefPositionAtIndex | Gets the specified text item's reference position in this note, for example, upper left, lower left, center, and so on. |
| Method | GetTriangleAtIndex | Gets the triangle at the specified index. |
| Method | GetTriangleCount | Gets the number of triangles in this surface finish symbol. |
| Method | HasExtraLeader | Gets whether this surface finish symbol has an extra leader line. |
| Method | IGetAnnotation | Gets the annotation for this surface finish symbol. |
| Method | IGetArcAtIndex | Gets information for the specified arc. |
| Method | IGetArrowHeadAtIndex | Gets information on the specified arrow head in this surface finish symbol. |
| Method | IGetArrowHeadInfo | Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line. |
| Method | IGetLeaderAtIndex | Gets information about the specified leader on this surface finish symbol. |
| Method | IGetLineAtIndex | Gets information for the specified line. |
| Method | IGetNext | Gets the next surface finish symbol in the view. |
| Method | IGetTextPositionAtIndex | Gets the text item's offset relative to note's text point. |
| Method | IGetTriangleAtIndex | Gets the triangle at the specified index. |
| Method | IsAttached | Gets whether the leader line for this surface finish symbol is attached. |
| Method | SetAngle | Sets the angle for this surface finish symbol. |
| Method | SetDirectionOfLay | Sets the direction of lay value for this surface finish symbol. |
| Method | SetSymbol | Sets the type of symbol for this surface finish symbol. |
| Method | SetSymbolType | Obsolete. Superseded by ISFSymbol::SetSymbol . |
| Method | SetText | Sets a text string in this surface finish symbol. |

[Top](#topBookmark)

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
