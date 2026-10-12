---
title: "CornerTreatmentTrimType Property (ITwoMemberCornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITwoMemberCornerTreatmentFeatureData"
member: "CornerTreatmentTrimType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData~CornerTreatmentTrimType.html"
---

# CornerTreatmentTrimType Property (ITwoMemberCornerTreatmentFeatureData)

Gets and sets the corner treatment trim type for this two member corner treatment feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CornerTreatmentTrimType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITwoMemberCornerTreatmentFeatureData
Dim value As System.Integer

instance.CornerTreatmentTrimType = value

value = instance.CornerTreatmentTrimType
```

### C#

```csharp
System.int CornerTreatmentTrimType {get; set;}
```

### C++/CLI

```cpp
property System.int CornerTreatmentTrimType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Corner treatment trim type as defined by [swCornerTreatmentTrimType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentTrimType_e.html)

## VBA Syntax

See [TwoMemberCornerTreatmentFeatureData::CornerTreatmentTrimType](ms-its:sldworksapivb6.chm::/sldworks~TwoMemberCornerTreatmentFeatureData~CornerTreatmentTrimType.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## See Also

[ITwoMemberCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData.html)
[ITwoMemberCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
