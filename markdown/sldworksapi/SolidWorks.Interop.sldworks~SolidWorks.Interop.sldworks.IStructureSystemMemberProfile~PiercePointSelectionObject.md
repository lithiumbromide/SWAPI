---
title: "PiercePointSelectionObject Property (IStructureSystemMemberProfile)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberProfile"
member: "PiercePointSelectionObject"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~PiercePointSelectionObject.html"
---

# PiercePointSelectionObject Property (IStructureSystemMemberProfile)

Gets and sets the selected pierce point object for the sketch of this member profile.

## Syntax

### Visual Basic (Declaration)

```vb
Property PiercePointSelectionObject As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberProfile
Dim value As System.Object

instance.PiercePointSelectionObject = value

value = instance.PiercePointSelectionObject
```

### C#

```csharp
System.object PiercePointSelectionObject {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PiercePointSelectionObject {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)

## VBA Syntax

See [StructureSystemMemberProfile::PiercePointSelectionObject](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberProfile~PiercePointSelectionObject.html).

## Remarks

This property is valid only if [IStructureSystemMemberProfile::ProfilePiercePointType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfilePiercePointType.html) is set to [swStructureProfilePiercePointType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStructureProfilePiercePointType_e.html).Selection.

## See Also

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.html)
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
