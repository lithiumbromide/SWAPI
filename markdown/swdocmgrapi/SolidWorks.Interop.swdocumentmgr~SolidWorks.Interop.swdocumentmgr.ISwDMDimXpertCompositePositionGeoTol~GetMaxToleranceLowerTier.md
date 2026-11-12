---
title: "GetMaxToleranceLowerTier Method (ISwDMDimXpertCompositePositionGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompositePositionGeoTol"
member: "GetMaxToleranceLowerTier"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol~GetMaxToleranceLowerTier.html"
---

# GetMaxToleranceLowerTier Method (ISwDMDimXpertCompositePositionGeoTol)

Gets whether the maximum tolerance is set in the lower tier for this DimXpert composite position geometric tolerance.

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
Dim instance As ISwDMDimXpertCompositePositionGeoTol
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

- `IsMax`: True, if maximum tolerance is set in the lower tier; false, otherwise
- `Tolerance`: Maximum tolerance in the lower tier

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertCompositePositionGeoTol::GetMaxToleranceLowerTier](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompositePositionGeoTol~GetMaxToleranceLowerTier.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompositePositionGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol.html)
[ISwDMDimXpertCompositePositionGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
