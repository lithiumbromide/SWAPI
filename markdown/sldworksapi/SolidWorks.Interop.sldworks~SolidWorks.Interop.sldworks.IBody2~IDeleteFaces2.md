---
title: "IDeleteFaces2 Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IDeleteFaces2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFaces2.html"
---

# IDeleteFaces2 Method (IBody2)

Obsolete. Superseded by [IBody2::IDeleteFaces3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IDeleteFaces3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IDeleteFaces2( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FaceList As Face2, _
   ByVal Option As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FaceList As Face2
Dim Option As System.Integer
Dim value As System.Integer

value = instance.IDeleteFaces2(NumOfFaces, FaceList, Option)
```

### C#

```csharp
System.int IDeleteFaces2(
   System.int NumOfFaces,
   ref Face2 FaceList,
   System.int Option
)
```

### C++/CLI

```cpp
System.int IDeleteFaces2(
   System.int NumOfFaces,
   Face2^% FaceList,
   System.int Option
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`:
- `FaceList`:
- `Option`:

## VBA Syntax

See [Body2::IDeleteFaces2](ms-its:sldworksapivb6.chm::/sldworks~Body2~IDeleteFaces2.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
