---
title: "SetIntersectingPlanesAndFaces Method (ISecondaryMemberSupportPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberSupportPlaneFeatureData"
member: "SetIntersectingPlanesAndFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData~SetIntersectingPlanesAndFaces.html"
---

# SetIntersectingPlanesAndFaces Method (ISecondaryMemberSupportPlaneFeatureData)

Sets the planar entities that intersect the primary structure system member pairs used to create this secondary structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetIntersectingPlanesAndFaces( _
   ByVal RefArray As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberSupportPlaneFeatureData
Dim RefArray As System.Object
Dim value As System.Boolean

value = instance.SetIntersectingPlanesAndFaces(RefArray)
```

### C#

```csharp
System.bool SetIntersectingPlanesAndFaces(
   System.object RefArray
)
```

### C++/CLI

```cpp
System.bool SetIntersectingPlanesAndFaces(
   System.Object^ RefArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RefArray`: Array of [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)s, [ISurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)s, and/or [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)s

### Return Value

True if intersecting planes and faces successfully set, false if not

## VBA Syntax

See [SecondaryMemberSupportPlaneFeatureData::SetIntersectingPlanesAndFaces](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberSupportPlaneFeatureData~SetIntersectingPlanesAndFaces.html).

## Examples

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html) examples.

## Remarks

During editing, RefArray can hold only one entity.

## See Also

[ISecondaryMemberSupportPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData.html)
[ISecondaryMemberSupportPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
