---
title: "IGetAllDecalProperties Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IGetAllDecalProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetAllDecalProperties.html"
---

# IGetAllDecalProperties Method (IFace2)

Gets the decal properties applied to this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAllDecalProperties( _
   ByVal Count As System.Integer _
) As FaceDecalProperties
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim Count As System.Integer
Dim value As FaceDecalProperties

value = instance.IGetAllDecalProperties(Count)
```

### C#

```csharp
FaceDecalProperties IGetAllDecalProperties(
   System.int Count
)
```

### C++/CLI

```cpp
FaceDecalProperties^ IGetAllDecalProperties(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of decals applied to this face

### Return Value

- in-process, unmanaged C++: Pointer to an array of [decal properties applied to this face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFaceDecalProperties.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IFace2::GetDecalsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetDecalsCount.html) to get the value of Count.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetAllDecalProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetAllDecalProperties.html)
[IFace2::IGetDecalProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetDecalProperties.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
