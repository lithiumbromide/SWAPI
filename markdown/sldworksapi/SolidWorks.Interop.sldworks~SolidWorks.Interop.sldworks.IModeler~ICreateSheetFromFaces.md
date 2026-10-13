---
title: "ICreateSheetFromFaces Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateSheetFromFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromFaces.html"
---

# ICreateSheetFromFaces Method (IModeler)

Creates a sheet (surface) body from connected faces.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateSheetFromFaces( _
   ByVal FaceCount As System.Integer, _
   ByRef FaceArr As Face2 _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim FaceCount As System.Integer
Dim FaceArr As Face2
Dim value As Body2

value = instance.ICreateSheetFromFaces(FaceCount, FaceArr)
```

### C#

```csharp
Body2 ICreateSheetFromFaces(
   System.int FaceCount,
   ref Face2 FaceArr
)
```

### C++/CLI

```cpp
Body2^ ICreateSheetFromFaces(
   System.int FaceCount,
   Face2^% FaceArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceCount`: Number of connected faces
- `FaceArr`: Array of connected [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

### Return Value

Newly created [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Modeler::ICreateSheetFromFaces](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreateSheetFromFaces.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CreateSheetFromSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSheetFromSurface.html)
[IModeler::CreateSheetFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSheetFromFaces.html)
[IModeler::ICreateSheetFromSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromSurface2.html)
[IFace2::CreateSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBody.html)
[IFace2::CreateSheetBodyByFaceExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBodyByFaceExtension.html)
[IFace2::ICreateSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBody.html)
[IFace2::ICreateSheetBodyByFaceExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBodyByFaceExtension.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
