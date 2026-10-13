---
title: "IGetSubFeatures Method (IDimXpertBestfitPlaneFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertBestfitPlaneFeature"
member: "IGetSubFeatures"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertBestfitPlaneFeature~IGetSubFeatures.html"
---

# IGetSubFeatures Method (IDimXpertBestfitPlaneFeature)

Gets all of the sub-features of this DimXpert best fit plane.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSubFeatures( _
   ByVal Count As System.Integer _
) As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertBestfitPlaneFeature
Dim Count As System.Integer
Dim value As DimXpertFeature

value = instance.IGetSubFeatures(Count)
```

### C#

```csharp
DimXpertFeature IGetSubFeatures(
   System.int Count
)
```

### C++/CLI

```cpp
DimXpertFeature^ IGetSubFeatures(
   System.int Count
)
```

### Parameters

- `Count`: Number of sub-features of this DimXpert best fit plane feature

### Return Value

in-process, unmanaged C++: Pointer to an array of [IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)s

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

This method returns all sub-features of this best fit plane feature. All of the sub-features returned by this method do not appear on the DimXpertManager tab of the Management Panel. Functional geometry sub-features such as planes and cylinders that represent each individual face of a part are for internal use only. These sub-features do not appear in the DimXpertManager tree. However, manufacturing sub-features that are significant for downstream machining and inspection do appear in the DimXpertManager tree.See [In-process Methods](sldworksapiprogguide.chm::/Overview/In-process_Methods.htm) for details about this type of method.

Before calling this method, call [IDimXpertBestfitPlaneFeature::GetSubFeatureCount](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertBestfitPlaneFeature~GetSubFeatureCount.html) to get the value for the Count parameter.

## See Also

[IDimXpertBestfitPlaneFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertBestfitPlaneFeature.html)
[IDimXpertBestfitPlaneFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertBestfitPlaneFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
