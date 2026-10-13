---
title: "GetSubFeatures Method (IDimXpertExtrudeFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertExtrudeFeature"
member: "GetSubFeatures"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature~GetSubFeatures.html"
---

# GetSubFeatures Method (IDimXpertExtrudeFeature)

Gets all of the sub-features of this DimXpert extrude.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSubFeatures() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertExtrudeFeature
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

See [DimXpertExtrudeFeature::GetSubFeatures](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertExtrudeFeature~GetSubFeatures.html).

## Remarks

This method returns all sub-features of this extrude feature. All of the sub-features returned by this method do not appear on the DimXpertManager tab of the Management Panel. Functional geometry sub-features such as planes and cylinders that represent each individual face of a part are for internal use only. These sub-features do not appear in the DimXpertManager tree. However, manufacturing sub-features that are significant for downstream machining and inspection do appear in the DimXpertManager tree.

## See Also

[IDimXpertExtrudeFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature.html)
[IDimXpertExtrudeFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
