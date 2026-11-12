---
title: "CompareFeature Property (gtcocswUtilities)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswUtilities"
member: "CompareFeature"
kind: "property"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities~CompareFeature.html"
---

# CompareFeature Property (gtcocswUtilities)

Gets an ICompareFeature object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CompareFeature As gtcocswCompareFeature
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswUtilities
Dim value As gtcocswCompareFeature

value = instance.CompareFeature
```

### C#

```csharp
gtcocswCompareFeature CompareFeature {get;}
```

### C++/CLI

```cpp
property gtcocswCompareFeature^ CompareFeature {
   gtcocswCompareFeature^ get();
}
```

### Property Value

Pointer to an [ICompareFeature](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.ICompareFeature.html) object

## VBA Syntax

See [IUtilities::CompareFeature](ms-its:swutilitiesapivb6.chm::/swutilities~IUtilities~CompareFeature.html).

## See Also

[gtcocswUtilities Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities.html)
[gtcocswUtilities Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
