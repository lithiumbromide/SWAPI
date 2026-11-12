---
title: "GeometryAnalysis Property (IUtilities)"
project: "SOLIDWORKS Utilities API Help"
interface: "IUtilities"
member: "GeometryAnalysis"
kind: "property"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities~GeometryAnalysis.html"
---

# GeometryAnalysis Property (IUtilities)

Gets an IGeometryAnalysis object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property GeometryAnalysis As gtcocswGeometryAnalysis
```

### Visual Basic (Usage)

```vb
Dim instance As IUtilities
Dim value As gtcocswGeometryAnalysis

value = instance.GeometryAnalysis
```

### C#

```csharp
gtcocswGeometryAnalysis GeometryAnalysis {get;}
```

### C++/CLI

```cpp
property gtcocswGeometryAnalysis^ GeometryAnalysis {
   gtcocswGeometryAnalysis^ get();
}
```

### Property Value

Pointer to [IGeometryAnalysis](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IGeometryAnalysis.html) object

## VBA Syntax

See [IUtilities::GeometryAnalysis](ms-its:swutilitiesapivb6.chm::/swutilities~IUtilities~GeometryAnalysis.html).

## See Also

[IUtilities Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities.html)
[IUtilities Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
