---
title: "GetAppliedFeatures Method (IDimXpertFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertFeature"
member: "GetAppliedFeatures"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature~GetAppliedFeatures.html"
---

# GetAppliedFeatures Method (IDimXpertFeature)

Gets all of the features that this DimXpert feature applies to.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAppliedFeatures() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertFeature
Dim value As System.Object

value = instance.GetAppliedFeatures()
```

### C#

```csharp
System.object GetAppliedFeatures()
```

### C++/CLI

```cpp
System.Object^ GetAppliedFeatures();
```

### Return Value

Array of [IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)s

## VBA Syntax

See [DimXpertFeature::GetAppliedFeatures](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertFeature~GetAppliedFeatures.html).

## Examples

[Get DimXpert Feature Example (VBA)](Get_DimXpert_Feature_Example_VB.htm)
[Get DimXpert Feature Example (VB.NET)](Get_DimXpert_Feature_Example_VBNET.htm)

## Remarks

Applied features of a DimXpertFeature are its many parents in the feature tree of the DimXpertManager tab of the Management Panel. A single DimXpertFeature can have many applied features.

## See Also

[IDimXpertFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature.html)
[IDimXpertFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
