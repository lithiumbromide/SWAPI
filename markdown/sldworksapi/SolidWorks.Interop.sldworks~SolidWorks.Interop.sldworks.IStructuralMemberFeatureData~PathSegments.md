---
title: "PathSegments Property (IStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberFeatureData"
member: "PathSegments"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~PathSegments.html"
---

# PathSegments Property (IStructuralMemberFeatureData)

Gets the path segments used or sets the path segments to use to create this structural member.

## Syntax

### Visual Basic (Declaration)

```vb
Property PathSegments As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberFeatureData
Dim value As System.Object

instance.PathSegments = value

value = instance.PathSegments
```

### C#

```csharp
System.object PathSegments {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PathSegments {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [path segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)

## VBA Syntax

See [StructuralMemberFeatureData::PathSegments](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberFeatureData~PathSegments.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html)
[IStructuralMemberFeatureData::GetPathSegmentAt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetPathSegmentAt.html)
[IStructuralMemberFeatureData::GetPathSegmentsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetPathSegmentsCount.html)
[IStructuralMemberFeatureData::IGetPathSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetPathSegments.html)
[IStructuralMemberFeatureData::ISetPathSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ISetPathSegments.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
