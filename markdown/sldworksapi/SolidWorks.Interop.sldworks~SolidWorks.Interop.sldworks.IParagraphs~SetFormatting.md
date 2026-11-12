---
title: "SetFormatting Method (IParagraphs)"
project: "SOLIDWORKS API Help"
interface: "IParagraphs"
member: "SetFormatting"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetFormatting.html"
---

# SetFormatting Method (IParagraphs)

Sets the formatting of the current paragraph.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFormatting( _
   ByVal Paragraphspacing As System.Double, _
   ByVal LineSpacing As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IParagraphs
Dim Paragraphspacing As System.Double
Dim LineSpacing As System.Double
Dim value As System.Boolean

value = instance.SetFormatting(Paragraphspacing, LineSpacing)
```

### C#

```csharp
System.bool SetFormatting(
   System.double Paragraphspacing,
   System.double LineSpacing
)
```

### C++/CLI

```cpp
System.bool SetFormatting(
   System.double Paragraphspacing,
   System.double LineSpacing
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Paragraphspacing`: Paragraph spacing
- `LineSpacing`: Line spacing

### Return Value

True if successful, false if not

## VBA Syntax

See [Paragraphs::SetFormatting](ms-its:sldworksapivb6.chm::/sldworks~Paragraphs~SetFormatting.html).

## Examples

See the [IParagraphs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html) examples.

## Remarks

Before calling this method, set the current paragraph using [IParagraphs::CurrentParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~CurrentParagraph.html).

After calling this method, call [IParagraphs::UpdateParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~UpdateParagraph.html) to update the model.

## See Also

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html)
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.html)
[IParagraphs::GetFormatting Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetFormatting.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
