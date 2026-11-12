---
title: "IGetTessellation Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IGetTessellation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IGetTessellation.html"
---

# IGetTessellation Method (IBody)

Obsolete. Superseded by [IBody2::IGetTessellation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetTessellation.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTessellation( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FaceList As Face _
) As Tessellation
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim NumOfFaces As System.Integer
Dim FaceList As Face
Dim value As Tessellation

value = instance.IGetTessellation(NumOfFaces, FaceList)
```

### C#

```csharp
Tessellation IGetTessellation(
   System.int NumOfFaces,
   ref Face FaceList
)
```

### C++/CLI

```cpp
Tessellation^ IGetTessellation(
   System.int NumOfFaces,
   Face^% FaceList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`:
- `FaceList`:

## VBA Syntax

See [Body::IGetTessellation](ms-its:sldworksapivb6.chm::/sldworks~Body~IGetTessellation.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
