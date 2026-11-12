---
title: "IGtol Interface Methods"
project: "SOLIDWORKS API Help"
interface: "IGtol_methods"
member: ""
kind: "methods"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_methods.html"
---

# IGtol Interface Methods

For a list of all members of this type, see [IGtol members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddFrame | Adds a frame at the end of the list of this Gtol's frames. |
| Method | CanConvertFormat | Gets whether this Gtol can be converted to the current format. |
| Method | ConvertFormat | Converts this Gtol to the current format. |
| Method | DeleteBelowFrameTextAt | Deletes the specified text line in the below frame of this GTol. |
| Method | DeleteFrame | Deletes the specified frame from this Gtol. |
| Method | GetAllAround | Gets whether this GTol uses an All Around leader. |
| Method | GetAllAroundThisSide | Gets whether this GTol uses an All Around This Side leader. |
| Method | GetAllOver | Gets whether this GTol uses an All Over leader. |
| Method | GetAllOverThisSide | Gets whether this GTol uses an All Over This Side leader. |
| Method | GetAnnotation | Gets the annotation for this specific Gtol. |
| Method | GetArcAtIndex | Gets information about the specified arc. |
| Method | GetArcCount | Gets the number of arcs in this GTol. |
| Method | GetArrowHeadAtIndex | Gets information on the specified arrow head in this GTol. |
| Method | GetArrowHeadCount | Gets the number of arrow heads in the GTol. |
| Method | GetArrowHeadInfo | Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line. |
| Method | GetAttachPos | Gets the attachment point of the GTol. |
| Method | GetBelowFrameTextAt | Gets the specified line of text in this GTol. |
| Method | GetBelowFrameTextLineCount | Gets the number of text lines in the below frame of this GTol. |
| Method | GetBetweenTwoPoints | Gets whether the between two points symbol is being used. |
| Method | GetBetweenTwoPointsText | Gets the text used in the between two points symbol. |
| Method | GetCompositeFrame | Obsolete. Superseded by IGtol::GetCompositeFrame2 . |
| Method | GetCompositeFrame2 | Gets whether the GTol frame with the specified index is part of a composite frame. |
| Method | GetDatumIdentifier | Gets the datum identifier. |
| Method | GetDisplayDualDimensionInRangeValues | Gets whether to display dual units in dimension range values. |
| Method | GetFontInfo | Gets with the font information for this GTol. |
| Method | GetFormat | Gets the format type of this Gtol. |
| Method | GetFrame | Gets the Gtol frame at the specified index. |
| Method | GetFrameCount | Gets the number of frames in this GTol symbol. |
| Method | GetFrameDiameterSymbols | Gets whether diameter symbols are displayed for the specified frame. |
| Method | GetFrameSymbols | Obsolete. Superseded by IGtol::GetFrameSymbols2 . |
| Method | GetFrameSymbols2 | Obsolete. Superseded by IGtol::GetFrameSymbols3 . |
| Method | GetFrameSymbols3 | Gets the symbols for the specified frame. |
| Method | GetFrameValues | Gets an array that describes the text that appears in each of the fields of the specified GTol frame. |
| Method | GetFromTo | Gets whether the From-To symbol is present in this Gtol. |
| Method | GetFromToText | Gets the From-To text of this Gtol. |
| Method | GetHeight | Gets the GTol height. |
| Method | GetLeaderAtIndex | Obsolete. Superseded by IGtol::GetLeaderAtIndex2 . |
| Method | GetLeaderAtIndex2 | Gets information about the specified leader on this GTol. |
| Method | GetLeaderCount | Gets the number of leaders on this GTol. |
| Method | GetLeaderInfo | Gets information describing the layout of the GTol leader lines. |
| Method | GetLeaderSide | Gets where the leader attaches to the symbol. |
| Method | GetLineAtIndex | Gets the start and end information for the specified line. |
| Method | GetLineCount | Gets the number of linea in this GTol. |
| Method | GetNextGTOL | Gets the next GTol. |
| Method | GetPTZHeight | Obsolete. Superseded by IGtol::GetPTZHeight2 . |
| Method | GetPTZHeight2 | Gets the projected tolerance zone for the specified frame and tolerance in this GTol. |
| Method | GetSymArcs | Gets an array that defines all arcs in the symbol. |
| Method | GetSymCircles | Gets an array that defines all circles in the symbol. |
| Method | GetSymDesc | Gets the specified symbol description. |
| Method | GetSymEdgeCounts | Gets an array of the number of lines, arcs and circles in the specified symbol. |
| Method | GetSymLines | Gets an array that defines all lines in the symbol. |
| Method | GetSymName | Gets the symbol name based on the specified index number that SOLIDWORKS uses to identify the symbol. |
| Method | GetSymText | Gets the symbol text. |
| Method | GetSymTextPoints | Gets the text points for the specified symbol. |
| Method | GetText | Gets the specified text part of this GTol. |
| Method | GetTextAngleAtIndex | Gets the text angle for the specified piece of text in this GTol. |
| Method | GetTextAtIndex | Gets the specified text from this GTol. |
| Method | GetTextCount | Gets the number of text items in the GTol. |
| Method | GetTextFont | Gets the font for this GTol. |
| Method | GetTextFormat | Obsolete. Superseded by IAnnotation::GetTextFormat . |
| Method | GetTextHeightAtIndex | Gets the text height for the specified piece of text in this GTol. |
| Method | GetTextInvertAtIndex | Gets the specified text item's invert flag. |
| Method | GetTextPoint | Gets the GTol text reference point, which is the upper-left corner of the bounding rectangle. |
| Method | GetTextPositionAtIndex | Gets the text item's offset relative to note's text point. |
| Method | GetTextRefPositionAtIndex | Gets the reference position for the specified text item in this GTol (for example, upper-left, lower-left, center). |
| Method | GetTriangleAtIndex | Gets the triangle at the specified index. |
| Method | GetTriangleCount | Gets the number of triangles in this GTol. |
| Method | GetUseDocTextFormat | Obsolete. Superseded by IAnnotation::GetUseDocTextFormat . |
| Method | GetWitnessLine | Gets the extension line that connects the leader of this geometric tolerance with the entity being dimensioned. |
| Method | HasExtraLeader | Gets whether the GTol has a bent leaderline or a straight leaderline. |
| Method | IGetAnnotation | Gets the annotation for this specific GTol. |
| Method | IGetArcAtIndex | Gets information for the specified arc. |
| Method | IGetArrowHeadAtIndex | Gets information on the specified arrow head in this GTol. |
| Method | IGetArrowHeadInfo | Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line. |
| Method | IGetAttachPos | Gets the attachment point of the GTol. |
| Method | IGetFontInfo | Gets with the font information for this GTol. |
| Method | IGetFrameDiameterSymbols | Gets whether diameter symbols are displayed for the specified frame. |
| Method | IGetFrameSymbols | Obsolete. Superseded by IGtol::IGetFrameSymbols2 . |
| Method | IGetFrameSymbols2 | Obsolete. Superseded by IGtol::GetFrameSymbols3 . |
| Method | IGetFrameValues | Gets an array that describes the text that appears in each of the fields of the specified GTol frame. |
| Method | IGetLeaderAtIndex | Obsolete. Superseded by IGtol::IGetLeaderAtIndex2 . |
| Method | IGetLeaderAtIndex2 | Gets information about the specified leader on this GTol. |
| Method | IGetLeaderInfo | Gets information describing the layout of the GTol leader lines. |
| Method | IGetLineAtIndex | Gets the start and end information for the specified line. |
| Method | IGetNextGTOL | Gets the next GTol. |
| Method | IGetSymArcs | Gets an array that defines all arcs in the symbol. |
| Method | IGetSymCircles | Gets an array that defines all circles in the symbol. |
| Method | IGetSymEdgeCounts | Gets an array of the number of lines, arcs and circles in the specified symbol. |
| Method | IGetSymLines | Gets an array that defines all lines in the symbol. |
| Method | IGetSymText | Gets the symbol text. |
| Method | IGetSymTextPoints | Gets the text points for the specified symbol. |
| Method | IGetTextFormat | Obsolete. Superseded by IAnnotation::IGetTextFormat . |
| Method | IGetTextPoint | Gets the GTol text reference point, which is the upper-left corner of the bounding rectangle. |
| Method | IGetTextPositionAtIndex | Gets the reference position for the specified text item in this GTol (for example, upper-left, lower-left, center). |
| Method | IGetTriangleAtIndex | Gets the triangle at the specified index. |
| Method | IGetWitnessLine | Gets the extension line that connects the leader of this geometric tolerance with the entity that is being dimensioned. |
| Method | InsertBelowFrameTextAt | Inserts the specified text at the specified line index in the below frame of this GTol. |
| Method | IsAttached | Gets whether this GTol is attached. |
| Method | ISetTextFormat | Obsolete. Superseded by IAnnotation::ISetTextFormat . |
| Method | SetAllAroundThisSide | Sets whether this GTol uses an All Around This Side leader. |
| Method | SetAllOver | Sets whether this Gtol uses an All Over leader. |
| Method | SetAllOverThisSide | Sets whether this Gtol uses an All Over This Side leader. |
| Method | SetBelowFrameTextAt | Edits or inserts a text line at the specified below frame line index of this GTol. |
| Method | SetBetweenTwoPoints | Enables or disables the between two points symbol and its texts. |
| Method | SetCompositeFrame | Obsolete. Superseded by IGtol::SetCompositeFrame2 . |
| Method | SetCompositeFrame2 | Sets whether to create a composite frame containing the specified GTol frame. |
| Method | SetDatumIdentifier | Sets the name of the datum being defined. |
| Method | SetDisplayDualDimensionInRangeValues | Sets whether to display dual units in dimension range values. |
| Method | SetFrameSymbols | Obsolete. Superseded by IGtol::SetFrameSymbols2 . |
| Method | SetFrameSymbols2 | Sets the symbols for the specified frame. |
| Method | SetFrameValues | Obsolete. Superseded by IGtol::SetFrameValues2 . |
| Method | SetFrameValues2 | Sets the geometric tolerance values and datum references in the specified frame of this GTol symbol. |
| Method | SetFromToText | Adds a From-To symbol and sets the From-To text for this Gtol. |
| Method | SetLeader | Sets the characteristics of the leader for this symbol. |
| Method | SetPosition | Sets the position of this GTol. |
| Method | SetPTZHeight | Obsolete. Superseded by IGtol::SetPTZHeight2 . |
| Method | SetPTZHeight2 | Sets the projected tolerance zone for the specified frame and tolerance in this GTol. |
| Method | SetText | Sets the specified text part of this GTol. |
| Method | SetTextFormat | Obsolete. Superseded by IAnnotation::SetTextFormat . |

[Top](#topBookmark)

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IModelDoc2::InsertGtol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertGtol.html)
