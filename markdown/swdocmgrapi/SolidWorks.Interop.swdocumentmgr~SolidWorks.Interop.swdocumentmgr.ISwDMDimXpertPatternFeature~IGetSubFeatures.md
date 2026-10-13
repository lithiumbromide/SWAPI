---
title: "IGetSubFeatures Method (ISwDMDimXpertPatternFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertPatternFeature"
member: "IGetSubFeatures"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPatternFeature~IGetSubFeatures.html"
---

# IGetSubFeatures Method (ISwDMDimXpertPatternFeature)

Gets all of the sub-features in this DimXpert pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSubFeatures( _
   ByVal Count As System.Integer _
) As SwDMDimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertPatternFeature
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

- `Count`: Number of sub-features in this pattern

### Return Value

in-process, unmanaged C++: Pointer to an array of [ISwDMDimXpertFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertFeature.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Use [ISwDMDimXpertPatternFeature::GetSubFeatureCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertPatternFeature~GetSubFeatureCount.html) to populate the Count argument.

## See Also

[ISwDMDimXpertPatternFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPatternFeature.html)
[ISwDMDimXpertPatternFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPatternFeature_members.html)
[ISwDMDimXpertPatternFeature::GetSubFeatures Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPatternFeature~GetSubFeatures.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
