---
title: "IGetTextPositionAtIndex Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "IGetTextPositionAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextPositionAtIndex.html"
---

# IGetTextPositionAtIndex Method (INote)

Gets the text item's offset relative to the document origin.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTextPositionAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim Index As System.Integer
Dim value As System.Double

value = instance.IGetTextPositionAtIndex(Index)
```

### C#

```csharp
System.double IGetTextPositionAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double IGetTextPositionAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the piece of text where the index begins at 0

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before using this method, use [INote::GetTextCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetTextCount.html).

The return value is the following array of doubles :

[ textPtX, textPtY, textPtZ ]

where these text position values are in relation to the document.

The data returned from this method is in terms of document space.

| If the document containing this note is... | Then the coordinates returned are based on the... |
| --- | --- |
| Drawing | Sheet origin |
| Part or assembly | Model origin |

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::AddText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~AddText.html)
[INote::GetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetText.html)
[INote::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextAngleAtIndex.html)
[INote::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextAtIndex.html)
[INote::GetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextCount.html)
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
[INote::SetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetText.html)
[INote::SetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextAtIndex.html)
[INote::SetTextJustification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextJustification.html)
[INote::SetTextJustificationAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextJustificationAtIndex.html)
[INote::SetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextOffsetAtIndex.html)
[INote::SetTextPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextPoint.html)
[INote::SetZeroLengthLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetZeroLengthLeader.html)
[INote::PropertyLinkedText Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~PropertyLinkedText.html)
[INote::TextRightToLeft Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~TextRightToLeft.html)
[INote::SetTextVerticalJustification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextVerticalJustification.html)
[INote::GetTextVerticalJustification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextVerticalJustification.html)
