---
title: "GetPathSegmentsCount Method (IStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberFeatureData"
member: "GetPathSegmentsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetPathSegmentsCount.html"
---

# GetPathSegmentsCount Method (IStructuralMemberFeatureData)

Gets the number of path segments for this structural member.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPathSegmentsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberFeatureData
Dim value As System.Integer

value = instance.GetPathSegmentsCount()
```

### C#

```csharp
System.int GetPathSegmentsCount()
```

### C++/CLI

```cpp
System.int GetPathSegmentsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of path segments

## VBA Syntax

See [StructuralMemberFeatureData::GetPathSegmentsCount](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberFeatureData~GetPathSegmentsCount.html).

## Remarks

Call this method before calling [IStructuralMemberFeatureData::IGetPathSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberFeatureData~IGetPathSegments.html) to get the size of the array for that method.

## See Also

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html)
[IStructuralMemberFeatureData::PathSegments Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~PathSegments.html)
[IStructuralMemberFeatureData::ISetPathSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ISetPathSegments.html)
[IStructuralMemberFeatureData::GetPathSegmentAt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetPathSegmentAt.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
