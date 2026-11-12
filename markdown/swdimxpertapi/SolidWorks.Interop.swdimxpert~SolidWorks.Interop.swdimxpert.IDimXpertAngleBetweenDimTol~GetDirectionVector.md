---
title: "GetDirectionVector Method (IDimXpertAngleBetweenDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAngleBetweenDimTol"
member: "GetDirectionVector"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenDimTol~GetDirectionVector.html"
---

# GetDirectionVector Method (IDimXpertAngleBetweenDimTol)

Gets the direction vector for computing the angle of this DimXpert angle-between dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDirectionVector( _
   ByRef I As System.Double, _
   ByRef J As System.Double, _
   ByRef K As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAngleBetweenDimTol
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetDirectionVector(I, J, K)
```

### C#

```csharp
System.bool GetDirectionVector(
   out System.double I,
   out System.double J,
   out System.double K
)
```

### C++/CLI

```cpp
System.bool GetDirectionVector(
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

See [DimXpertAngleBetweenDimTol::GetDirectionVector](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAngleBetweenDimTol~GetDirectionVector.html).

## See Also

[IDimXpertAngleBetweenDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenDimTol.html)
[IDimXpertAngleBetweenDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
