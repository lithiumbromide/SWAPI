---
title: "CreateBodyFromFaces Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "CreateBodyFromFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBodyFromFaces.html"
---

# CreateBodyFromFaces Method (IBody2)

Creates a temporary body from the faces.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateBodyFromFaces( _
   ByVal NumOfFaces As System.Integer, _
   ByVal FaceList As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FaceList As System.Object
Dim value As System.Object

value = instance.CreateBodyFromFaces(NumOfFaces, FaceList)
```

### C#

```csharp
System.object CreateBodyFromFaces(
   System.int NumOfFaces,
   System.object FaceList
)
```

### C++/CLI

```cpp
System.Object^ CreateBodyFromFaces(
   System.int NumOfFaces,
   System.Object^ FaceList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`: Number of faces to use to create the body
- `FaceList`: Array containing the faces to use to create the body

### Return Value

Object for the body

## VBA Syntax

See [Body2::CreateBodyFromFaces](ms-its:sldworksapivb6.chm::/sldworks~Body2~CreateBodyFromFaces.html).

## Examples

[Create Body from Selected Faces (C#)](Create_Body_From_Selected_Faces_Example_CSharp.htm)
[Create Body from Selected Faces (VB.NET)](Create_Body_From_Selected_Faces_Example_VBNET.htm)
[Create Body from Selected Faces (VBA)](Create_Body_From_Selected_Faces_Example_VB.htm)

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::ICreateBodyFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBodyFromFaces.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
