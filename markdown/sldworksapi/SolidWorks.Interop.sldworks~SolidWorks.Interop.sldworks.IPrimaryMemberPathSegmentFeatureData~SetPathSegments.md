---
title: "SetPathSegments Method (IPrimaryMemberPathSegmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberPathSegmentFeatureData"
member: "SetPathSegments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData~SetPathSegments.html"
---

# SetPathSegments Method (IPrimaryMemberPathSegmentFeatureData)

Gets the path segments, curves, and edges to create the structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPathSegments( _
   ByVal PathSegments As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberPathSegmentFeatureData
Dim PathSegments As System.Object
Dim value As System.Boolean

value = instance.SetPathSegments(PathSegments)
```

### C#

```csharp
System.bool SetPathSegments(
   System.object PathSegments
)
```

### C++/CLI

```cpp
System.bool SetPathSegments(
   System.Object^ PathSegments
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PathSegments`: Array of [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)s, [IReferenceCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.html)s, and/or [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)s

### Return Value

True if path segments successfully set, false if not

## VBA Syntax

See [PrimaryMemberPathSegmentFeatureData::SetPathSegments](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberPathSegmentFeatureData~SetPathSegments.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

See the [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.html) examples.

## Remarks

For .NET applications, you must marshal the PathSegments array to IDispatch object arrays before calling this method. See [IDispatch Object Arrays as Input in .NET](ms-its:sldworksapiprogguide.chm::/Overview/IDispatch_Object_Arrays_as_Input_in_.NET.htm).

## See Also

[IPrimaryMemberPathSegmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.html)
[IPrimaryMemberPathSegmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
