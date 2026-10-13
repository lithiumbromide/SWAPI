---
title: "CreateBodyFromFaces Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "CreateBodyFromFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~CreateBodyFromFaces.html"
---

# CreateBodyFromFaces Method (IBody)

Obsolete. Superseded by [IBody2::CreateBodyFromFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateBodyFromFaces.html).

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
Dim instance As IBody
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

- `NumOfFaces`:
- `FaceList`:

## VBA Syntax

See [Body::CreateBodyFromFaces](ms-its:sldworksapivb6.chm::/sldworks~Body~CreateBodyFromFaces.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
