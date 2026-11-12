---
title: "GetTextSegmentFormat Method (IParagraphs)"
project: "SOLIDWORKS API Help"
interface: "IParagraphs"
member: "GetTextSegmentFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetTextSegmentFormat.html"
---

# GetTextSegmentFormat Method (IParagraphs)

Gets the text format for the specified text segment in the current paragraph.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextSegmentFormat( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IParagraphs
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetTextSegmentFormat(Index)
```

### C#

```csharp
System.object GetTextSegmentFormat(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetTextSegmentFormat(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of text segment whose text format to get

### Return Value

[ITextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.html)

## VBA Syntax

See [Paragraphs::GetTextSegmentFormat](ms-its:sldworksapivb6.chm::/sldworks~Paragraphs~GetTextSegmentFormat.html).

## Examples

See the [IParagraphs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html) examples.

## Remarks

Paragraphs contain one or more text segments. Each text segment has a different format.

Before calling this method, set the current paragraph using [IParagraphs::CurrentParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~CurrentParagraph.html).

To populate Index, call [IParagraphs::GetTextSegmentCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetTextSegmentCount.html).

## See Also

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html)
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.html)
[IParagraphs::GetTextSegmentText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetTextSegmentText.html)
[IParagraphis::SetTextSegmentFormat Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetTextSegmentFormat.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
