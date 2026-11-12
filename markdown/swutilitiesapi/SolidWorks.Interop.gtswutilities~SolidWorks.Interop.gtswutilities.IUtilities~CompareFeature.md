---
title: "CompareFeature Property (IUtilities)"
project: "SOLIDWORKS Utilities API Help"
interface: "IUtilities"
member: "CompareFeature"
kind: "property"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities~CompareFeature.html"
---

# CompareFeature Property (IUtilities)

Gets an ICompareFeature object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CompareFeature As gtcocswCompareFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IUtilities
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

[IUtilities Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities.html)
[IUtilities Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
