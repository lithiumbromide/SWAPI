---
title: "GetNominalVector Method (IDimXpertIntersectPointFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertIntersectPointFeature"
member: "GetNominalVector"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectPointFeature~GetNominalVector.html"
---

# GetNominalVector Method (IDimXpertIntersectPointFeature)

Gets the direction vector of this DimXpert intersect point.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalVector( _
   ByRef I As System.Double, _
   ByRef J As System.Double, _
   ByRef K As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertIntersectPointFeature
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetNominalVector(I, J, K)
```

### C#

```csharp
System.bool GetNominalVector(
   out System.double I,
   out System.double J,
   out System.double K
)
```

### C++/CLI

```cpp
System.bool GetNominalVector(
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `I`: I component of the direction vector of the intersect point
- `J`: J component of the direction vector of the intersect point
- `K`: K component of the direction vector of the intersect point

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertIntersectPointFeature::GetNominalVector](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertIntersectPointFeature~GetNominalVector.html).

## See Also

[IDimXpertIntersectPointFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectPointFeature.html)
[IDimXpertIntersectPointFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectPointFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
