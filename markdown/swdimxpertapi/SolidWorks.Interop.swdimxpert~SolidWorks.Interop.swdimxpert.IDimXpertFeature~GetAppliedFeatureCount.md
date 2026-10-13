---
title: "GetAppliedFeatureCount Method (IDimXpertFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertFeature"
member: "GetAppliedFeatureCount"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature~GetAppliedFeatureCount.html"
---

# GetAppliedFeatureCount Method (IDimXpertFeature)

Gets the number of features that this DimXpert feature applies to.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAppliedFeatureCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertFeature
Dim value As System.Integer

value = instance.GetAppliedFeatureCount()
```

### C#

```csharp
System.int GetAppliedFeatureCount()
```

### C++/CLI

```cpp
System.int GetAppliedFeatureCount();
```

### Return Value

Number of features that this feature applies to

## VBA Syntax

See [DimXpertFeature::GetAppliedFeatureCount](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertFeature~GetAppliedFeatureCount.html).

## Examples

[Get DimXpert Feature Example (VBA)](Get_DimXpert_Feature_Example_VB.htm)
[Get DimXpert Feature Example (VB.NET)](Get_DimXpert_Feature_Example_VBNET.htm)

## Remarks

Applied features of a DimXpertFeature are its many parents in the feature tree of the DimXpertManager tab of the Management Panel. A single DimXpertFeature can have many applied features.

## See Also

[IDimXpertFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature.html)
[IDimXpertFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature_members.html)
