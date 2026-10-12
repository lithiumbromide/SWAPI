---
title: "IGetDecalProperties Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IGetDecalProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetDecalProperties.html"
---

# IGetDecalProperties Method (IFace2)

Gets the properties of the specified decal on this face.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetDecalProperties( _
   ByVal PDecal As Decal, _
   ByRef pFaceDecalProperties As FaceDecalProperties _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim PDecal As Decal
Dim pFaceDecalProperties As FaceDecalProperties

instance.IGetDecalProperties(PDecal, pFaceDecalProperties)
```

### C#

```csharp
void IGetDecalProperties(
   Decal PDecal,
   ref FaceDecalProperties pFaceDecalProperties
)
```

### C++/CLI

```cpp
void IGetDecalProperties(
   Decal^ PDecal,
   FaceDecalProperties^% pFaceDecalProperties
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PDecal`: [Decal](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDecal.html) whose properties to get
- `pFaceDecalProperties`: - in-process, unmanaged C++: Pointer to an array of [decal properties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFaceDecalProperties.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetAllDecalProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetAllDecalProperties.html)
[IFace2::GetDecalsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetDecalsCount.html)
[IFace2::IGetAllDecalProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetAllDecalProperties.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
