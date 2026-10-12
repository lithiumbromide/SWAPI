---
title: "IGetSketch Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "IGetSketch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetSketch.html"
---

# IGetSketch Method (INote)

Obsolete for documents created in SOLIDWORKS 2016 and later. Gets the sketch for the current compound note.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSketch() As Sketch
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As Sketch

value = instance.IGetSketch()
```

### C#

```csharp
Sketch IGetSketch()
```

### C++/CLI

```cpp
Sketch^ IGetSketch();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html) for this compound note

## VBA Syntax

See [Note::IGetSketch](ms-its:sldworksapivb6.chm::/sldworks~Note~IGetSketch.html).

## Remarks

If the current note is not a compound note, then a NULL value is returned.

For adding or modifying actual sketch geometry in a compound note, use [INote::BeginSketchEdit](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~BeginSketchEdit.html), which activates the sketch of the compound note for modification.

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::AddText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~AddText.html)
[INote::BeginSketchEdit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~BeginSketchEdit.html)
[INote::EndSketchEdit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~EndSketchEdit.html)
[INote::GetCompoundTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetCompoundTextAtIndex.html)
[INote::GetCompoundTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetCompoundTextCount.html)
[INote::GetExtent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetExtent.html)
[INote::GetExtentAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetExtentAtIndex.html)
[INote::GetHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHeightAtIndex.html)
[INote::GetTextJustificationAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextJustificationAtIndex.html)
[INote::GetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextOffsetAtIndex.html)
[INote::IGetExtent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetExtent.html)
[INote::IGetExtentAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetExtentAtIndex.html)
[INote::IGetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextOffsetAtIndex.html)
[INote::IsCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsCompoundNote.html)
[INote::SetTextJustificationAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextJustificationAtIndex.html)
[INote::SetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextOffsetAtIndex.html)
[INote::SetTextPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextPoint.html)
[INote::SetZeroLengthLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetZeroLengthLeader.html)
