---
title: "GetPlaneFeatures Method (ISwDMDimXpertIntersectLineFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertIntersectLineFeature"
member: "GetPlaneFeatures"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectLineFeature~GetPlaneFeatures.html"
---

# GetPlaneFeatures Method (ISwDMDimXpertIntersectLineFeature)

Gets the DimXpert plane features that intersect to form this DimXpert intersect line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlaneFeatures( _
   ByRef Feature1 As SwDMDimXpertFeature, _
   ByRef Feature2 As SwDMDimXpertFeature _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertIntersectLineFeature
Dim Feature1 As SwDMDimXpertFeature
Dim Feature2 As SwDMDimXpertFeature
Dim value As System.Boolean

value = instance.GetPlaneFeatures(Feature1, Feature2)
```

### C#

```csharp
System.bool GetPlaneFeatures(
   out SwDMDimXpertFeature Feature1,
   out SwDMDimXpertFeature Feature2
)
```

### C++/CLI

```cpp
System.bool GetPlaneFeatures(
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

See [SwDMDimXpertIntersectLineFeature::GetPlaneFeatures](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertIntersectLineFeature~GetPlaneFeatures.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertIntersectLineFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectLineFeature.html)
[ISwDMDimXpertIntersectLineFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectLineFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
