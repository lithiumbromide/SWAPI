---
title: "GetText Method (IParagraphs)"
project: "SOLIDWORKS API Help"
interface: "IParagraphs"
member: "GetText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetText.html"
---

# GetText Method (IParagraphs)

Gets the text of the current paragraph.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetText( _
   ByVal ShowWordWrap As System.Boolean _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IParagraphs
Dim ShowWordWrap As System.Boolean
Dim value As System.String

value = instance.GetText(ShowWordWrap)
```

### C#

```csharp
System.string GetText(
   System.bool ShowWordWrap
)
```

### C++/CLI

```cpp
System.String^ GetText(
   System.bool ShowWordWrap
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ShowWordWrap`: True to show word wrap, false to not

### Return Value

Text of the current paragraph

## VBA Syntax

See [Paragraphs::GetText](ms-its:sldworksapivb6.chm::/sldworks~Paragraphs~GetText.html).

## Examples

See the [IParagraphs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html) examples.

## Remarks

Before calling this method, set the current paragraph using [IParagraphs::CurrentParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~CurrentParagraph.html).

## See Also

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html)
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
