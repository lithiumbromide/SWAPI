---
title: "GetNextFaceArray Method (IMidSurface2)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface2"
member: "GetNextFaceArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextFaceArray.html"
---

# GetNextFaceArray Method (IMidSurface2)

Obsolete. Superseded by [IMidSurface3::GetNextFaceArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~GetNextFaceArray.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNextFaceArray( _
   ByRef Thickness As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface2
Dim Thickness As System.Double
Dim value As System.Object

value = instance.GetNextFaceArray(Thickness)
```

### C#

```csharp
System.object GetNextFaceArray(
   out System.double Thickness
)
```

### C++/CLI

```cpp
System.Object^ GetNextFaceArray(
   [Out] System.double Thickness
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`: Thickness between the faces

### Return Value

Next [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [MidSurface2::GetNextFaceArray](ms-its:sldworksapivb6.chm::/sldworks~MidSurface2~GetNextFaceArray.html).

## Remarks

A separator is needed between the front faces and back faces. Thus, a NULL always exists between the front faces and the back faces.

For example, if there are five faces in the model, then the mid-surface has five faces. To get the five faces:

- Call [IMidSurface2::GetGetFirstFaceArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~GetFirstFaceArray.html) once.
- Call IMidSurface2::GetNextFaceArray four times.

At each call, the data is arranged as follows if there is one front face in the array:

[Neutral face], [front face], NULL, [back face]

If there are more than one front face in the array, then the data is arranged as follows:

[Neutral face], [front face1, front face2], NULL, [back face1, back face2]

Call [IMidSurface2::GetFirstFaceArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~GetFirstFaceArray.html) to get the first face from the original paired faces.

## See Also

[IMidSurface2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.html)
[IMidSurface2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2_members.html)
[IMidSurface2::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFaceCount.html)
[IMidSurface2::IGetFirstFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstFaceArray.html)
[IMidSurface2::IGetNextFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetNextFaceArray.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
