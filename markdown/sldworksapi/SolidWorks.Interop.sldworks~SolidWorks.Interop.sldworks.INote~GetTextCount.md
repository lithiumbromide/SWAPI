---
title: "GetTextCount Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetTextCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextCount.html"
---

# GetTextCount Method (INote)

Gets the number of text items in this note.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Integer

value = instance.GetTextCount()
```

### C#

```csharp
System.int GetTextCount()
```

### C++/CLI

```cpp
System.int GetTextCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of text items

## VBA Syntax

See [Note::GetTextCount](ms-its:sldworksapivb6.chm::/sldworks~Note~GetTextCount.html).

## Examples

[Change Note Text (VBA)](Change_Note_Text_Example_VB.htm)

## Remarks

After calling this method, call any of the following methods:

- [INote::GetTextAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetTextAtIndex.html)
- [INote::GetTextHeightAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetTextHeightAtIndex.html)
- [INote::GetTextPositionAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetTextPositionAtIndex.html) or [INote::IGetTextPositionAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~IGetTextPositionAtIndex.html)
- [INote::GetTextAngleAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetTextAngleAtIndex.html)
- [INote::GetTextRefPositionAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetTextRefPositionAtIndex.html)
- [INote::GetTextInvertAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetTextInvertAtIndex.html)
- [INote::GetTextFontAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetTextFontAtIndex.html)
- [INote::GetTextLineSpacingAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetTextLineSpacingAtIndex.html)

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::INote::AddText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~AddText.html)
[INote::INote::GetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetText.html)
[INote::GetTextJustification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextJustification.html)
[INote::GetTextJustificationAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextJustificationAtIndex.html)
[INote::GetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextOffsetAtIndex.html)
[INote::GetTextPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextPoint2.html)
[INote::IGetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextOffsetAtIndex.html)
[INote::IGetTextPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextPoint2.html)
[INote::SetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetText.html)
[INote::SetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextAtIndex.html)
[INote::SetTextJustification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextJustification.html)
[INote::SetTextJustificationAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextJustificationAtIndex.html)
[INote::SetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextOffsetAtIndex.html)
[INote::SetTextPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextPoint.html)
[INote::PropertyLinkedText Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~PropertyLinkedText.html)
[INote::TextRightToLeft Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~TextRightToLeft.html)
[INote::GetTextVerticalJustification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextVerticalJustification.html)
[INote::SetTextVerticalJustification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextVerticalJustification.html)
