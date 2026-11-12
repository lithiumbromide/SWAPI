---
title: "GeometryAnalysis Property (gtcocswUtilities)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswUtilities"
member: "GeometryAnalysis"
kind: "property"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities~GeometryAnalysis.html"
---

# GeometryAnalysis Property (gtcocswUtilities)

Gets an IGeometryAnalysis object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property GeometryAnalysis As gtcocswGeometryAnalysis
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswUtilities
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

[gtcocswUtilities Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities.html)
[gtcocswUtilities Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
