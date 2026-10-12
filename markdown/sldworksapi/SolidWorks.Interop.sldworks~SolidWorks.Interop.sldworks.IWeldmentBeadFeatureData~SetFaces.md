---
title: "SetFaces Method (IWeldmentBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentBeadFeatureData"
member: "SetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetFaces.html"
---

# SetFaces Method (IWeldmentBeadFeatureData)

Sets the faces to which to apply the weld bead.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFaces( _
   ByVal Side As System.Integer, _
   ByVal FaceSet1 As System.Object, _
   ByVal FaceSet2 As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentBeadFeatureData
Dim Side As System.Integer
Dim FaceSet1 As System.Object
Dim FaceSet2 As System.Object
Dim value As System.Boolean

value = instance.SetFaces(Side, FaceSet1, FaceSet2)
```

### C#

```csharp
System.bool SetFaces(
   System.int Side,
   System.object FaceSet1,
   System.object FaceSet2
)
```

### C++/CLI

```cpp
System.bool SetFaces(
   System.int Side,
   System.Object^ FaceSet1,
   System.Object^ FaceSet2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Side`: Side as defined in [swWeldBeadSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)
- `FaceSet1`: First set of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to which to apply the weld bead
- `FaceSet2`: Second set of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to which to apply the weld bead

### Return Value

True if the weld bead is applied to the specified faces, false if not

## VBA Syntax

See [WeldmentBeadFeatureData::SetFaces](ms-its:sldworksapivb6.chm::/sldworks~WeldmentBeadFeatureData~SetFaces.html).

## Examples

[Change Weld Bead Faces (VBA)](Change_Weld_Bead_Faces_Example_VB.htm)

## Remarks

Although you must select planar faces for the face sets, fillet weld beads can follow non-planar, tangent contours when you set [IWeldmentBeadFeatureData::TangentPropagation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~TangentPropagation.html) to TRUE.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html)
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.html)
[IWeldmentBeadFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetFaces.html)
[IWeldmentBeadFeatureData::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~IGetFaces.html)
[IWeldmentBeadFeatureData::GetFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetFacesCount.html)
[IWeldmentBeadFeatureData::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetFaces.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
