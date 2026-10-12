---
title: "SetTextSegmentFormat Method (IParagraphs)"
project: "SOLIDWORKS API Help"
interface: "IParagraphs"
member: "SetTextSegmentFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetTextSegmentFormat.html"
---

# SetTextSegmentFormat Method (IParagraphs)

Sets the text format for the specified text segment in the current paragraph.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTextSegmentFormat( _
   ByVal Segment As System.Integer, _
   ByVal Format As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IParagraphs
Dim Segment As System.Integer
Dim Format As System.Object
Dim value As System.Boolean

value = instance.SetTextSegmentFormat(Segment, Format)
```

### C#

```csharp
System.bool SetTextSegmentFormat(
   System.int Segment,
   System.object Format
)
```

### C++/CLI

```cpp
System.bool SetTextSegmentFormat(
   System.int Segment,
   System.Object^ Format
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Segment`: 0-based index of the text segment whose format to set
- `Format`: [ITextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.html)

### Return Value

True if successful, false if not

## VBA Syntax

See [Paragraphs::SetTextSegmentFormat](ms-its:sldworksapivb6.chm::/sldworks~Paragraphs~SetTextSegmentFormat.html).

## Examples

See the [IParagraphs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html) examples.

## Remarks

Paragraphs contain one or more text segments. Each text segment has a different format.

Before calling this method:

- set the current paragraph using [IParagraphs::CurrentParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~CurrentParagraph.html).
- call [IParagraphs::GetTextSegmentCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetTextSegmentCount.html) to get the total number of text segments and a valid value for Segment.

After calling this method, call [IParagraphs::UpdateParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~UpdateParagraph.html) to update the model.

## See Also

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html)
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.html)
[IParagraphics::GetTextSegmentFormat Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetTextSegmentFormat.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
