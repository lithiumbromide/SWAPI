---
title: "GetHeightAtIndex Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetHeightAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHeightAtIndex.html"
---

# GetHeightAtIndex Method (INote)

Obsolete for documents created in SOLIDWORKS 2016 and later. Gets the specified text item's height in a compound note.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHeightAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim Index As System.Integer
Dim value As System.Double

value = instance.GetHeightAtIndex(Index)
```

### C#

```csharp
System.double GetHeightAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double GetHeightAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index position of the text

### Return Value

Text height

## VBA Syntax

See [Note::GetHeightAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Note~GetHeightAtIndex.html).

## Examples

[Create Compound Note (VBA)](Create_Compound_Note_Example_VB.htm)

## Remarks

Because a compound note can have multiple pieces of text, many of the compound note methods require you to specify the index value of the desired text. For example, the first piece of text added to the compound note using [INote::AddText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~AddText.html) has an index number of 1, the second text added has index number of 2, and so on.

If you use this method on a standard note (not a compound note), then the index value must be set to 1.

To set the specified text's height, use [IAnnotation::SetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~SetTextFormat.html) or [IAnnotation::ISetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~ISetTextFormat.html).

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
[INote::GetSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetSketch.html)
[INote::IGetExtent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetExtent.html)
[INote::IGetExtentAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetExtentAtIndex.html)
[INote::IGetSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetSketch.html)
[INote::IsCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsCompoundNote.html)
[INote::SetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextAtIndex.html)
[INote::SetTextJustificationAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextJustificationAtIndex.html)
[INote::SetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextOffsetAtIndex.html)
[INote::SetTextPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextPoint.html)
[INote::SetZeroLengthLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetZeroLengthLeader.html)
[INote::SetHeightInPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetHeightInPoints.html)
[INote::SetHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetHeight.html)
[INote::GetHeightInPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHeightInPoints.html)
[INote::GetHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHeight.html)
