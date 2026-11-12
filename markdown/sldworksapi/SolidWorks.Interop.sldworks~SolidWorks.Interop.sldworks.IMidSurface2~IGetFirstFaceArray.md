---
title: "IGetFirstFaceArray Method (IMidSurface2)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface2"
member: "IGetFirstFaceArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstFaceArray.html"
---

# IGetFirstFaceArray Method (IMidSurface2)

Obsolete. Superseded by [IMidSurface3::IGetFirstFaceArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~IGetFirstFaceArray.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstFaceArray( _
   ByRef FromFrontFaceListDisp As Face2, _
   ByRef SizeOfFrontFaceList As System.Integer, _
   ByRef FromFaceBackListDisp As Face2, _
   ByRef SizeOfBackFaceList As System.Integer, _
   ByRef Thickness As System.Double _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface2
Dim FromFrontFaceListDisp As Face2
Dim SizeOfFrontFaceList As System.Integer
Dim FromFaceBackListDisp As Face2
Dim SizeOfBackFaceList As System.Integer
Dim Thickness As System.Double
Dim value As Face2

value = instance.IGetFirstFaceArray(FromFrontFaceListDisp, SizeOfFrontFaceList, FromFaceBackListDisp, SizeOfBackFaceList, Thickness)
```

### C#

```csharp
Face2 IGetFirstFaceArray(
   out Face2 FromFrontFaceListDisp,
   out System.int SizeOfFrontFaceList,
   out Face2 FromFaceBackListDisp,
   out System.int SizeOfBackFaceList,
   out System.double Thickness
)
```

### C++/CLI

```cpp
Face2^ IGetFirstFaceArray(
   [Out] Face2^ FromFrontFaceListDisp,
   [Out] System.int SizeOfFrontFaceList,
   [Out] Face2^ FromFaceBackListDisp,
   [Out] System.int SizeOfBackFaceList,
   [Out] System.double Thickness
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FromFrontFaceListDisp`: List of front [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)
- `SizeOfFrontFaceList`: Number of front faces
- `FromFaceBackListDisp`: List of back [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)
- `SizeOfBackFaceList`: Number of back faces
- `Thickness`: Thickness between the faces

### Return Value

First [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [MidSurface2::IGetFirstFaceArray](ms-its:sldworksapivb6.chm::/sldworks~MidSurface2~IGetFirstFaceArray.html).

## Remarks

A separator is needed between the front faces and back faces. Thus, a NULL always exists between the front faces and the back faces.

For example, if there are five faces in the model, then the mid-surface has five faces. To get the five faces:

- Call IMidSurface2::IGetGetFirstFaceArray once.
- Call [IMidSurface2::IGetNextFaceArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~IGetNextFaceArray.html) four times.

At each call, the data is arranged as follows if there is one front face in the array:

[Neutral face], [front face], NULL, [back face]

If there are more than one front face in the array, then the data is arranged as follows:

[Neutral face], [front face1, front face2], NULL, [back face1, back face2]

To get the next face from the original paired faces, call [IMidSurface2::IGetNextFaceArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~IGetNextFaceArray.html).

## See Also

[IMidSurface2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.html)
[IMidSurface2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2_members.html)
[IMidSurface2::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFaceCount.html)
[IMidSurface2::GetFirstFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFirstFaceArray.html)
[IMidSurface2::GetNextFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextFaceArray.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
