---
title: "GetFaces Method (IWeldmentBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentBeadFeatureData"
member: "GetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetFaces.html"
---

# GetFaces Method (IWeldmentBeadFeatureData)

Gets the sets of faces whose edges intersection defines the edges to which the weld bead is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetFaces( _
   ByVal Side As System.Integer, _
   ByRef FaceSet1 As System.Object, _
   ByRef FaceSet2 As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentBeadFeatureData
Dim Side As System.Integer
Dim FaceSet1 As System.Object
Dim FaceSet2 As System.Object

instance.GetFaces(Side, FaceSet1, FaceSet2)
```

### C#

```csharp
void GetFaces(
   System.int Side,
   out System.object FaceSet1,
   out System.object FaceSet2
)
```

### C++/CLI

```cpp
void GetFaces(
   System.int Side,
   [Out] System.Object^ FaceSet1,
   [Out] System.Object^ FaceSet2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Side`: Side as defined in [swWeldBeadSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)
- `FaceSet1`: First set of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)
- `FaceSet2`: Second set of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [WeldmentBeadFeatureData::GetFaces](ms-its:sldworksapivb6.chm::/sldworks~WeldmentBeadFeatureData~GetFaces.html).

## Examples

See the [IWeldmentBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html) examples.

## Remarks

After using this method, use [IWeldmentBeadFeatureData::GetVirtualEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdges.html) to get the new intersections. Then use [IWeldmentBeadFeatureData::SetVirtualEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~SetVirtualEdges.html) to specify the edges to which you want the weld bead applied. By default, [IWeldmentBeadFeatureData::SetFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~SetFaces.html) creates the bead on all virtual edges. [IWeldmentBeadFeatureData::SetVirtualEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~SetVirtualEdges.html) lets
you exclude any of these edges.

## See Also

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html)
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.html)
[IWeldmentBeadFeatureData::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~IGetFaces.html)
[IWeldmentBeadFeatureData::GetFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetFacesCount.html)
[IWeldmentBeadFeatureData::SetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetFaces.html)
[IWeldmentBeadFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetFaces.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
