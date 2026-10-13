---
title: "IGetFaces Method (IWeldmentBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentBeadFeatureData"
member: "IGetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~IGetFaces.html"
---

# IGetFaces Method (IWeldmentBeadFeatureData)

Gets the sets of faces whose edges intersection defines the edges to which the weld bead is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetFaces( _
   ByVal Side As System.Integer, _
   ByVal Count1 As System.Integer, _
   ByRef FaceSet1 As Face2, _
   ByVal Count2 As System.Integer, _
   ByRef FaceSet2 As Face2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentBeadFeatureData
Dim Side As System.Integer
Dim Count1 As System.Integer
Dim FaceSet1 As Face2
Dim Count2 As System.Integer
Dim FaceSet2 As Face2

instance.IGetFaces(Side, Count1, FaceSet1, Count2, FaceSet2)
```

### C#

```csharp
void IGetFaces(
   System.int Side,
   System.int Count1,
   out Face2 FaceSet1,
   System.int Count2,
   out Face2 FaceSet2
)
```

### C++/CLI

```cpp
void IGetFaces(
   System.int Side,
   System.int Count1,
   [Out] Face2^ FaceSet1,
   System.int Count2,
   [Out] Face2^ FaceSet2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Side`: Side as defined in [swWeldBeadSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)
- `Count1`: Number of faces in first set of faces
- `FaceSet1`: - in-process, unmanaged C++: Pointer to an array of the first set of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `Count2`: Number of faces in second set of faces
- `FaceSet2`: - in-process, unmanaged C++: Pointer to an array of the second set of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Before calling this method, call [IWeldmentBeadFeatureData::GetFacesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~GetFacesCount.html).

After using this method, use [IWeldmentBeadFeatureData::IGetVirtualEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~IGetVirtualEdges.html) to get the new intersections. Then use [IWeldmentBeadFeatureData::ISetVirtualEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~ISetVirtualEdges.html) to specify the edges to which you want the weld bead applied. By default, WeldmentBeadFeatureData::SetFaces creates the bead on all virtual edges. IWeldmentBeadFeatureData::ISetVirtualEdges lets you exclude any of these edges.

## See Also

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html)
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.html)
[IWeldmentBeadFeatureData::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetFaces.html)
[IWeldmentBeadFeatureData::GetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdges.html)
[IWeldmentBeadFeatureData::GetVirtualEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdgesCount.html)
[IWeldmentBeadFeatureData::SetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetFaces.html)
[IWeldmentBeadFeatureData::SetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetVirtualEdges.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
