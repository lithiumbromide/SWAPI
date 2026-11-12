---
title: "INote Interface Members"
project: "SOLIDWORKS API Help"
interface: "INote_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html"
---

# INote Interface Members

The following tables list the members exposed by [INote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AllUpperCase | Gets or sets whether the text of this note is all uppercase. |
| Property | Angle | Controls the rotation angle of this note. |
| Property | BehindSheet | Places this note, located on the sheet format in a drawing, behind the drawing sheet. |
| Property | HasMultipleFonts | Gets whether a note contains multiple fonts. |
| Property | IncludeDimPrefixSuffixTolerance | Gets or sets whether to include the dimension prefix, suffix, and tolerance in this dimension note. |
| Property | IsBendLineNote | Gets whether this note is a bendline note. |
| Property | LockPosition | Gets and sets whether to anchor this note. |
| Property | PromptText | Gets and sets the message prompt text. |
| Property | PropertyLinkedText | Gets or sets the text for the note using the values of the properties linked to the note. |
| Property | ReadOnly | Gets or sets the read-only state of a note. |
| Property | TagName | Gets or sets the tag name for this note. |
| Property | TextRightToLeft | Gets or sets whether notes are displayed right to left. |
| Property | ToBoundingBox | Gets and sets whether to select the To bounding box option for leaders in this note's PropertyManager page. |
| Property | Visible | Gets and sets the visibility state of a note during the creation of a block. |
| Property | WatermarkBehindGeometry | Gets or sets whether to place this note, specified to be a watermark, behind the geometry in a part or assembly. |
| Property | WatermarkNote | Gets or sets whether the note is a watermark in a part or assembly. |
| Property | WatermarkTransparencyLevel | Gets or sets the transparency level of a note specified to be a watermark. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddText | Obsolete for documents created in SOLIDWORKS 2016 and later. Adds text to the selected compound note. |
| Method | BeginSketchEdit | Obsolete for documents created in SOLIDWORKS 2016 and later . Activates the sketch of the compound note . |
| Method | EndSketchEdit | Obsolete for documents created in SOLIDWORKS 2016 and later . Finishes accessing this compound note's sketch. |
| Method | GetAnnotation | Gets the annotation for this specific note. |
| Method | GetArcAtIndex | Gets information for the specified arc in this note. |
| Method | GetArcCount | Gets the number of arcs in the note. |
| Method | GetArrowHeadAtIndex | Gets information on the specified arrowhead in this note. |
| Method | GetArrowHeadCount | Gets the number of arrowheads in the note. |
| Method | GetArrowHeadInfo | Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line. |
| Method | GetAttachPos | Gets the attachment point of this note. |
| Method | GetBalloonInfo | Gets information describing the geometry of the balloon, if any, that encloses the note text. |
| Method | GetBalloonOptions | Gets the balloon options for this note. |
| Method | GetBalloonPadding | Gets the balloon padding of this note. |
| Method | GetBalloonSize | Gets the balloon size or fit of this note. |
| Method | GetBalloonStack | Gets the balloon stack for this balloon note. |
| Method | GetBalloonStyle | Gets the balloon style of this note. |
| Method | GetBendLineValues | Obsolete. Superseded by INote::GetBendLineValues2 . |
| Method | GetBendLineValues2 | Gets the values of a bend line note. |
| Method | GetBomBalloonText | Gets the text for this BOM balloon note. |
| Method | GetBomBalloonTextStyle | Gets the text style of this BOM balloon note. |
| Method | GetCompoundTextAtIndex | Obsolete for documents created in SOLIDWORKS 2016 and later . Gets the text item corresponding to the specified index from a compound note. |
| Method | GetCompoundTextCount | Obsolete for documents created in SOLIDWORKS 2016 and later . Gets the number of text items in a compound note. |
| Method | GetExtent | Gets the extents of a note in sheet space. |
| Method | GetExtentAtIndex | Obsolete for documents created in SOLIDWORKS 2016 and later . Gets the extents of the specified piece of text within a compound note. |
| Method | GetFontInfo | Gets with the note's font information. |
| Method | GetHeight | Get the note's height. |
| Method | GetHeightAtIndex | Obsolete for documents created in SOLIDWORKS 2016 and later . Gets the specified text item's height in a compound note. |
| Method | GetHeightInPoints | Gets the height of this note in points (for example, 8, 10, 12, and so on). |
| Method | GetHyperlinkText | Gets the hyperlink in a note. |
| Method | GetLeaderAtIndex | Gets information about the specified leader on this note. |
| Method | GetLeaderCount | Gets the number of leaders on this note. |
| Method | GetLeaderInfo | Gets information describing the layout of the note leader lines. |
| Method | GetLeaderNumPointsAt | Gets the number of points in the specified leader of this note. |
| Method | GetLineAtIndex | Gets information for the specified line. |
| Method | GetLineCount | Gets the number of line segments in this note. |
| Method | GetName | Gets the name of this note. |
| Method | GetNext | Gets the next note in drawing view . |
| Method | GetSketch | Obsolete for documents created in SOLIDWORKS 2016 and later . Gets the sketch for the current compound note. |
| Method | GetText | Gets this note's text. |
| Method | GetTextAngleAtIndex | Gets the text angle for the specified piece of text in this note. |
| Method | GetTextAtIndex | Gets the specified text in this note. |
| Method | GetTextCount | Gets the number of text items in this note. |
| Method | GetTextFontAtIndex | Gets the font used by the specified text item in this note. |
| Method | GetTextFormat | Obsolete. Superseded by IAnnotation::GetTextFormat and IAnnotation::IGetTextFormat . |
| Method | GetTextFormatAtIndex | Obsolete. Superseded by IAnnotation::GetTextFormat and IAnnotation::IGetTextFormat . |
| Method | GetTextHeightAtIndex | Gets the text height for the specified piece of text in this note. |
| Method | GetTextInvertAtIndex | Gets the specified text item's invert flag. |
| Method | GetTextJustification | Gets the text justification of a standard note. |
| Method | GetTextJustificationAtIndex | Obsolete for documents created in SOLIDWORKS 2016 and later . Gets the text justification for the specified text item in a compound note. |
| Method | GetTextLineSpacingAtIndex | Gets the line spacing for this note. |
| Method | GetTextOffsetAtIndex | Obsolete for documents created in SOLIDWORKS 2016 and later . Gets the text item's offset relative to note's text point in a compound note. |
| Method | GetTextPoint | Obsolete. Superseded by INote::GetTextPoint2 or INote::IGetTextPoint2 . |
| Method | GetTextPoint2 | Gets the note's text reference point (i.e., note origin). |
| Method | GetTextPositionAtIndex | Gets the text item's offset relative to the document origin. |
| Method | GetTextRefPositionAtIndex | Gets the specified text item's reference position in this note; for example, the upper left, lower left, or center. |
| Method | GetTextVerticalJustification | Gets the vertical justification of a standard note. |
| Method | GetTriangleAtIndex | Gets the triangle at the specified index. |
| Method | GetTriangleCount | Gets the number of triangles in this note. |
| Method | GetUpperRight | Gets the note's upper-right text point. |
| Method | GetUseDocTextFormat | Obsolete. Superseded by IAnnotation::GetUseDocTextFormat . |
| Method | HasBalloon | Gets whether this note has a balloon. |
| Method | HasExtraLeader | Gets whether this note has a bent or straight leaderline. |
| Method | IGetAnnotation | Gets the annotation for this specific note. |
| Method | IGetArcAtIndex | Gets information for the specified arc in this note. |
| Method | IGetArrowHeadAtIndex | Gets information on the specified arrowhead in this note. |
| Method | IGetArrowHeadInfo | Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line. |
| Method | IGetAttachPos | Gets the attachment point of this note. |
| Method | IGetBalloonInfo | Gets information describing the geometry of the balloon, if any, that encloses the note text. |
| Method | IGetExtent | Gets the extents of a note in sheet space. |
| Method | IGetExtentAtIndex | Obsolete for documents created in SOLIDWORKS 2016 and later . Gets the extents of the specified piece of text within a compound note. |
| Method | IGetFontInfo | Gets with the note's font information. |
| Method | IGetLeaderAtIndex | Gets information about the specified leader on this note. |
| Method | IGetLeaderInfo | Gets information describing the layout of the note leader lines. |
| Method | IGetLineAtIndex | Gets information for the specified line. |
| Method | IGetNext | Gets the next note in drawing view . |
| Method | IGetSketch | Obsolete for documents created in SOLIDWORKS 2016 and later . Gets the sketch for the current compound note. |
| Method | IGetTextFormat | Obsolete. Superseded by IAnnotation::GetTextFormat and IAnnotation::IGetTextFormat . |
| Method | IGetTextFormatAtIndex | Obsolete. Superseded by IAnnotation::GetTextFormat and IAnnotation::GetTextFormat . |
| Method | IGetTextOffsetAtIndex | Obsolete for documents created in SOLIDWORKS 2016 and later . Gets whether the text item's offset relative to note's text point in a compound note. |
| Method | IGetTextPoint | Obsolete. Superseded by INote::IGetTextPoint . |
| Method | IGetTextPoint2 | Gets the note's text reference point (i.e., note origin). |
| Method | IGetTextPositionAtIndex | Gets the text item's offset relative to the document origin. |
| Method | IGetTriangleAtIndex | Gets the triangle at the specified index. |
| Method | IGetUpperRight | Gets the note's upper-right text point. |
| Method | IsAttached | Gets whether the note is attached. |
| Method | IsAttribute | Obsolete. Not superseded. |
| Method | IsBomBalloon | Gets whether this note has a BOM balloon. |
| Method | IsCompoundNote | Obsolete for documents created in SOLIDWORKS 2016 and later . Gets whether the current note is a compound note. |
| Method | ISetTextFormat | Obsolete. Superseded by IAnnotation::SetTextFormat and IAnnotation::ISetTextFormat . |
| Method | ISetTextFormatAtIndex | Obsolete. Superseded by IAnnotation::SetTextFormat and IAnnotation::ISetTextFormat . |
| Method | IsStackedBalloon | Gets whether this note is part of a stacked balloon. |
| Method | IsStackedBalloonMaster | Gets whether this note is the master note of a balloon stack. |
| Method | MakeStackedBalloon | Converts this balloon to a stacked balloon. |
| Method | SetBalloon | Sets the balloon style, size, and fit for this note. |
| Method | SetBalloonPadding | Sets the padding for this balloon note. |
| Method | SetBomBalloonText | Sets the text for this BOM balloon note. |
| Method | SetHeight | Sets the height of this note in meters. |
| Method | SetHeightInPoints | Sets the height of this note in points (for example, 8, 10, 12, and so on). |
| Method | SetHyperlinkText | Sets the hyperlink in a note. |
| Method | SetName | Sets the name for this note. |
| Method | SetText | Sets the text of the note. |
| Method | SetTextAtIndex | Obsolete for documents created in SOLIDWORKS 2016 and later . Sets the text value at the specified index within the compound note. |
| Method | SetTextFormat | Obsolete. Superseded by IAnnotation::SetTextFormat and IAnnotation::ISetTextFormat . |
| Method | SetTextFormatAtIndex | Obsolete. Superseded by IAnnotation::SetTextFormat and IAnnotation::ISetTextFormat . |
| Method | SetTextJustification | Sets the text justification of a standard note. |
| Method | SetTextJustificationAtIndex | Obsolete for documents created in SOLIDWORKS 2016 and later . Sets the text justification for the specified text item in a compound note. |
| Method | SetTextOffsetAtIndex | Obsolete for documents created in SOLIDWORKS 2016 and later . Relocates the offset (origin) of the specified piece of text in a compound note. |
| Method | SetTextPoint | Relocates the note origin to the specified location. |
| Method | SetTextVerticalJustification | Sets the vertical justification of a standard note. |
| Method | SetZeroLengthLeader | Obsolete for documents created in SOLIDWORKS 2016 and later . Sets a 0-length leader for a compound note. |

[Top](#topBookmark)

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelDoc2::InsertNewNote3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertNewNote3.html)
[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
