---
title: "MiterTrimPlanePoint Property (ITwoMemberCornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITwoMemberCornerTreatmentFeatureData"
member: "MiterTrimPlanePoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData~MiterTrimPlanePoint.html"
---

# MiterTrimPlanePoint Property (ITwoMemberCornerTreatmentFeatureData)

Gets and sets the point through which to create the miter trim for this two member corner treatment feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property MiterTrimPlanePoint As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITwoMemberCornerTreatmentFeatureData
Dim value As System.Object

instance.MiterTrimPlanePoint = value

value = instance.MiterTrimPlanePoint
```

### C#

```csharp
System.object MiterTrimPlanePoint {get; set;}
```

### C++/CLI

```cpp
property System.Object^ MiterTrimPlanePoint {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IRefPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.html)

## VBA Syntax

See [TwoMemberCornerTreatmentFeatureData::MiterTrimPlanePoint](ms-its:sldworksapivb6.chm::/sldworks~TwoMemberCornerTreatmentFeatureData~MiterTrimPlanePoint.html).

## Remarks

This property is valid only if [ITwoMemberCornerTreatmentFeatureData::CornerTreatmentTrimType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData~CornerTreatmentTrimType.html) is set to [swCornerTreatmentTrimType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentTrimType_e.html).swCornerTreatmentTrim_MiterTrim.

## See Also

[ITwoMemberCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData.html)
[ITwoMemberCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
