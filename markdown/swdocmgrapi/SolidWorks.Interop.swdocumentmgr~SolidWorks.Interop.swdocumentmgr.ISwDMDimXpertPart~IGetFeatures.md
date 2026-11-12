---
title: "IGetFeatures Method (ISwDMDimXpertPart)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertPart"
member: "IGetFeatures"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart~IGetFeatures.html"
---

# IGetFeatures Method (ISwDMDimXpertPart)

Gets all of the DimXpert features in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFeatures( _
   ByVal Count As System.Integer _
) As SwDMDimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertPart
Dim Count As System.Integer
Dim value As SwDMDimXpertFeature

value = instance.IGetFeatures(Count)
```

### C#

```csharp
SwDMDimXpertFeature IGetFeatures(
   System.int Count
)
```

### C++/CLI

```cpp
SwDMDimXpertFeature^ IGetFeatures(
   System.int Count
)
```

### Parameters

- `Count`: Number of features

### Return Value

in-process, unmanaged C++: Pointer to an array of [ISwDMDimXpertFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertFeature.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Use [ISwDMDimXpertPart::GetFeatureCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertPart~GetFeatureCount.html) to populate the Count argument.

## See Also

[ISwDMDimXpertPart Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart.html)
[ISwDMDimXpertPart Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart_members.html)
[ISwDMDimXpertPart::GetFeatures Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart~GetFeatures.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
