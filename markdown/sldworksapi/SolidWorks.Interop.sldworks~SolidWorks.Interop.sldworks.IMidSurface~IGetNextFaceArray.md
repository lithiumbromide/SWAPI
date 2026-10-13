---
title: "IGetNextFaceArray Method (IMidSurface)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface"
member: "IGetNextFaceArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface~IGetNextFaceArray.html"
---

# IGetNextFaceArray Method (IMidSurface)

Obsolete. Superseded by [IMidSurface2::IGetNextFaceArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~IGetNextFaceArray.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNextFaceArray( _
   ByVal FromFrontFaceListDisp As System.IntPtr, _
   ByRef SizeOfFrontFaceList As System.Integer, _
   ByVal FromFaceBackListDisp As System.IntPtr, _
   ByRef SizeOfBackFaceList As System.Integer, _
   ByRef Thickness As System.Double _
) As Face
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface
Dim FromFrontFaceListDisp As System.IntPtr
Dim SizeOfFrontFaceList As System.Integer
Dim FromFaceBackListDisp As System.IntPtr
Dim SizeOfBackFaceList As System.Integer
Dim Thickness As System.Double
Dim value As Face

value = instance.IGetNextFaceArray(FromFrontFaceListDisp, SizeOfFrontFaceList, FromFaceBackListDisp, SizeOfBackFaceList, Thickness)
```

### C#

```csharp
Face IGetNextFaceArray(
   out System.IntPtr FromFrontFaceListDisp,
   out System.int SizeOfFrontFaceList,
   out System.IntPtr FromFaceBackListDisp,
   out System.int SizeOfBackFaceList,
   out System.double Thickness
)
```

### C++/CLI

```cpp
Face^ IGetNextFaceArray(
   [Out] System.IntPtr FromFrontFaceListDisp,
   [Out] System.int SizeOfFrontFaceList,
   [Out] System.IntPtr FromFaceBackListDisp,
   [Out] System.int SizeOfBackFaceList,
   [Out] System.double Thickness
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FromFrontFaceListDisp`:
- `SizeOfFrontFaceList`:
- `FromFaceBackListDisp`:
- `SizeOfBackFaceList`:
- `Thickness`:

## VBA Syntax

See [MidSurface::IGetNextFaceArray](ms-its:sldworksapivb6.chm::/sldworks~MidSurface~IGetNextFaceArray.html).

## See Also

[IMidSurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface.html)
[IMidSurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface_members.html)
