---
title: "ICreateBodyFromFaces Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ICreateBodyFromFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBodyFromFaces.html"
---

# ICreateBodyFromFaces Method (IBody2)

Creates a temporary body from the faces.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBodyFromFaces( _
   ByVal NumOfFaces As System.Integer, _
   ByVal FaceList As System.Object _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FaceList As System.Object
Dim value As Body2

value = instance.ICreateBodyFromFaces(NumOfFaces, FaceList)
```

### C#

```csharp
Body2 ICreateBodyFromFaces(
   System.int NumOfFaces,
   System.object FaceList
)
```

### C++/CLI

```cpp
Body2^ ICreateBodyFromFaces(
   System.int NumOfFaces,
   System.Object^ FaceList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`: Number of faces to use to create the body
- `FaceList`: Array containing the faces to use to create the body

### Return Value

[IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) object

## VBA Syntax

See [Body2::ICreateBodyFromFaces](ms-its:sldworksapivb6.chm::/sldworks~Body2~ICreateBodyFromFaces.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::CreateBodyFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBodyFromFaces.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
