---
title: "CompareDocument Property (gtcocswUtilities)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswUtilities"
member: "CompareDocument"
kind: "property"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities~CompareDocument.html"
---

# CompareDocument Property (gtcocswUtilities)

Gets an ICompareDocument object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CompareDocument As gtcocswCompareDocument
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswUtilities
Dim value As gtcocswCompareDocument

value = instance.CompareDocument
```

### C#

```csharp
gtcocswCompareDocument CompareDocument {get;}
```

### C++/CLI

```cpp
property gtcocswCompareDocument^ CompareDocument {
   gtcocswCompareDocument^ get();
}
```

### Property Value

Pointer to an [ICompareDocument](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.ICompareDocument.html) object

## VBA Syntax

See [IUtilities::CompareDocument](ms-its:swutilitiesapivb6.chm::/swutilities~IUtilities~CompareDocument.html).

## See Also

[gtcocswUtilities Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities.html)
[gtcocswUtilities Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
