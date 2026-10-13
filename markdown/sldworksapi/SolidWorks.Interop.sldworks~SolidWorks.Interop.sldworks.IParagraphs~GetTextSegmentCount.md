---
title: "GetTextSegmentCount Method (IParagraphs)"
project: "SOLIDWORKS API Help"
interface: "IParagraphs"
member: "GetTextSegmentCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetTextSegmentCount.html"
---

# GetTextSegmentCount Method (IParagraphs)

Gets the number of text segments in the current paragraph.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextSegmentCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IParagraphs
Dim value As System.Integer

value = instance.GetTextSegmentCount()
```

### C#

```csharp
System.int GetTextSegmentCount()
```

### C++/CLI

```cpp
System.int GetTextSegmentCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of text segments

## VBA Syntax

See [Paragraphs::GetTextSegmentCount](ms-its:sldworksapivb6.chm::/sldworks~Paragraphs~GetTextSegmentCount.html).

## Examples

See the [IParagraphs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html) examples.

## Remarks

Paragraphs contain one or more text segments. Each text segment has a different format.

Before calling this method, set the current paragraph using [IParagraphs::CurrentParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~CurrentParagraph.html).

## See Also

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html)
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.html)
[IParagraphs::GetTextSegmentFormat Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetTextSegmentFormat.html)
[IParagraphs::GetTextSegmentText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetTextSegmentText.html)
[IParagraphs::SetTextSegmentFormat Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetTextSegmentFormat.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
