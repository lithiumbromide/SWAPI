---
title: "IDeleteBlends2 Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IDeleteBlends2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IDeleteBlends2.html"
---

# IDeleteBlends2 Method (IBody)

Obsolete. Superseded by [IBody2::IDeleteBlends2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IDeleteBlends2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IDeleteBlends2( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FaceList As Face, _
   ByVal DoLocalCheck As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim NumOfFaces As System.Integer
Dim FaceList As Face
Dim DoLocalCheck As System.Boolean
Dim value As System.Boolean

value = instance.IDeleteBlends2(NumOfFaces, FaceList, DoLocalCheck)
```

### C#

```csharp
System.bool IDeleteBlends2(
   System.int NumOfFaces,
   ref Face FaceList,
   System.bool DoLocalCheck
)
```

### C++/CLI

```cpp
System.bool IDeleteBlends2(
   System.int NumOfFaces,
   Face^% FaceList,
   System.bool DoLocalCheck
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`:
- `FaceList`:
- `DoLocalCheck`:

## VBA Syntax

See [Body::IDeleteBlends2](ms-its:sldworksapivb6.chm::/sldworks~Body~IDeleteBlends2.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
