---
title: "PlanarTrimOption Property (ISimpleCornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimpleCornerTreatmentFeatureData"
member: "PlanarTrimOption"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData~PlanarTrimOption.html"
---

# PlanarTrimOption Property (ISimpleCornerTreatmentFeatureData)

Gets and sets the planar trim option for this simple corner treatment feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PlanarTrimOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleCornerTreatmentFeatureData
Dim value As System.Integer

instance.PlanarTrimOption = value

value = instance.PlanarTrimOption
```

### C#

```csharp
System.int PlanarTrimOption {get; set;}
```

### C++/CLI

```cpp
property System.int PlanarTrimOption {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Planar trim option as defined by [swCornerTreatmentPlanarTrimOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentPlanarTrimOptions_e.html)

## VBA Syntax

See [SimpleCornerTreatmentFeatureData::PlanarTrimOption](ms-its:sldworksapivb6.chm::/sldworks~SimpleCornerTreatmentFeatureData~PlanarTrimOption.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## Remarks

This property is valid only if:

- [ISimpleCornerTreatmentFeatureData::CornerTreatmentTrimType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData~CornerTreatmentTrimType.html) is set to [swCornerTreatmentTrimType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentTrimType_e.html).swCornerTreatmentTrim_PlanarTrim.

-and -

- ISimpleCornerTreatmentFeatureData::PlanarTrimToolType is set to [swCornerTreatmentPlanarTrimToolType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentPlanarTrimToolType_e.html).swCornerTreatmentPlanarTrimTool_Automatic.

## See Also

[ISimpleCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData.html)
[ISimpleCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
