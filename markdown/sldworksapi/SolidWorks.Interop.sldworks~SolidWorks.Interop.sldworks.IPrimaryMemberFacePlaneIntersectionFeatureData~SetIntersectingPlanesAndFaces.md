---
title: "SetIntersectingPlanesAndFaces Method (IPrimaryMemberFacePlaneIntersectionFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberFacePlaneIntersectionFeatureData"
member: "SetIntersectingPlanesAndFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData~SetIntersectingPlanesAndFaces.html"
---

# SetIntersectingPlanesAndFaces Method (IPrimaryMemberFacePlaneIntersectionFeatureData)

Sets the planes, surfaces, and faces that intersect with parameter faces of this structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetIntersectingPlanesAndFaces( _
   ByVal RefList As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberFacePlaneIntersectionFeatureData
Dim RefList As System.Object
Dim value As System.Boolean

value = instance.SetIntersectingPlanesAndFaces(RefList)
```

### C#

```csharp
System.bool SetIntersectingPlanesAndFaces(
   System.object RefList
)
```

### C++/CLI

```cpp
System.bool SetIntersectingPlanesAndFaces(
   System.Object^ RefList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RefList`: Array of [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)s, [ISurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)s, and/or [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)s that intersect with parameter faces

### Return Value

True if intersecting objects successfully set, false if not

## VBA Syntax

See [PrimaryMemberFacePlaneIntersectionFeatureData::SetIntersectingPlanesAndFaces](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberFacePlaneIntersectionFeatureData~SetIntersectingPlanesAndFaces.html).

## Examples

See the [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.html) examples.

## Remarks

Entities passed should intersect with at least one entity returned by [IPrimaryMemberFacePlaneIntersectionFeatureData::GetParameterFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData~GetParameterFaces.html).

At edit time, you can set only one intersecting entity.

## See Also

[IPrimaryMemberFacePlaneIntersectionFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.html)
[IPrimaryMemberFacePlaneIntersectionFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
