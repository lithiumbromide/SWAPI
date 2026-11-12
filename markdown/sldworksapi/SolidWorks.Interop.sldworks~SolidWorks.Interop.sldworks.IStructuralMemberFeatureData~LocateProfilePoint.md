---
title: "LocateProfilePoint Property (IStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberFeatureData"
member: "LocateProfilePoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~LocateProfilePoint.html"
---

# LocateProfilePoint Property (IStructuralMemberFeatureData)

Gets or sets the point to use to locate the profile for this structural member.

## Syntax

### Visual Basic (Declaration)

```vb
Property LocateProfilePoint As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberFeatureData
Dim value As SketchPoint

instance.LocateProfilePoint = value

value = instance.LocateProfilePoint
```

### C#

```csharp
SketchPoint LocateProfilePoint {get; set;}
```

### C++/CLI

```cpp
property SketchPoint^ LocateProfilePoint {
   SketchPoint^ get();
   void set (    SketchPoint^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) to use to locate the profile

## VBA Syntax

See [StructuralMemberFeatureData::LocateProfilePoint](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberFeatureData~LocateProfilePoint.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html)
[IStructuralMemberFeatureData::WeldmentProfilePath Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~WeldmentProfilePath.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
