---
title: "CompareGeometry Property (IUtilities)"
project: "SOLIDWORKS Utilities API Help"
interface: "IUtilities"
member: "CompareGeometry"
kind: "property"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities~CompareGeometry.html"
---

# CompareGeometry Property (IUtilities)

Gets an ICompareGeometry object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CompareGeometry As gtcocswCompareGeometry
```

### Visual Basic (Usage)

```vb
Dim instance As IUtilities
Dim value As gtcocswCompareGeometry

value = instance.CompareGeometry
```

### C#

```csharp
gtcocswCompareGeometry CompareGeometry {get;}
```

### C++/CLI

```cpp
property gtcocswCompareGeometry^ CompareGeometry {
   gtcocswCompareGeometry^ get();
}
```

### Property Value

Pointer to an [ICompareGeometry](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.ICompareGeometry.html) object

## VBA Syntax

See [IUtilities::CompareGeometry](ms-its:swutilitiesapivb6.chm::/swutilities~IUtilities~CompareGeometry.html).

## See Also

[IUtilities Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities.html)
[IUtilities Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
