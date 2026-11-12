---
title: "UpdateParagraph Method (IParagraphs)"
project: "SOLIDWORKS API Help"
interface: "IParagraphs"
member: "UpdateParagraph"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~UpdateParagraph.html"
---

# UpdateParagraph Method (IParagraphs)

Updates the model with the changes made to the current paragraph.

## Syntax

### Visual Basic (Declaration)

```vb
Function UpdateParagraph() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IParagraphs
Dim value As System.Boolean

value = instance.UpdateParagraph()
```

### C#

```csharp
System.bool UpdateParagraph()
```

### C++/CLI

```cpp
System.bool UpdateParagraph();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the model is updated with the paragraph changes, false if not

## VBA Syntax

See [Paragraphs::UpdateParagraph](ms-its:sldworksapivb6.chm::/sldworks~Paragraphs~UpdateParagraph.html).

## Examples

See the [IParagraphs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html) examples.

## Remarks

You must call this method to update the model after calling:

- [IParagraphs::SetBulletsAndNumbering](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetBulletsAndNumbering.html)
- [IParagraphs::SetFormatting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetFormatting.html)
- [IParagraphs::SetIndentation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetIndentation.html)
- [IParagraphs::SetTextSegmentFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetTextSegmentFormat.html)

## See Also

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html)
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
