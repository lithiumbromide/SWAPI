---
title: "GetIntraFeature Method (ISwDMDimXpertCompositeDistanceBetweenDimTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompositeDistanceBetweenDimTol"
member: "GetIntraFeature"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol~GetIntraFeature.html"
---

# GetIntraFeature Method (ISwDMDimXpertCompositeDistanceBetweenDimTol)

Gets the DimXpert feature located by the feature-locating portion of this DimXpert composite distance-between dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIntraFeature( _
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

value = instance.GetIntraFeature(Feature, FosUsage)
```

### C#

```csharp
System.bool GetIntraFeature(
   out SwDMDimXpertFeature Feature,
   out swDmDimXpertDistanceFosUsage_e FosUsage
)
```

### C++/CLI

```cpp
System.bool GetIntraFeature(
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

See [SwDMDimXpertCompositeDistanceBetweenDimTol::GetIntraFeature](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompositeDistanceBetweenDimTol~GetIntraFeature.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol.html)
[ISwDMDimXpertCompositeDistanceBetweenDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
