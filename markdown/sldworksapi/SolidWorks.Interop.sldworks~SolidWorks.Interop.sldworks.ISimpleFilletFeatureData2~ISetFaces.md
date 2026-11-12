---
title: "ISetFaces Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "ISetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetFaces.html"
---

# ISetFaces Method (ISimpleFilletFeatureData2)

Sets the faces on which to create a simple radius fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetFaces( _
   ByVal WhichFaceList As System.Integer, _
   ByVal Count As System.Integer, _
   ByRef FaceList As Face2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim WhichFaceList As System.Integer
Dim Count As System.Integer
Dim FaceList As Face2

instance.ISetFaces(WhichFaceList, Count, FaceList)
```

### C#

```csharp
void ISetFaces(
   System.int WhichFaceList,
   System.int Count,
   ref Face2 FaceList
)
```

### C++/CLI

```cpp
void ISetFaces(
   System.int WhichFaceList,
   System.int Count,
   Face2^% FaceList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichFaceList`: Face as defined in [swSimpleFilletWhichFaces_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSimpleFilletWhichFaces_e.html)
- `Count`: Number of faces
- `FaceList`: - in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetFaceCount.html)
[ISimpleFilletFeatureData2::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetFaces.html)
[ISimpleFilletFeatureData2::SetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetFaces.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
