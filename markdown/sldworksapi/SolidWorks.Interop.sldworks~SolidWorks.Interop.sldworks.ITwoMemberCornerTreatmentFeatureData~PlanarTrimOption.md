---
title: "PlanarTrimOption Property (ITwoMemberCornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITwoMemberCornerTreatmentFeatureData"
member: "PlanarTrimOption"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData~PlanarTrimOption.html"
---

# PlanarTrimOption Property (ITwoMemberCornerTreatmentFeatureData)

Gets and sets the planar trim option for this two member corner treatment feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PlanarTrimOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITwoMemberCornerTreatmentFeatureData
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

See [TwoMemberCornerTreatmentFeatureData::PlanarTrimOption](ms-its:sldworksapivb6.chm::/sldworks~TwoMemberCornerTreatmentFeatureData~PlanarTrimOption.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## Remarks

This property is valid only if [ITwoMemberCornerTreatmentFeatureData::CornerTreatmentTrimType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData~CornerTreatmentTrimType.html) is set to [swCornerTreatmentTrimType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentTrimType_e.html).swCornerTreatmentTrim_PlanarTrim.

## See Also

[ITwoMemberCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData.html)
[ITwoMemberCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
