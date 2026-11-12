---
title: "AlignmentVector Property (IStructuralMemberGroup)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberGroup"
member: "AlignmentVector"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~AlignmentVector.html"
---

# AlignmentVector Property (IStructuralMemberGroup)

Gets and sets a reference vector for this structural-member group.

## Syntax

### Visual Basic (Declaration)

```vb
Property AlignmentVector As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberGroup
Dim value As System.Object

instance.AlignmentVector = value

value = instance.AlignmentVector
```

### C#

```csharp
System.object AlignmentVector {get; set;}
```

### C++/CLI

```cpp
property System.Object^ AlignmentVector {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Object in the model that provides location and direction in aligning this structural-member group

## VBA Syntax

See [StructuralMemberGroup::AlignmentVector](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberGroup~AlignmentVector.html).

## See Also

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.html)
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
