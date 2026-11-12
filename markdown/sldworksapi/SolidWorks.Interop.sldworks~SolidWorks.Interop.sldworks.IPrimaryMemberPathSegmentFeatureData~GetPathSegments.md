---
title: "GetPathSegments Method (IPrimaryMemberPathSegmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberPathSegmentFeatureData"
member: "GetPathSegments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData~GetPathSegments.html"
---

# GetPathSegments Method (IPrimaryMemberPathSegmentFeatureData)

Gets the path segments, curves, and edges used to create the structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPathSegments() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberPathSegmentFeatureData
Dim value As System.Object

value = instance.GetPathSegments()
```

### C#

```csharp
System.object GetPathSegments()
```

### C++/CLI

```cpp
System.Object^ GetPathSegments();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)s, [IReferenceCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.html)s, and/or [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)s

## VBA Syntax

See [PrimaryMemberPathSegmentFeatureData::GetPathSegments](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberPathSegmentFeatureData~GetPathSegments.html).

## See Also

[IPrimaryMemberPathSegmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.html)
[IPrimaryMemberPathSegmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
