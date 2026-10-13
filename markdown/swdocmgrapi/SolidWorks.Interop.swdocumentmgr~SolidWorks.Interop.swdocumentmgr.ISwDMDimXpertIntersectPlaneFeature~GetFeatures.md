---
title: "GetFeatures Method (ISwDMDimXpertIntersectPlaneFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertIntersectPlaneFeature"
member: "GetFeatures"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPlaneFeature~GetFeatures.html"
---

# GetFeatures Method (ISwDMDimXpertIntersectPlaneFeature)

Gets the DimXpert features that intersect to form this DimXpert intersect plane.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatures( _
   ByRef Feature1 As SwDMDimXpertFeature, _
   ByRef Feature2 As SwDMDimXpertFeature _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertIntersectPlaneFeature
Dim Feature1 As SwDMDimXpertFeature
Dim Feature2 As SwDMDimXpertFeature
Dim value As System.Boolean

value = instance.GetFeatures(Feature1, Feature2)
```

### C#

```csharp
System.bool GetFeatures(
   out SwDMDimXpertFeature Feature1,
   out SwDMDimXpertFeature Feature2
)
```

### C++/CLI

```cpp
System.bool GetFeatures(
   [Out] SwDMDimXpertFeature^ Feature1,
   [Out] SwDMDimXpertFeature^ Feature2
)
```

### Parameters

- `Feature1`: [ISwDMDimXpertFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertFeature.html)
- `Feature2`: [ISwDMDimXpertFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertFeature.html)

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertIntersectPlaneFeature::GetFeatures](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertIntersectPlaneFeature~GetFeatures.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertIntersectPlaneFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPlaneFeature.html)
[ISwDMDimXpertIntersectPlaneFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPlaneFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
