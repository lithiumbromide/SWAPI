---
title: "GetUpperAndLowerLimitIntraFeature Method (IDimXpertCompositeDistanceBetweenDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompositeDistanceBetweenDimTol"
member: "GetUpperAndLowerLimitIntraFeature"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol~GetUpperAndLowerLimitIntraFeature.html"
---

# GetUpperAndLowerLimitIntraFeature Method (IDimXpertCompositeDistanceBetweenDimTol)

Gets the upper and lower tolerance limits for the feature-locating portion of this DimXpert composite distance-between dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUpperAndLowerLimitIntraFeature( _
   ByRef Upper As System.Double, _
   ByRef Lower As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompositeDistanceBetweenDimTol
Dim Upper As System.Double
Dim Lower As System.Double
Dim value As System.Boolean

value = instance.GetUpperAndLowerLimitIntraFeature(Upper, Lower)
```

### C#

```csharp
System.bool GetUpperAndLowerLimitIntraFeature(
   out System.double Upper,
   out System.double Lower
)
```

### C++/CLI

```cpp
System.bool GetUpperAndLowerLimitIntraFeature(
   [Out] System.double Upper,
   [Out] System.double Lower
)
```

### Parameters

- `Upper`: Upper limit
- `Lower`: Lower limit

### Return Value

True if the method call is successful; false otherwise

## VBA Syntax

See [DimXpertCompositeDistanceBetweenDimTol::GetUpperAndLowerLimitIntraFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompositeDistanceBetweenDimTol~GetUpperAndLowerLimitIntraFeature.html).

## See Also

[IDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol.html)
[IDimXpertCompositeDistanceBetweenDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
