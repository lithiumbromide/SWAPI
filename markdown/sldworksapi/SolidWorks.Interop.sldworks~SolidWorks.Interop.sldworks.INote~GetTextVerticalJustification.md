---
title: "GetTextVerticalJustification Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetTextVerticalJustification"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextVerticalJustification.html"
---

# GetTextVerticalJustification Method (INote)

Gets the vertical justification of a standard note.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextVerticalJustification() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Integer

value = instance.GetTextVerticalJustification()
```

### C#

```csharp
System.int GetTextVerticalJustification()
```

### C++/CLI

```cpp
System.int GetTextVerticalJustification();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Vertical justification as defined in [swTextAlignmentVertical_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTextAlignmentVertical_e.html)

## VBA Syntax

See [Note::GetTextVerticalJustification](ms-its:sldworksapivb6.chm::/sldworks~Note~GetTextVerticalJustification.html).

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::SetTextVerticalJustification Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextVerticalJustification.html)
[INote::GetText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetText.html)
[INote::GetTextAngleAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextAngleAtIndex.html)
[INote::GetTextCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextCount.html)
[INote::GetTextFontAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextFontAtIndex.html)
[INote::GetTextHeightAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextHeightAtIndex.html)
[INote::GetTextInvertAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextInvertAtIndex.html)
[INote::GetTextJustification Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextJustification.html)
[INote::GetTextLineSpacingAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextLineSpacingAtIndex.html)
[INote::GetTextPoint2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextPoint2.html)
[INote::GetTextPositionAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextPositionAtIndex.html)
[INote::GetTextRefPositionAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextRefPositionAtIndex.html)
[INote::SetText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetText.html)
[INote::SetTextJustification Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextJustification.html)
[INote::SetTextPoint Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextPoint.html)
[INote::PropertyLinkedText Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~PropertyLinkedText.html)
[INote::TextRightToLeft Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~TextRightToLeft.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
