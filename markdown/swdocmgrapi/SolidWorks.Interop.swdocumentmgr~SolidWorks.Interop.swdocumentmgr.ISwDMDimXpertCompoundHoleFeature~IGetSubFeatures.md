---
title: "IGetSubFeatures Method (ISwDMDimXpertCompoundHoleFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompoundHoleFeature"
member: "IGetSubFeatures"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature~IGetSubFeatures.html"
---

# IGetSubFeatures Method (ISwDMDimXpertCompoundHoleFeature)

Gets all of the sub-features of this DimXpert compound hole.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSubFeatures( _
   ByVal Count As System.Integer _
) As SwDMDimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompoundHoleFeature
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

- `Count`: Number of sub-features in this compound hole

### Return Value

in-process, unmanaged C++: Pointer to an array of [SwDMDimXpertFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertFeature.html)s

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Use [ISwDMDimXpertCompoundHoleFeature::GetSubFeatureCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature~GetSubFeatureCount.html) to populate the Count argument.

## See Also

[ISwDMDimXpertCompoundHoleFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature.html)
[ISwDMDimXpertCompoundHoleFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature_members.html)
[ISwDMDimXpertCompoundHoleFeature::GetSubFeatures Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature~GetSubFeatures.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
