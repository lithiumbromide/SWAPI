---
title: "GetFirstFaceArray Method (IMidSurface3)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface3"
member: "GetFirstFaceArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFirstFaceArray.html"
---

# GetFirstFaceArray Method (IMidSurface3)

Gets the first face and the thickness between the faces.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstFaceArray( _
   ByRef Thickness As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface3
Dim Thickness As System.Double
Dim value As System.Object

value = instance.GetFirstFaceArray(Thickness)
```

### C#

```csharp
System.object GetFirstFaceArray(
   out System.double Thickness
)
```

### C++/CLI

```cpp
System.Object^ GetFirstFaceArray(
   [Out] System.double Thickness
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`: Thickness between the faces

### Return Value

First [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [MidSurface3::GetFirstFaceArray](ms-its:sldworksapivb6.chm::/sldworks~MidSurface3~GetFirstFaceArray.html).

## Remarks

A separator is needed between the front faces and back faces. Thus, a NULL always exists between the front and back faces.

For example, if there are five faces in the model, then the mid-surface has five faces. To get the five faces:

- Call IMidSurface3::GetGetFirstFaceArray once.
- Call [IMidSurface3::GetNextFaceArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~GetNextFaceArray.html) four times.

At each call, the data is arranged as follows if there is one front face in the array:

[Neutral face], [front face], NULL, [back face]

If there are more than one front face in the array, then the data is arranged as follows:

[Neutral face], [front face1, front face2], NULL, [back face1, back face2]

To get the next face from the original paired faces, call IMidSurface3::GetNextFaceArray.

## See Also

[IMidSurface3 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.html)
[IMidSurface3 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3_members.html)
[IMidSurface3::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFaceCount.html)
[IMidSurface3::IGetFirstFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetFirstFaceArray.html)
[IMidSurface3::IGetNextFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetNextFaceArray.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
