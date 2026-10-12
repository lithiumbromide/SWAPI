---
title: "ISetFaces Method (IWeldmentBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentBeadFeatureData"
member: "ISetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetFaces.html"
---

# ISetFaces Method (IWeldmentBeadFeatureData)

Sets the faces to which to apply the weld bead.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetFaces( _
   ByVal Side As System.Integer, _
   ByVal Count1 As System.Integer, _
   ByRef FaceSet1 As Face2, _
   ByVal Count2 As System.Integer, _
   ByRef FaceSet2 As Face2 _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentBeadFeatureData
Dim Side As System.Integer
Dim Count1 As System.Integer
Dim FaceSet1 As Face2
Dim Count2 As System.Integer
Dim FaceSet2 As Face2
Dim value As System.Boolean

value = instance.ISetFaces(Side, Count1, FaceSet1, Count2, FaceSet2)
```

### C#

```csharp
System.bool ISetFaces(
   System.int Side,
   System.int Count1,
   ref Face2 FaceSet1,
   System.int Count2,
   ref Face2 FaceSet2
)
```

### C++/CLI

```cpp
System.bool ISetFaces(
   System.int Side,
   System.int Count1,
   Face2^% FaceSet1,
   System.int Count2,
   Face2^% FaceSet2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Side`: Side as defined in [swWeldBeadSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)
- `Count1`: Number of faces in the first set of faces
- `FaceSet1`: - in-process, unmanaged C++: Pointer to an array of the first set of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `Count2`: Number of faces in the second set of faces
- `FaceSet2`: - in-process, unmanaged C++: Pointer to an array of the second set of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

### Return Value

True if the weld bead is applied to the specified faces, false if not

## Remarks

Although you must select planar faces for the face sets, fillet weld beads can follow non-planar, tangent contours when you set [IWeldmentBeadFeatureData::TangentPropagation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~TangentPropagation.html) to TRUE.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html)
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.html)
[IWeldmentBeadFeatureData::SetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetFaces.html)
[IWeldmentBeadFeatureData::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~IGetFaces.html)
[IWeldmentBeadFeatureData::GetFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetFacesCount.html)
[IWeldmentBeadFeatureData::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetFaces.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
