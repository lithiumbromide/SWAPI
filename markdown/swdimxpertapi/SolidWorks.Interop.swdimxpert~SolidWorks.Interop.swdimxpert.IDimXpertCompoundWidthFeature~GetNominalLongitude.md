---
title: "GetNominalLongitude Method (IDimXpertCompoundWidthFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompoundWidthFeature"
member: "GetNominalLongitude"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundWidthFeature~GetNominalLongitude.html"
---

# GetNominalLongitude Method (IDimXpertCompoundWidthFeature)

Gets components of the longitudinal vector for this width.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalLongitude( _
   ByRef I As System.Double, _
   ByRef J As System.Double, _
   ByRef K As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompoundWidthFeature
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetNominalLongitude(I, J, K)
```

### C#

```csharp
System.bool GetNominalLongitude(
   out System.double I,
   out System.double J,
   out System.double K
)
```

### C++/CLI

```cpp
System.bool GetNominalLongitude(
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `I`: I component of the longitudinal unit vector of the width
- `J`: J component of the longitudinal unit vector of the width
- `K`: K component of the longitudinal unit vector of the width

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertCompoundWidthFeature::GetNominalLongitude](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompoundWidthFeature~GetNominalLongitude.html).

## Remarks

The i, j, and k components of the longitudinal vector indicate the direction of a feature's length with respect to its part axes. For example, if the length of a feature goes along the y-axis of the part, its longitudinal vector is (0, 1, 0).

## See Also

[IDimXpertCompoundWidthFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundWidthFeature.html)
[IDimXpertCompoundWidthFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundWidthFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
