---
title: "CreateSheetFromFaces Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreateSheetFromFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSheetFromFaces.html"
---

# CreateSheetFromFaces Method (IModeler)

Creates a sheet (surface) body from connected faces.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSheetFromFaces( _
   ByVal FaceArr As System.Object _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim FaceArr As System.Object
Dim value As Body2

value = instance.CreateSheetFromFaces(FaceArr)
```

### C#

```csharp
Body2 CreateSheetFromFaces(
   System.object FaceArr
)
```

### C++/CLI

```cpp
Body2^ CreateSheetFromFaces(
   System.Object^ FaceArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceArr`: Array of connected [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

### Return Value

Newly created [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Modeler::CreateSheetFromFaces](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreateSheetFromFaces.html).

## Examples

[Create Sheet Body From Faces and Feature From Sheet Body (VBA)](Create_Sheet_Body_From_Faces_and_Feature_from_Sheet_Body_Example_VB.htm)

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CreateSheetFromSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSheetFromSurface.html)
[IModeler::ICreateSheetFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromFaces.html)
[IModeler::ICreateSheetFromSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromSurface2.html)
[IFace2::CreateSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBody.html)
[IFace2::CreateSheetBodyByFaceExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBodyByFaceExtension.html)
[IFace2::ICreateSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBody.html)
[IFace2::ICreateSheetBodyByFaceExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBodyByFaceExtension.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
