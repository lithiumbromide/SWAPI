---
title: "GetZoneDirection Method (IDimXpertSymmetryTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertSymmetryTolerance"
member: "GetZoneDirection"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertSymmetryTolerance~GetZoneDirection.html"
---

# GetZoneDirection Method (IDimXpertSymmetryTolerance)

Gets the zone direction of this DimXpert symmetry tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetZoneDirection( _
   ByRef I As System.Double, _
   ByRef J As System.Double, _
   ByRef K As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertSymmetryTolerance
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetZoneDirection(I, J, K)
```

### C#

```csharp
System.bool GetZoneDirection(
   out System.double I,
   out System.double J,
   out System.double K
)
```

### C++/CLI

```cpp
System.bool GetZoneDirection(
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `I`: I component of the zone direction vector
- `J`: J component of the zone direction vector
- `K`: K component of the zone direction vector

### Return Value

True if the method call is successful; false otherwise

## VBA Syntax

See [DimXpertSymmetryTolerance::GetZoneDirection](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertSymmetryTolerance~GetZoneDirection.html).

## Examples

[Get DimXpert Tolerance2 Example (VBA)](Get_DimXpert_Tolerance2_Example_VB.htm)
[Get DimXpert Tolerance2 Example (VB.NET)](Get_DimXpert_Tolerance2_Example_VBNET.htm)

## See Also

[IDimXpertSymmetryTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertSymmetryTolerance.html)
[IDimXpertSymmetryTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertSymmetryTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
