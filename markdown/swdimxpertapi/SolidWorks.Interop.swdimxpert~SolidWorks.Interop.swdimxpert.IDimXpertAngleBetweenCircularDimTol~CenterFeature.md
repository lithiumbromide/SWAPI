---
title: "CenterFeature Property (IDimXpertAngleBetweenCircularDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAngleBetweenCircularDimTol"
member: "CenterFeature"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenCircularDimTol~CenterFeature.html"
---

# CenterFeature Property (IDimXpertAngleBetweenCircularDimTol)

Gets the DimXpert center feature for this DimXpert angle-between circular dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CenterFeature As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAngleBetweenCircularDimTol
Dim value As DimXpertFeature

value = instance.CenterFeature
```

### C#

```csharp
DimXpertFeature CenterFeature {get;}
```

### C++/CLI

```cpp
property DimXpertFeature^ CenterFeature {
   DimXpertFeature^ get();
}
```

### Property Value

[IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)

## VBA Syntax

See [DimXpertAngleBetweenCircularDimTol::CenterFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAngleBetweenCircularDimTol~CenterFeature.html).

## See Also

[IDimXpertAngleBetweenCircularDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenCircularDimTol.html)
[IDimXpertAngleBetweenCircularDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenCircularDimTol_members.html)

## Availability

SOLIDWORKS 2026 SP02, Revision Number 34.2
