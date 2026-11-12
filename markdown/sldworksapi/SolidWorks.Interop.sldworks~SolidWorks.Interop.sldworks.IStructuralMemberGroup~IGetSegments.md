---
title: "IGetSegments Method (IStructuralMemberGroup)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberGroup"
member: "IGetSegments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~IGetSegments.html"
---

# IGetSegments Method (IStructuralMemberGroup)

Gets the sketch segments in this structural-member group.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSegments( _
   ByVal Count As System.Integer _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberGroup
Dim Count As System.Integer
Dim value As SketchSegment

value = instance.IGetSegments(Count)
```

### C#

```csharp
SketchSegment IGetSegments(
   System.int Count
)
```

### C++/CLI

```cpp
SketchSegment^ IGetSegments(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of sketch segments

### Return Value

- in-process, unmanaged C++: Pointer to an array of [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before using this method, call [IStructuralMemberGroup::GetSegmentsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberGroup~GetSegmentsCount.html) to populate the `Count` parameter.

## See Also

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.html)
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.html)
[IStructuralMemberGroup::ISetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~ISetSegments.html)
[IStructuralMemberGroup::Segments Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~Segments.html)

## Availability

SOLIDWORKS 2009 SP5, Revision Number 17.5
