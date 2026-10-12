---
title: "LocateProfilePoint Property (IStructuralMemberGroup)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberGroup"
member: "LocateProfilePoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~LocateProfilePoint.html"
---

# LocateProfilePoint Property (IStructuralMemberGroup)

Gets and sets the point to use to locate the profile for this structural-member group.

## Syntax

### Visual Basic (Declaration)

```vb
Property LocateProfilePoint As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberGroup
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

See [StructuralMemberGroup::LocateProfilePoint](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberGroup~LocateProfilePoint.html).

## Remarks

This property can be set only after creating the structural-member group.

## See Also

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.html)
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
