---
title: "GetTextRefPositionAtIndex Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetTextRefPositionAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextRefPositionAtIndex.html"
---

# GetTextRefPositionAtIndex Method (INote)

Gets the specified text item's reference position in this note; for example, the upper left, lower left, or center.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextRefPositionAtIndex( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim Index As System.Integer
Dim value As System.Integer

value = instance.GetTextRefPositionAtIndex(Index)
```

### C#

```csharp
System.int GetTextRefPositionAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetTextRefPositionAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the desired piece of text where the index begins at 1

### Return Value

Reference position of the specified text item as defined in [swTextPosition_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTextPosition_e.html)

## VBA Syntax

See [Note::GetTextRefPositionAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Note~GetTextRefPositionAtIndex.html).

## Remarks

Before using this method, use [INote::GetTextCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetTextCount.html).

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::AddText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~AddText.html)
[INote::GetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetText.html)
[INote::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextAngleAtIndex.html)
[INote::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextAtIndex.html)
[INote::GetTextFontAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextFontAtIndex.html)
[INote::GetTextHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextHeightAtIndex.html)
[INote::GetTextInvertAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextInvertAtIndex.html)
[INote::GetTextJustification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextJustification.html)
[INote::GetTextJustificationAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextJustificationAtIndex.html)
[INote::GetTextLineSpacingAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextLineSpacingAtIndex.html)
[INote::GetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextOffsetAtIndex.html)
[INote::GetTextPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextPoint2.html)
[INote::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextPositionAtIndex.html)
[INote::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextRefPositionAtIndex.html)
[INote::IGetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextOffsetAtIndex.html)
[INote::IGetTextPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextPoint2.html)
[INote::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextPositionAtIndex.html)
[INote::IGetTextPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextPoint2.html)
[INote::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextPositionAtIndex.html)
[INote::SetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextAtIndex.html)
[INote::SetTextJustification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextJustification.html)
[INote::SetTextJustificationAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextJustificationAtIndex.html)
[INote::SetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextOffsetAtIndex.html)
[INote::SetTextPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextPoint.html)
[INote::PropertyLinkedText Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~PropertyLinkedText.html)
[INote::TextRightToLeft Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~TextRightToLeft.html)
[INote::SetTextVerticalJustification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextVerticalJustification.html)
[INote::GetTextVerticalJustification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextVerticalJustification.html)
