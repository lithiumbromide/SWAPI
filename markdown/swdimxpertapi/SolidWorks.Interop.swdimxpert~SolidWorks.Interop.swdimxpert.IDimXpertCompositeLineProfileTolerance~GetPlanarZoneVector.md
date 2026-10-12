---
title: "GetPlanarZoneVector Method (IDimXpertCompositeLineProfileTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompositeLineProfileTolerance"
member: "GetPlanarZoneVector"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeLineProfileTolerance~GetPlanarZoneVector.html"
---

# GetPlanarZoneVector Method (IDimXpertCompositeLineProfileTolerance)

Gets the planar zone vector that is used for computing this DimXpert composite line profile tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlanarZoneVector( _
   ByRef I As System.Double, _
   ByRef J As System.Double, _
   ByRef K As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompositeLineProfileTolerance
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetPlanarZoneVector(I, J, K)
```

### C#

```csharp
System.bool GetPlanarZoneVector(
   out System.double I,
   out System.double J,
   out System.double K
)
```

### C++/CLI

```cpp
System.bool GetPlanarZoneVector(
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `I`: I component of the planar zone vector
- `J`: J component of the planar zone vector
- `K`: K component of the planar zone vector

### Return Value

True if the method call is successful; false otherwise

## VBA Syntax

See [DimXpertCompositeLineProfileTolerance::GetPlanarZoneVector](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompositeLineProfileTolerance~GetPlanarZoneVector.html).

## See Also

[IDimXpertCompositeLineProfileTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeLineProfileTolerance.html)
[IDimXpertCompositeLineProfileTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeLineProfileTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
