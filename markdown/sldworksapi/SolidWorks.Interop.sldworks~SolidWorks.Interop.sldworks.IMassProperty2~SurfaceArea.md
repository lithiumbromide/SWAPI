---
title: "SurfaceArea Property (IMassProperty2)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty2"
member: "SurfaceArea"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~SurfaceArea.html"
---

# SurfaceArea Property (IMassProperty2)

Gets the surface area of selected components/bodies.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SurfaceArea As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty2
Dim value As System.Double

value = instance.SurfaceArea
```

### C#

```csharp
System.double SurfaceArea {get;}
```

### C++/CLI

```cpp
property System.double SurfaceArea {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Surface area

## VBA Syntax

See [MassProperty2::SurfaceArea](ms-its:sldworksapivb6.chm::/sldworks~MassProperty2~SurfaceArea.html).

## Examples

See the [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html) examples.

## Remarks

If [IMassProperty2::IncludeHiddenBodiesOrComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~IncludeHiddenBodiesOrComponents.html) is reset, then call [IMassProperty2::Recalculate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~Recalculate.html) before using this property.

## See Also

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html)
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
