---
title: "CornerTreatmentType Property (IStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberFeatureData"
member: "CornerTreatmentType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~CornerTreatmentType.html"
---

# CornerTreatmentType Property (IStructuralMemberFeatureData)

Gets or sets the type of corner treatment for this structural member.

## Syntax

### Visual Basic (Declaration)

```vb
Property CornerTreatmentType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberFeatureData
Dim value As System.Integer

instance.CornerTreatmentType = value

value = instance.CornerTreatmentType
```

### C#

```csharp
System.int CornerTreatmentType {get; set;}
```

### C++/CLI

```cpp
property System.int CornerTreatmentType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of corner treatment as defined in [swSolidworksWeldmentEndCondOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSolidworksWeldmentEndCondOptions_e.html)

## VBA Syntax

See [StructuralMemberFeatureData::CornerTreatmentType](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberFeatureData~CornerTreatmentType.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html)
[IStructuralMemberFeatureData::ApplyCornerTreatment Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ApplyCornerTreatment.html)
[IStructuralMemberFeatureData::ConnectionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ConnectionType.html)
[IStructuralMemberFeatureData::GetConnectionPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetConnectionPoints.html)
[IStructuralMemberFeatureData::GetConnectionPointsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetConnectionPointsCount.html)
[IStructuralMemberFeatureData::IGetConnectionPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetConnectionPoints.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
