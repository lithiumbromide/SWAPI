---
title: "GetPlanarZoneVector Method (IDimXpertStraightnessTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertStraightnessTolerance"
member: "GetPlanarZoneVector"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertStraightnessTolerance~GetPlanarZoneVector.html"
---

# GetPlanarZoneVector Method (IDimXpertStraightnessTolerance)

Gets the planar zone vector that is used to compute this DimXpert straightness tolerance.

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
Dim instance As IDimXpertStraightnessTolerance
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

See [DimXpertStraightnessTolerance::GetPlanarZoneVector](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertStraightnessTolerance~GetPlanarZoneVector.html).

## Examples

[Get DimXpert Tolerance4 Example (VBA)](Get_DimXpert_Tolerance4_Example_VB.htm)
[Get DimXpert Tolerance4 Example (VB.NET)](Get_DimXpert_Tolerance4_Example_VBNET.htm)

## See Also

[IDimXpertStraightnessTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertStraightnessTolerance.html)
[IDimXpertStraightnessTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertStraightnessTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
