---
title: "ApplyCornerTreatment Property (IStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberFeatureData"
member: "ApplyCornerTreatment"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ApplyCornerTreatment.html"
---

# ApplyCornerTreatment Property (IStructuralMemberFeatureData)

Gets or sets whether or not to apply a corner treatment to this structural member.

## Syntax

### Visual Basic (Declaration)

```vb
Property ApplyCornerTreatment As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberFeatureData
Dim value As System.Boolean

instance.ApplyCornerTreatment = value

value = instance.ApplyCornerTreatment
```

### C#

```csharp
System.bool ApplyCornerTreatment {get; set;}
```

### C++/CLI

```cpp
property System.bool ApplyCornerTreatment {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to apply corner treatment, false to not (see Remarks)

## VBA Syntax

See [StructuralMemberFeatureData::ApplyCornerTreatment](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberFeatureData~ApplyCornerTreatment.html).

## Remarks

You must specify the [type corner treatment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberFeatureData~CornerTreatmentType.html) before changing this property from false to true.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html)
[IStructuralMemberFeatureData::ConnectionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ConnectionType.html)
[IStructuralMemberFeatureData::CornerTreatmentType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~CornerTreatmentType.html)
[IStructuralMemberFeatureData::GetConnectionPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetConnectionPoints.html)
[IStructuralMemberFeatureData::GetConnectionPointsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetConnectionPointsCount.html)
[IStructuralMemberFeatureData::IGetConnectionPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetConnectionPoints.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
