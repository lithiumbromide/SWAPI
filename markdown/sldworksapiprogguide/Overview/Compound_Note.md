---
title: "Compound Note"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Compound_Note.htm"
---

# Compound Note

In SOLIDWORKS 2015 and earlier, you could create compound notes. A compound note was a note that contained multiple text strings and sketch geometry. The compound note entities appeared to the end-user as though they were one item. If the user selected the compound note and dragged it, all of the entities and text moved together.

As of SOLIDWORKS 2016, compound notes cannot be created either in the SOLIDWORKS user interface or through the SOLIDWORKS API. For documents created with SOLIDWORKS 2016 and later, instead of creating compound notes you can create sketch blocks that function like compound notes using ISketchBlockDefinition and ISketchBlockInstance. See [Block Definitions and Block Instances](Block_Definitions_and_Block_Instances.htm).

For documents created with SOLIDWORKS 2015 or earlier, you can use the following APIs to create and/or modify compound notes:

**IAnnotation methods**

- [IAnnotation::GetTextFormat](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IAnnotation~GetTextFormat.html)
- [IAnnotation::GetTextFormatCount](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IAnnotation~GetTextFormatCount.html)
- [IAnnotation::GetUseDocTextFormat](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IAnnotation~GetUseDocTextFormat.html)
- [IAnnotation::SetTextFormat](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IAnnotation~SetTextFormat.html)

**IDrawingDoc methods**

- [IDrawingDoc::CreateCompoundNote](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IDrawingDoc~CreateCompoundNote.html)

**INote methods**

- [INote::BeginSketchEdit](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.INote~BeginSketchEdit.html)
- [INote::EndSketchEdit](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.INote~EndSketchEdit.html)
- [INote::GetCompoundTextAtIndex](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.INote~GetCompoundTextAtIndex.html)
- [INote::GetCompoundTextCount](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.INote~GetCompoundTextCount.html)
- [INote::GetExtent](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.INote~GetExtent.html)
- [INote::GetExtentAtIndex](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.INote~GetExtentAtIndex.html)
- [INote::GetHeightAtIndex](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.INote~GetHeightAtIndex.html)
- [INote::GetSketch](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.INote~GetSketch.html)
- [INote::GetTextAtIndex](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.INote~GetTextAtIndex.html)
- [INote::GetTextJustification](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.INote~GetTextJustification.html)
- [INote::GetTextJustificationAtIndex](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.INote~GetTextJustificationAtIndex.html)
- [INote::GetTextOffsetAtIndex](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.INote~GetTextOffsetAtIndex.html)
- [INote::IsCompoundNote](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.INote~IsCompoundNote.html)
- [INote::SetTextAtIndex](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.INote~SetTextAtIndex.html)
- [INote::SetTextJustificationAtIndex](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.INote~SetTextJustificationAtIndex.html)
- [INote::SetTextOffsetAtIndex](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.INote~SetTextOffsetAtIndex.html)
- [INote::SetTextPoint](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.INote~SetTextPoint.html)
- [INote::SetZeroLengthLeader](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.INote~SetZeroLengthLeader.html)
