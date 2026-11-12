---
title: "GetPlanarZoneVector Method (IDimXpertOrientationTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertOrientationTolerance"
member: "GetPlanarZoneVector"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertOrientationTolerance~GetPlanarZoneVector.html"
---

# GetPlanarZoneVector Method (IDimXpertOrientationTolerance)

Gets the planar zone vector that is used to compute this DimXpert orientation tolerance.

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
Dim instance As IDimXpertOrientationTolerance
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

See [DimXpertOrientationTolerance::GetPlanarZoneVector](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertOrientationTolerance~GetPlanarZoneVector.html).

## Examples

[Get DimXpert Tolerance3 Example (VBA)](Get_DimXpert_Tolerance3_Example_VB.htm)
[Get DimXpert Tolerance3 Example (VB.NET)](Get_DimXpert_Tolerance3_Example_VBNET.htm)

## See Also

[IDimXpertOrientationTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertOrientationTolerance.html)
[IDimXpertOrientationTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertOrientationTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
