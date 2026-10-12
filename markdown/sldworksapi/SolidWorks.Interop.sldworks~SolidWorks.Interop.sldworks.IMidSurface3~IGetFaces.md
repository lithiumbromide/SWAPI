---
title: "IGetFaces Method (IMidSurface3)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface3"
member: "IGetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetFaces.html"
---

# IGetFaces Method (IMidSurface3)

Gets the faces in this midsurface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFaces( _
   ByVal NumFaces As System.Integer _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface3
Dim NumFaces As System.Integer
Dim value As Face2

value = instance.IGetFaces(NumFaces)
```

### C#

```csharp
Face2 IGetFaces(
   System.int NumFaces
)
```

### C++/CLI

```cpp
Face2^ IGetFaces(
   System.int NumFaces
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumFaces`: Number of faces

### Return Value

- in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IMidSurface3::GetFaceCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~GetFaceCount.html) to get NumFaces.

## See Also

[IMidSurface3 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.html)
[IMidSurface3 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3_members.html)
[IMidSurface3::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFaces.html)
[IMidSurface3::GetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFirstFace.html)
[IMidSurface3::GetNextFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetNextFace.html)
[IMidSurface3::IGetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetFirstFace.html)
[IMidSurface3::IGetNextFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetNextFace.html)

## Availability

SOLIDWORKS 2009 FCS, Revision 17.0
