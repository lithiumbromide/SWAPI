---
title: "IGetPathSegments Method (IStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberFeatureData"
member: "IGetPathSegments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetPathSegments.html"
---

# IGetPathSegments Method (IStructuralMemberFeatureData)

Gets the path segments used to create this structural member.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPathSegments( _
   ByVal Count As System.Integer _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberFeatureData
Dim Count As System.Integer
Dim value As SketchSegment

value = instance.IGetPathSegments(Count)
```

### C#

```csharp
SketchSegment IGetPathSegments(
   System.int Count
)
```

### C++/CLI

```cpp
SketchSegment^ IGetPathSegments(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of path segments

### Return Value

- in-process, unmanaged C++: Pointer to an array of [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IStructuralMemberFeatureData::GetPathSegmentsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberFeatureData~GetPathSegmentsCount.html) before calling this method to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html)
[IStructuralMemberFeatureData::PathSegments Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~PathSegments.html)
[IStructuralMemberFeatureData::ISetPathSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ISetPathSegments.html)
[IStructuralMemberFeatureData::GetPathSegmentsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetPathSegmentsCount.html)
[IStructuralMemberFeatureData::GetPathSegmentAt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetPathSegmentAt.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
