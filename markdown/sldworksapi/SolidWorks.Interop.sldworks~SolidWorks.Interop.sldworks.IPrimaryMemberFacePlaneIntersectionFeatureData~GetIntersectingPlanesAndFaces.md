---
title: "GetIntersectingPlanesAndFaces Method (IPrimaryMemberFacePlaneIntersectionFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberFacePlaneIntersectionFeatureData"
member: "GetIntersectingPlanesAndFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData~GetIntersectingPlanesAndFaces.html"
---

# GetIntersectingPlanesAndFaces Method (IPrimaryMemberFacePlaneIntersectionFeatureData)

Gets the planes, surfaces, and faces that intersect with parameter faces of this structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIntersectingPlanesAndFaces() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberFacePlaneIntersectionFeatureData
Dim value As System.Object

value = instance.GetIntersectingPlanesAndFaces()
```

### C#

```csharp
System.object GetIntersectingPlanesAndFaces()
```

### C++/CLI

```cpp
System.Object^ GetIntersectingPlanesAndFaces();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)s, [ISurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)s, and/or [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)s

## VBA Syntax

See [PrimaryMemberFacePlaneIntersectionFeatureData::GetIntersectingPlanesAndFaces](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberFacePlaneIntersectionFeatureData~GetIntersectingPlanesAndFaces.html).

## See Also

[IPrimaryMemberFacePlaneIntersectionFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.html)
[IPrimaryMemberFacePlaneIntersectionFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
