---
title: "PlanarTrimOption Property (IComplexCornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IComplexCornerTreatmentFeatureData"
member: "PlanarTrimOption"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~PlanarTrimOption.html"
---

# PlanarTrimOption Property (IComplexCornerTreatmentFeatureData)

Gets and sets the planar trim option for this complex corner treatment feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PlanarTrimOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComplexCornerTreatmentFeatureData
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

See [ComplexCornerTreatmentFeatureData::PlanarTrimOption](ms-its:sldworksapivb6.chm::/sldworks~ComplexCornerTreatmentFeatureData~PlanarTrimOption.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## Remarks

This property is valid only if [IComplexCornerTreatmentFeatureData::PlanarTrimToolType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~PlanarTrimToolType.html) is set to [swCornerTreatmentPlanarTrimToolType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentPlanarTrimToolType_e.html).swAutomatic.

## See Also

[IComplexCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData.html)
[IComplexCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
