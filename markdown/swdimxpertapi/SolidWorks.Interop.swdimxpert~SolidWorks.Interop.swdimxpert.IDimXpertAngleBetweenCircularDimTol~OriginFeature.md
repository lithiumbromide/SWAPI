---
title: "OriginFeature Property (IDimXpertAngleBetweenCircularDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAngleBetweenCircularDimTol"
member: "OriginFeature"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenCircularDimTol~OriginFeature.html"
---

# OriginFeature Property (IDimXpertAngleBetweenCircularDimTol)

Gets the DimXpert origin feature for this DimXpert angle-between circular dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property OriginFeature As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAngleBetweenCircularDimTol
Dim value As DimXpertFeature

value = instance.OriginFeature
```

### C#

```csharp
DimXpertFeature OriginFeature {get;}
```

### C++/CLI

```cpp
property DimXpertFeature^ OriginFeature {
   DimXpertFeature^ get();
}
```

### Property Value

[IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)

## VBA Syntax

See [DimXpertAngleBetweenCircularDimTol::OriginFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAngleBetweenCircularDimTol~OriginFeaturee.html).

## See Also

[IDimXpertAngleBetweenCircularDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenCircularDimTol.html)
[IDimXpertAngleBetweenCircularDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenCircularDimTol_members.html)

## Availability

SOLIDWORKS 2026 SP02, Revision Number 34.2
