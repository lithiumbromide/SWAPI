---
title: "IDeleteFaces2 Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IDeleteFaces2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IDeleteFaces2.html"
---

# IDeleteFaces2 Method (IBody)

Obsolete. Superseded by [IBody2::IDeleteFaces3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IDeleteFaces3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IDeleteFaces2( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FaceList As Face, _
   ByVal Option As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim NumOfFaces As System.Integer
Dim FaceList As Face
Dim Option As System.Integer
Dim value As System.Integer

value = instance.IDeleteFaces2(NumOfFaces, FaceList, Option)
```

### C#

```csharp
System.int IDeleteFaces2(
   System.int NumOfFaces,
   ref Face FaceList,
   System.int Option
)
```

### C++/CLI

```cpp
System.int IDeleteFaces2(
   System.int NumOfFaces,
   Face^% FaceList,
   System.int Option
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`:
- `FaceList`:
- `Option`:

## VBA Syntax

See [Body::IDeleteFaces2](ms-its:sldworksapivb6.chm::/sldworks~Body~IDeleteFaces2.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
