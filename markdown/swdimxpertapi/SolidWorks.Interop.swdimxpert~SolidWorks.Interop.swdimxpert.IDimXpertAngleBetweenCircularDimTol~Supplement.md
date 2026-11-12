---
title: "Supplement Property (IDimXpertAngleBetweenCircularDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAngleBetweenCircularDimTol"
member: "Supplement"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenCircularDimTol~Supplement.html"
---

# Supplement Property (IDimXpertAngleBetweenCircularDimTol)

Gets whether to evaluate the supplement angle for this DimXpert angle-between circular dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Supplement As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAngleBetweenCircularDimTol
Dim value As System.Boolean

value = instance.Supplement
```

### C#

```csharp
System.bool Supplement {get;}
```

### C++/CLI

```cpp
property System.bool Supplement {
   System.bool get();
}
```

### Property Value

True to evaluate the supplement angle (default); false otherwisev

## VBA Syntax

See [DimXpertAngleBetweenCircularDimTol::Supplement](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAngleBetweenCircularDimTol~Supplement.html).

## See Also

[IDimXpertAngleBetweenCircularDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenCircularDimTol.html)
[IDimXpertAngleBetweenCircularDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenCircularDimTol_members.html)

## Availability

SOLIDWORKS 2026 SP02, Revision Number 34.2
