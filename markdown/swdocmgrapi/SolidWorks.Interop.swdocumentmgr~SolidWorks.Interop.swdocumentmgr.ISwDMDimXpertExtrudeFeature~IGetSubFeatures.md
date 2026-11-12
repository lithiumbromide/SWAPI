---
title: "IGetSubFeatures Method (ISwDMDimXpertExtrudeFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertExtrudeFeature"
member: "IGetSubFeatures"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~IGetSubFeatures.html"
---

# IGetSubFeatures Method (ISwDMDimXpertExtrudeFeature)

Gets all of the sub-features of this DimXpert extrude.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSubFeatures( _
   ByVal Count As System.Integer _
) As SwDMDimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertExtrudeFeature
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

- `Count`: Number of sub-features in the extrude

### Return Value

in-process, unmanaged C++: Pointer to an array of [SwDMDimXpertFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertFeature.html)s

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Use [ISwDMDimXpertExtrudeFeature::GetSubFeatureCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~GetSubFeatureCount.html) to populate the Count argument.

## See Also

[ISwDMDimXpertExtrudeFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature.html)
[ISwDMDimXpertExtrudeFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature_members.html)
[ISwDMDimXpertExtrudeFeature::GetSubFeatures Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~GetSubFeatures.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
