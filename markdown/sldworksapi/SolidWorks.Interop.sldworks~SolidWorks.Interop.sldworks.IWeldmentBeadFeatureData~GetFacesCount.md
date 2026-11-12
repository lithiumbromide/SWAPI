---
title: "GetFacesCount Method (IWeldmentBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentBeadFeatureData"
member: "GetFacesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetFacesCount.html"
---

# GetFacesCount Method (IWeldmentBeadFeatureData)

Gets the number of faces in each sets of faces whose intersection defines the edges to which this weld bead is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetFacesCount( _
   ByVal Side As System.Integer, _
   ByRef FaceSet1Count As System.Integer, _
   ByRef FaceSet2Count As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentBeadFeatureData
Dim Side As System.Integer
Dim FaceSet1Count As System.Integer
Dim FaceSet2Count As System.Integer

instance.GetFacesCount(Side, FaceSet1Count, FaceSet2Count)
```

### C#

```csharp
void GetFacesCount(
   System.int Side,
   out System.int FaceSet1Count,
   out System.int FaceSet2Count
)
```

### C++/CLI

```cpp
void GetFacesCount(
   System.int Side,
   [Out] System.int FaceSet1Count,
   [Out] System.int FaceSet2Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Side`: Side as defined in [swWeldBeadSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)
- `FaceSet1Count`: Number of faces in first set of faces
- `FaceSet2Count`: Number of faces in second set of faces

## VBA Syntax

See [WeldmentBeadFeatureData::GetFacesCount](ms-its:sldworksapivb6.chm::/sldworks~WeldmentBeadFeatureData~GetFacesCount.html).

## Remarks

Call this method before calling [IWeldmentBeadFeatureData::IGetFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~IGetFaces.html).

## See Also

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html)
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.html)
[IWeldmentBeadFeatureData::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetFaces.html)
[IWeldmentBeadFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetFaces.html)
[IWeldmentBeadFeatureData::SetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetFaces.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
