---
title: "IDeleteBlends Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IDeleteBlends"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteBlends.html"
---

# IDeleteBlends Method (IBody2)

Obsolete. Superseded by [IBody2::IDeleteBlends2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IDeleteBlends2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IDeleteBlends( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FaceList As Face2 _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FaceList As Face2
Dim value As System.Boolean

value = instance.IDeleteBlends(NumOfFaces, FaceList)
```

### C#

```csharp
System.bool IDeleteBlends(
   System.int NumOfFaces,
   ref Face2 FaceList
)
```

### C++/CLI

```cpp
System.bool IDeleteBlends(
   System.int NumOfFaces,
   Face2^% FaceList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`:
- `FaceList`:

## VBA Syntax

See [Body2::IDeleteBlends](ms-its:sldworksapivb6.chm::/sldworks~Body2~IDeleteBlends.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
