---
title: "ISetPathSegments Method (IStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberFeatureData"
member: "ISetPathSegments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ISetPathSegments.html"
---

# ISetPathSegments Method (IStructuralMemberFeatureData)

Sets the path segments to use to create this structural member.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetPathSegments( _
   ByVal Count As System.Integer, _
   ByRef SegArr As SketchSegment _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberFeatureData
Dim Count As System.Integer
Dim SegArr As SketchSegment

instance.ISetPathSegments(Count, SegArr)
```

### C#

```csharp
void ISetPathSegments(
   System.int Count,
   ref SketchSegment SegArr
)
```

### C++/CLI

```cpp
void ISetPathSegments(
   System.int Count,
   SketchSegment^% SegArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of path segments
- `SegArr`: - in-process, unmanaged C++: Pointer to an array of [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html)
[IStructuralMemberFeatureData::GetPathSegmentAt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetPathSegmentAt.html)
[IStructuralMemberFeatureData::GetPathSegmentsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetPathSegmentsCount.html)
[IStructuralMemberFeatureData::IGetPathSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetPathSegments.html)
[IStructuralMemberFeatureData::PathSegments Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~PathSegments.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
