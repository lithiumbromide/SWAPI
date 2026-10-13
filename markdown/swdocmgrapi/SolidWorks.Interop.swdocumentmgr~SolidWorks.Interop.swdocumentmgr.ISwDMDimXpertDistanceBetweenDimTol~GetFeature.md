---
title: "GetFeature Method (ISwDMDimXpertDistanceBetweenDimTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertDistanceBetweenDimTol"
member: "GetFeature"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDistanceBetweenDimTol~GetFeature.html"
---

# GetFeature Method (ISwDMDimXpertDistanceBetweenDimTol)

Gets the DimXpert feature to which this DimXpert distance-between dimension tolerance is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeature( _
   ByRef Feature As SwDMDimXpertFeature, _
   ByRef FosUsage As swDmDimXpertDistanceFosUsage_e _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertDistanceBetweenDimTol
Dim Feature As SwDMDimXpertFeature
Dim FosUsage As swDmDimXpertDistanceFosUsage_e
Dim value As System.Boolean

value = instance.GetFeature(Feature, FosUsage)
```

### C#

```csharp
System.bool GetFeature(
   out SwDMDimXpertFeature Feature,
   out swDmDimXpertDistanceFosUsage_e FosUsage
)
```

### C++/CLI

```cpp
System.bool GetFeature(
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

See [SwDMDimXpertDistanceBetweenDimTol::GetFeature](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertDistanceBetweenDimTol~GetFeature.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDistanceBetweenDimTol.html)
[ISwDMDimXpertDistanceBetweenDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDistanceBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
