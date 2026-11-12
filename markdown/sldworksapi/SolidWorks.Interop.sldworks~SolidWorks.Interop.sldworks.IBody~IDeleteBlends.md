---
title: "IDeleteBlends Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IDeleteBlends"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IDeleteBlends.html"
---

# IDeleteBlends Method (IBody)

Obsolete. Superseded by [IBody2::IDeleteBlends2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IDeleteBlends2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IDeleteBlends( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FaceList As Face _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim NumOfFaces As System.Integer
Dim FaceList As Face
Dim value As System.Boolean

value = instance.IDeleteBlends(NumOfFaces, FaceList)
```

### C#

```csharp
System.bool IDeleteBlends(
   System.int NumOfFaces,
   ref Face FaceList
)
```

### C++/CLI

```cpp
System.bool IDeleteBlends(
   System.int NumOfFaces,
   Face^% FaceList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`:
- `FaceList`:

## VBA Syntax

See [Body::IDeleteBlends](ms-its:sldworksapivb6.chm::/sldworks~Body~IDeleteBlends.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
