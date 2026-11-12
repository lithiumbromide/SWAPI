---
title: "IGetAppliedFeatures Method (IDimXpertFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertFeature"
member: "IGetAppliedFeatures"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature~IGetAppliedFeatures.html"
---

# IGetAppliedFeatures Method (IDimXpertFeature)

Gets all of the features that this DimXpert feature applies to.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAppliedFeatures( _
   ByVal Count As System.Integer _
) As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertFeature
Dim Count As System.Integer
Dim value As DimXpertFeature

value = instance.IGetAppliedFeatures(Count)
```

### C#

```csharp
DimXpertFeature IGetAppliedFeatures(
   System.int Count
)
```

### C++/CLI

```cpp
DimXpertFeature^ IGetAppliedFeatures(
   System.int Count
)
```

### Parameters

- `Count`: Number of parent features in the DimXpertManager tree that this feature applies to

### Return Value

in-process, unmanaged C++: Pointer to an array of [IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Applied features of a DimXpertFeature are its many parents in the feature tree of the DimXpertManager tab of the Management Panel. A single DimXpertFeature can have many applied features.

See [In-process Methods](sldworksapiprogguide.chm::/Overview/In-process_Methods.htm) for details about this type of method.

Before calling this method, call [IDimXpertFeature::GetAppliedFeatureCount](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature~GetAppliedFeatureCount.html) to get the value for the Count parameter.

## See Also

[IDimXpertFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature.html)
[IDimXpertFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
