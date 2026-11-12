---
title: "GetCompoundTextAtIndex Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetCompoundTextAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetCompoundTextAtIndex.html"
---

# GetCompoundTextAtIndex Method (INote)

Obsolete for documents created in SOLIDWORKS 2016 and later. Gets the text item corresponding to the specified index from a compound note.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCompoundTextAtIndex( _
   ByVal Index As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim Index As System.Integer
Dim value As System.String

value = instance.GetCompoundTextAtIndex(Index)
```

### C#

```csharp
System.string GetCompoundTextAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.String^ GetCompoundTextAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the text item in the compound note; index is 1-based

### Return Value

Text corresponding to specified index

## VBA Syntax

See [Note::GetCompoundTextAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Note~GetCompoundTextAtIndex.html).

## Remarks

Before calling this method, call [INote::GetCompoundTextCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetCompoundTextCount.html) to get the number of text items.

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
[INote::IGetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextOffsetAtIndex.html)
[INote::IsCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsCompoundNote.html)
[INote::SetTextJustificationAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextJustificationAtIndex.html)
[INote::SetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextOffsetAtIndex.html)
[INote::SetTextPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextPoint.html)
[INote::SetZeroLengthLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetZeroLengthLeader.html)
[INote::GetHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHeight.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
