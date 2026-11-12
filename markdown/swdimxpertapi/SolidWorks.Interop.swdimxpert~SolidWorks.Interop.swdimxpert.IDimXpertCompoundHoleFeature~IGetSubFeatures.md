---
title: "IGetSubFeatures Method (IDimXpertCompoundHoleFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompoundHoleFeature"
member: "IGetSubFeatures"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundHoleFeature~IGetSubFeatures.html"
---

# IGetSubFeatures Method (IDimXpertCompoundHoleFeature)

Gets all of the sub-features of this DimXpert compound hole.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSubFeatures( _
   ByVal Count As System.Integer _
) As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompoundHoleFeature
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

- `Count`: Number of sub-features of this DimXpert hole feature

### Return Value

in-process, unmanaged C++: Pointer to an array of [IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)s

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

This method returns all sub-features of the hole feature. All of the sub-features returned by this method do not appear on the DimXpertManager tab of the Management Panel. Functional geometry sub-features such as planes and cylinders that represent each individual face of a part are for internal use only. These sub-features do not appear in the DimXpertManager tree. However, manufacturing sub-features that are significant for downstream machining and inspection do appear in the DimXpertManager tree.

For example, the sub-features of a simple hole are related to functional geometry and are not listed in the DimXpertManager tree. However, the sub-features of a hole pattern are manufacturing features (e.g., simple holes) that are significant for downstream processes. These manufacturing features are listed in the DimXpertManager tree.

See [In-process Methods](sldworksapiprogguide.chm::/Overview/In-process_Methods.htm) for details about this type of method.

Before calling this method, call [IDimXpertCompoundHoleFeature::GetSubFeatureCount](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertCompoundHoleFeature~GetSubFeatureCount.html) to get the value for the Count parameter.

## See Also

[IDimXpertCompoundHoleFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundHoleFeature.html)
[IDimXpertCompoundHoleFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundHoleFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
