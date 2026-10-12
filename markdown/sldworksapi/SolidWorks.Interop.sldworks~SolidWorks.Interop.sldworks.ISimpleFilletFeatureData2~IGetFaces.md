---
title: "IGetFaces Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "IGetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetFaces.html"
---

# IGetFaces Method (ISimpleFilletFeatureData2)

Gets the faces on which to create a simple radius fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFaces( _
   ByVal WhichFaceList As System.Integer, _
   ByVal Count As System.Integer _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim WhichFaceList As System.Integer
Dim Count As System.Integer
Dim value As Face2

value = instance.IGetFaces(WhichFaceList, Count)
```

### C#

```csharp
Face2 IGetFaces(
   System.int WhichFaceList,
   System.int Count
)
```

### C++/CLI

```cpp
Face2^ IGetFaces(
   System.int WhichFaceList,
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichFaceList`: Face as defined in [swSimpleFilletWhichFaces_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSimpleFilletWhichFaces_e.html)
- `Count`: Number of faces

### Return Value

- in-process in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISimpleFilletFeatureData2::GetFaceCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~GetFaceCount.html) before this method to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetFaces.html)
[ISimpleFilletFeatureData2::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetFaces.html)
[ISimpleFilletFeatureData2::SetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetFaces.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
