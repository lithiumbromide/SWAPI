---
title: "GetActPlaneVector Method (IDimXpertAngleBetweenCircularDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAngleBetweenCircularDimTol"
member: "GetActPlaneVector"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenCircularDimTol~GetActPlaneVector.html"
---

# GetActPlaneVector Method (IDimXpertAngleBetweenCircularDimTol)

Gets the actual plane vector for computing the angle of this DimXpert angle-between circular dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetActPlaneVector( _
   ByRef I As System.Double, _
   ByRef J As System.Double, _
   ByRef K As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAngleBetweenCircularDimTol
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetActPlaneVector(I, J, K)
```

### C#

```csharp
System.bool GetActPlaneVector(
   out System.double I,
   out System.double J,
   out System.double K
)
```

### C++/CLI

```cpp
System.bool GetActPlaneVector(
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `I`: I component of the direction vector
- `J`: J component of the direction vector
- `K`: K component of the direction vector

### Return Value

True if the method call is successful; false otherwise

## VBA Syntax

See [DimXpertAngleBetweenCircularDimTol::GetActPlaneVector](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAngleBetweenCircularDimTol~GetActPlaneVector.html).

## See Also

[IDimXpertAngleBetweenCircularDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenCircularDimTol.html)
[IDimXpertAngleBetweenCircularDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenCircularDimTol_members.html)

## Availability

SOLIDWORKS 2026 SP02, Revision Number 34.2
