---
title: "GetFormatting Method (IParagraphs)"
project: "SOLIDWORKS API Help"
interface: "IParagraphs"
member: "GetFormatting"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetFormatting.html"
---

# GetFormatting Method (IParagraphs)

Gets the formatting of the current paragraph.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFormatting( _
   ByRef Paragraphspacing As System.Double, _
   ByRef LineSpacing As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IParagraphs
Dim Paragraphspacing As System.Double
Dim LineSpacing As System.Double
Dim value As System.Boolean

value = instance.GetFormatting(Paragraphspacing, LineSpacing)
```

### C#

```csharp
System.bool GetFormatting(
   out System.double Paragraphspacing,
   out System.double LineSpacing
)
```

### C++/CLI

```cpp
System.bool GetFormatting(
   [Out] System.double Paragraphspacing,
   [Out] System.double LineSpacing
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Paragraphspacing`: Paragraph spacing
- `LineSpacing`: Line spacing

### Return Value

True if successful, false if not

## VBA Syntax

See [Paragraphs::GetFormatting](ms-its:sldworksapivb6.chm::/sldworks~Paragraphs~GetFormatting.html).

## Remarks

Before calling this method, set the current paragraph using [IParagraphs::CurrentParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~CurrentParagraph.html).

## See Also

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html)
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.html)
[IParagraphs::SetFormatting Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetFormatting.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
