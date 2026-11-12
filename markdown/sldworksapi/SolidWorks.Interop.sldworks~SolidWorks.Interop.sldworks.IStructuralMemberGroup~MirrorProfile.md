---
title: "MirrorProfile Property (IStructuralMemberGroup)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberGroup"
member: "MirrorProfile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~MirrorProfile.html"
---

# MirrorProfile Property (IStructuralMemberGroup)

Gets and sets whether to mirror the profile of this structural-member group.

## Syntax

### Visual Basic (Declaration)

```vb
Property MirrorProfile As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberGroup
Dim value As System.Boolean

instance.MirrorProfile = value

value = instance.MirrorProfile
```

### C#

```csharp
System.bool MirrorProfile {get; set;}
```

### C++/CLI

```cpp
property System.bool MirrorProfile {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to mirror the profile, false to not

## VBA Syntax

See [StructuralMemberGroup::MirrorProfile](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberGroup~MirrorProfile.html).

## Examples

[Insert Structural Weldment (C#)](Insert_Structural_Weldment_Example_CSharp.htm)
[Insert Structural Weldment (VB.NET)](Insert_Structural_Weldment_Example_VBNET.htm)
[Insert Structural Weldment (VBA)](Insert_Structural_Weldment_Example_VB.htm)

## See Also

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.html)
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.html)
[IStructuralMemberGroup::MirrorProfileAxis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~MirrorProfileAxis.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
