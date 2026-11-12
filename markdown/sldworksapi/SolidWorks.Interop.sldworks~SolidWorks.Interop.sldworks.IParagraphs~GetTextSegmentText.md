---
title: "GetTextSegmentText Method (IParagraphs)"
project: "SOLIDWORKS API Help"
interface: "IParagraphs"
member: "GetTextSegmentText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetTextSegmentText.html"
---

# GetTextSegmentText Method (IParagraphs)

Gets the text of the specified text segment in the current paragraph.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextSegmentText( _
   ByVal Index As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IParagraphs
Dim Index As System.Integer
Dim value As System.String

value = instance.GetTextSegmentText(Index)
```

### C#

```csharp
System.string GetTextSegmentText(
   System.int Index
)
```

### C++/CLI

```cpp
System.String^ GetTextSegmentText(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of text segment whose text to get

### Return Value

Text of text segment

## VBA Syntax

See [Paragraphs::GetTextSegmentText](ms-its:sldworksapivb6.chm::/sldworks~Paragraphs~GetTextSegmentText.html).

## Examples

See the [IParagraphs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html) examples.

## Remarks

Paragraphs contain one or more text segments. Each text segment has a different format.

Before calling this method, set the current paragraph using [IParagraphs::CurrentParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~CurrentParagraph.html).

To populate Index, call [IParagraphs::GetTextSegmentCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetTextSegmentCount.html).

## See Also

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html)
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.html)
[IParagraphs::GetTextSegmentFormat Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetTextSegmentFormat.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
