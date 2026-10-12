---
title: "GetSubFeatures Method (IDimXpertBestfitPlaneFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertBestfitPlaneFeature"
member: "GetSubFeatures"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertBestfitPlaneFeature~GetSubFeatures.html"
---

# GetSubFeatures Method (IDimXpertBestfitPlaneFeature)

Gets all of the sub-features of this DimXpert best fit plane.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSubFeatures() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertBestfitPlaneFeature
Dim value As System.Object

value = instance.GetSubFeatures()
```

### C#

```csharp
System.object GetSubFeatures()
```

### C++/CLI

```cpp
System.Object^ GetSubFeatures();
```

### Return Value

Array of [IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)s

## VBA Syntax

See [DimXpertBestfitPlaneFeature::GetSubFeatures](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertBestfitPlaneFeature~GetSubFeatures.html).

## Examples

[Get DimXpert Width And Best Fit Plane Features Example (VBA)](Get_DimXpert_Width_And_BestFitPlane_Features_Example_VB.htm)
[Get DimXpert Width And Best Fit Plane Features Example (VB.NET)](Get_DimXpert_Width_And_BestFitPlane_Features_Example_VBNET.htm)

## Remarks

This method returns all sub-features of this best fit plane feature. All of the sub-features returned by this method do not appear on the DimXpertManager tab of the Management Panel. Functional geometry sub-features such as planes and cylinders that represent each individual face of a part are for internal use only. These sub-features do not appear in the DimXpertManager tree. However, manufacturing sub-features that are significant for downstream machining and inspection do appear in the DimXpertManager tree.

## See Also

[IDimXpertBestfitPlaneFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertBestfitPlaneFeature.html)
[IDimXpertBestfitPlaneFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertBestfitPlaneFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
