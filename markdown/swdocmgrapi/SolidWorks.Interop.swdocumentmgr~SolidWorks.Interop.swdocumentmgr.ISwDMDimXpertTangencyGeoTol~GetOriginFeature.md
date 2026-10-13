---
title: "GetOriginFeature Method (ISwDMDimXpertTangencyGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertTangencyGeoTol"
member: "GetOriginFeature"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertTangencyGeoTol~GetOriginFeature.html"
---

# GetOriginFeature Method (ISwDMDimXpertTangencyGeoTol)

Gets the DimXpert feature of origin for this DimXpert tangency geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOriginFeature( _
   ByRef Feature As SwDMDimXpertFeature _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertTangencyGeoTol
Dim Feature As SwDMDimXpertFeature
Dim value As System.Boolean

value = instance.GetOriginFeature(Feature)
```

### C#

```csharp
System.bool GetOriginFeature(
   out SwDMDimXpertFeature Feature
)
```

### C++/CLI

```cpp
System.bool GetOriginFeature(
   [Out] SwDMDimXpertFeature^ Feature
)
```

### Parameters

- `Feature`: [ISwDMDimXpertFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertFeature.html)

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertTangencyGeoTol::GetOriginFeature](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertTangencyGeoTol~GetOriginFeature.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertTangencyGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertTangencyGeoTol.html)
[ISwDMDimXpertTangencyGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertTangencyGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
