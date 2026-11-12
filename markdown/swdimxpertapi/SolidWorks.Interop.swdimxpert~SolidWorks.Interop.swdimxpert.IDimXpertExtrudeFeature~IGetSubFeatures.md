---
title: "IGetSubFeatures Method (IDimXpertExtrudeFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertExtrudeFeature"
member: "IGetSubFeatures"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature~IGetSubFeatures.html"
---

# IGetSubFeatures Method (IDimXpertExtrudeFeature)

Gets all of the sub-features of this DimXpert extrude.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSubFeatures( _
   ByVal Count As System.Integer _
) As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertExtrudeFeature
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

- `Count`: Number of sub-features of this DimXpert extrude feature

### Return Value

in-process, unmanaged C++: Pointer to an array of [IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)s

VBA, VB.NET, C#, and C++/CLI: Not supported

## Examples

[Get DimXpert Extrude Feature Example (VBA)](Get_DimXpert_Extrude_Feature_Example_VB.htm)
[Get DimXpert Extrude Feature Example (VB.NET)](Get_DimXpert_Extrude_Feature_Example_VBNET.htm)

## Remarks

This method returns all sub-features of this extrude feature. All of the sub-features returned by this method do not appear on the DimXpertManager tab of the Management Panel. Functional geometry sub-features such as planes and cylinders that represent each individual face of a part are for internal use only. These sub-features do not appear in the DimXpertManager tree. However, manufacturing sub-features that are significant for downstream machining and inspection do appear in the DimXpertManager tree.

See [In-process Methods](sldworksapiprogguide.chm::/Overview/In-process_Methods.htm) for details about this type of method.

Before calling this method, call [IDimXpertExtrudeFeature::GetSubFeatureCount](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertExtrudeFeature~GetSubFeatureCount.html) to get the value for the Count parameter.

## See Also

[IDimXpertExtrudeFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature.html)
[IDimXpertExtrudeFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
