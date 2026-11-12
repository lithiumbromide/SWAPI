---
title: "GetCompoundTextCount Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetCompoundTextCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetCompoundTextCount.html"
---

# GetCompoundTextCount Method (INote)

Obsolete for documents created in SOLIDWORKS 2016 and later. Gets the number of text items in a compound note.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCompoundTextCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Integer

value = instance.GetCompoundTextCount()
```

### C#

```csharp
System.int GetCompoundTextCount()
```

### C++/CLI

```cpp
System.int GetCompoundTextCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of text items in a compound note

## VBA Syntax

See [Note::GetCompoundTextCount](ms-its:sldworksapivb6.chm::/sldworks~Note~GetCompoundTextCount.html).

## Remarks

Use this method before using any of the following methods:

- [INote::GetCompoundTextAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetCompoundTextAtIndex.html)
- [INote::GetTextOffsetAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetTextOffsetAtIndex.html) and [INote::IGetTextOffsetAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~IGetTextOffsetAtIndex.html)
- [INote::GetTextJustificationAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetTextJustificationAtIndex.html)

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::AddText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~AddText.html)
[INote::BeginSketchEdit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~BeginSketchEdit.html)
[INote::EndSketchEdit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~EndSketchEdit.html)
[INote::GetExtent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetExtent.html)
[INote::GetExtentAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetExtentAtIndex.html)
[INote::GetSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetSketch.html)
[INote::GetTextJustificationAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextJustificationAtIndex.html)
[INote::GetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextOffsetAtIndex.html)
[INote::IGetExtent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetExtent.html)
[INote::IGetExtentAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetExtentAtIndex.html)
[INote::IGetSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetSketch.html)
[INote::IsCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsCompoundNote.html)
[INote::SetTextJustificationAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextJustificationAtIndex.html)
[INote::SetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextOffsetAtIndex.html)
[INote::SetTextPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextPoint.html)
[INote::SetZeroLengthLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetZeroLengthLeader.html)
[INote::GetHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHeightAtIndex.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
