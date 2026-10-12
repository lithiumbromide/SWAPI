---
title: "IGetSubFeatures Method (ISwDMDimXpertBestFitPlaneFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertBestFitPlaneFeature"
member: "IGetSubFeatures"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertBestFitPlaneFeature~IGetSubFeatures.html"
---

# IGetSubFeatures Method (ISwDMDimXpertBestFitPlaneFeature)

Gets all of the sub-features of this DimXpert best fit plane.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSubFeatures( _
   ByVal Count As System.Integer _
) As SwDMDimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertBestFitPlaneFeature
Dim Count As System.Integer
Dim value As SwDMDimXpertFeature

value = instance.IGetSubFeatures(Count)
```

### C#

```csharp
SwDMDimXpertFeature IGetSubFeatures(
   System.int Count
)
```

### C++/CLI

```cpp
SwDMDimXpertFeature^ IGetSubFeatures(
   System.int Count
)
```

### Parameters

- `Count`: Number of sub-features of the best fit plane

### Return Value

in-process, unmanaged C++: Pointer to an array of [SwDMDimXpertFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertFeature.html)s

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Use [ISwDMDimXpertBestFitPlaneFeature::GetSubFeatureCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertBestFitPlaneFeature~GetSubFeatureCount.html) to populate the Count argument.

## See Also

[ISwDMDimXpertBestFitPlaneFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertBestFitPlaneFeature.html)
[ISwDMDimXpertBestFitPlaneFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertBestFitPlaneFeature_members.html)
[ISwDMDimXpertBestFitPlaneFeature::GetSubFeatures Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertBestFitPlaneFeature~GetSubFeatures.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
