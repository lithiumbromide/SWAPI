---
title: "PropertyLinkedText Property (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "PropertyLinkedText"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~PropertyLinkedText.html"
---

# PropertyLinkedText Property (INote)

Gets or sets the text for the note using the values of the properties linked to the note.

## Syntax

### Visual Basic (Declaration)

```vb
Property PropertyLinkedText As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.String

instance.PropertyLinkedText = value

value = instance.PropertyLinkedText
```

### C#

```csharp
System.string PropertyLinkedText {get; set;}
```

### C++/CLI

```cpp
property System.String^ PropertyLinkedText {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text of note

## VBA Syntax

See [Note::PropertyLinkedText](ms-its:sldworksapivb6.chm::/sldworks~Note~PropertyLinkedText.html).

## Remarks

The string returned by this property is the unresolved string of the note. If the note has linked text, then the source of the link is returned rather than the value of the link.

For example:

| For links to... | This property.... | Returns... |
| --- | --- | --- |
| Custom properties | INote::PropertyLinkedText | Date: ($PRPVIEW:"SW-Long Date") |
|  | INote::GetText | Date: (Monday, December 16, 2016) |
| Dimensions | INote::PropertyLinkedText | Value: ("RD1@Drawing View1") |
|  | INote::GetText | Value: (70) |

NOTE: For notes without links, INote::PropertyLinkedText and INote::GetText behave the same.

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::AddText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~AddText.html)
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
[INote::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextPositionAtIndex.html)
[INote::SetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetText.html)
[INote::SetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextAtIndex.html)
[INote::SetTextJustification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextJustification.html)
[INote::SetTextJustificationAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextJustificationAtIndex.html)
[INote::SetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextOffsetAtIndex.html)
[INote::SetTextPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextPoint.html)
[INote::TextRightToLeft Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~TextRightToLeft.html)
[INote::GetTextVerticalJustification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextVerticalJustification.html)
[INote::SetTextVerticalJustification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextVerticalJustification.html)
