---
title: "PlanarTrimToolType Property (IComplexCornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IComplexCornerTreatmentFeatureData"
member: "PlanarTrimToolType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~PlanarTrimToolType.html"
---

# PlanarTrimToolType Property (IComplexCornerTreatmentFeatureData)

Gets and sets the planar trim tool type for this complex corner treatment feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PlanarTrimToolType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComplexCornerTreatmentFeatureData
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

See [ComplexCornerTreatmentFeatureData::PlanarTrimToolType](ms-its:sldworksapivb6.chm::/sldworks~ComplexCornerTreatmentFeatureData~PlanarTrimToolType.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## See Also

[IComplexCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData.html)
[IComplexCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
