---
title: "ICreateBodyFromFaces Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "ICreateBodyFromFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreateBodyFromFaces.html"
---

# ICreateBodyFromFaces Method (IBody)

Obsolete. Superseded by [IBody2::ICreateBodyFromFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateBodyFromFaces.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBodyFromFaces( _
   ByVal NumOfFaces As System.Integer, _
   ByVal FaceList As System.Object _
) As Body
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim NumOfFaces As System.Integer
Dim FaceList As System.Object
Dim value As Body

value = instance.ICreateBodyFromFaces(NumOfFaces, FaceList)
```

### C#

```csharp
Body ICreateBodyFromFaces(
   System.int NumOfFaces,
   System.object FaceList
)
```

### C++/CLI

```cpp
Body^ ICreateBodyFromFaces(
   System.int NumOfFaces,
   System.Object^ FaceList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`:
- `FaceList`:

## VBA Syntax

See [Body::ICreateBodyFromFaces](ms-its:sldworksapivb6.chm::/sldworks~Body~ICreateBodyFromFaces.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
