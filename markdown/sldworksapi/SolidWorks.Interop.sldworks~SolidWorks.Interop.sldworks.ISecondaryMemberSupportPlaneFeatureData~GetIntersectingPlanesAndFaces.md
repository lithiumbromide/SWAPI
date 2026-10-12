---
title: "GetIntersectingPlanesAndFaces Method (ISecondaryMemberSupportPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberSupportPlaneFeatureData"
member: "GetIntersectingPlanesAndFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData~GetIntersectingPlanesAndFaces.html"
---

# GetIntersectingPlanesAndFaces Method (ISecondaryMemberSupportPlaneFeatureData)

Gets the planar entities that intersect the primary structure system member pairs used to create this secondary structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIntersectingPlanesAndFaces() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberSupportPlaneFeatureData
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

See [SecondaryMemberSupportPlaneFeatureData::GetIntersectingPlanesAndFaces](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberSupportPlaneFeatureData~GetIntersectingPlanesAndFaces.html).

## See Also

[ISecondaryMemberSupportPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData.html)
[ISecondaryMemberSupportPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
