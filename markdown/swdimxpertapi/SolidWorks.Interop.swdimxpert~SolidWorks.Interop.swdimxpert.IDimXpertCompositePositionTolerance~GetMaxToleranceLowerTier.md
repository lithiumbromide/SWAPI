---
title: "GetMaxToleranceLowerTier Method (IDimXpertCompositePositionTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompositePositionTolerance"
member: "GetMaxToleranceLowerTier"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositePositionTolerance~GetMaxToleranceLowerTier.html"
---

# GetMaxToleranceLowerTier Method (IDimXpertCompositePositionTolerance)

Gets whether the maximum tolerance is set in the lower tier for this DimXpert composite position tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaxToleranceLowerTier( _
   ByRef IsMax As System.Boolean, _
   ByRef Tolerance As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompositePositionTolerance
Dim IsMax As System.Boolean
Dim Tolerance As System.Double
Dim value As System.Boolean

value = instance.GetMaxToleranceLowerTier(IsMax, Tolerance)
```

### C#

```csharp
System.bool GetMaxToleranceLowerTier(
   out System.bool IsMax,
   out System.double Tolerance
)
```

### C++/CLI

```cpp
System.bool GetMaxToleranceLowerTier(
   [Out] System.bool IsMax,
   [Out] System.double Tolerance
)
```

### Parameters

- `IsMax`: True if the maximum tolerance is set in the lower tier; false otherwise
- `Tolerance`: Maximum tolerance in lower tier

### Return Value

True if the method call is successful; false otherwise

## VBA Syntax

See [DimXpertCompositePositionTolerance::GetMaxToleranceLowerTier](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompositePositionTolerance~GetMaxToleranceLowerTier.html).

## Remarks

The second row of the Geometric Tolerance Properties dialog comes into play for composite tolerances. This lower tier property is set in the second row of the dialog.

## See Also

[IDimXpertCompositePositionTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositePositionTolerance.html)
[IDimXpertCompositePositionTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositePositionTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
