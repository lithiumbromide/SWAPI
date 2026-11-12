---
title: "GetOriginFeature Method (ISwDMDimXpertCompositeDistanceBetweenDimTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompositeDistanceBetweenDimTol"
member: "GetOriginFeature"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol~GetOriginFeature.html"
---

# GetOriginFeature Method (ISwDMDimXpertCompositeDistanceBetweenDimTol)

Gets the DimXpert feature of origin to which this DimXpert composite distance-between dimension tolerance is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOriginFeature( _
   ByRef Feature As SwDMDimXpertFeature, _
   ByRef FosUsage As swDmDimXpertDistanceFosUsage_e _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompositeDistanceBetweenDimTol
Dim Feature As SwDMDimXpertFeature
Dim FosUsage As swDmDimXpertDistanceFosUsage_e
Dim value As System.Boolean

value = instance.GetOriginFeature(Feature, FosUsage)
```

### C#

```csharp
System.bool GetOriginFeature(
   out SwDMDimXpertFeature Feature,
   out swDmDimXpertDistanceFosUsage_e FosUsage
)
```

### C++/CLI

```cpp
System.bool GetOriginFeature(
   [Out] SwDMDimXpertFeature^ Feature,
   [Out] swDmDimXpertDistanceFosUsage_e FosUsage
)
```

### Parameters

- `Feature`: [ISwDMDimXpertFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertFeature.html)
- `FosUsage`: How to treat the feature of size when applying this tolerance as defined in [swDmDimXpertDistanceFosUsage_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmDimXpertDistanceFosUsage_e.html)

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertCompositeDistanceBetweenDimTol::GetOriginFeature](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompositeDistanceBetweenDimTol~GetOriginFeature.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol.html)
[ISwDMDimXpertCompositeDistanceBetweenDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
