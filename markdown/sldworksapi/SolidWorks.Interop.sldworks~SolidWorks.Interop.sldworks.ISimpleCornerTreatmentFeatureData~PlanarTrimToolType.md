---
title: "PlanarTrimToolType Property (ISimpleCornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimpleCornerTreatmentFeatureData"
member: "PlanarTrimToolType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData~PlanarTrimToolType.html"
---

# PlanarTrimToolType Property (ISimpleCornerTreatmentFeatureData)

Gets and sets the planar trim tool type for this simple corner treatment feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PlanarTrimToolType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleCornerTreatmentFeatureData
Dim value As System.Integer

instance.PlanarTrimToolType = value

value = instance.PlanarTrimToolType
```

### C#

```csharp
System.int PlanarTrimToolType {get; set;}
```

### C++/CLI

```cpp
property System.int PlanarTrimToolType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Planar trim tool type as defined by [swCornerTreatmentPlanarTrimToolType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentPlanarTrimToolType_e.html)

## VBA Syntax

See [SimpleCornerTreatmentFeatureData::PlanarTrimToolType](ms-its:sldworksapivb6.chm::/sldworks~SimpleCornerTreatmentFeatureData~PlanarTrimToolType.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## See Also

[ISimpleCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData.html)
[ISimpleCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
