---
title: "IDeleteFaces3 Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IDeleteFaces3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IDeleteFaces3.html"
---

# IDeleteFaces3 Method (IBody)

Obsolete. Superseded by [IBody2::IDeleteFaces3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IDeleteFaces3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub IDeleteFaces3( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FaceList As Face, _
   ByVal Option As System.Integer, _
   ByVal DoLocalCheck As System.Boolean, _
   ByRef LocalCheckResult As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim NumOfFaces As System.Integer
Dim FaceList As Face
Dim Option As System.Integer
Dim DoLocalCheck As System.Boolean
Dim LocalCheckResult As System.Boolean

instance.IDeleteFaces3(NumOfFaces, FaceList, Option, DoLocalCheck, LocalCheckResult)
```

### C#

```csharp
void IDeleteFaces3(
   System.int NumOfFaces,
   ref Face FaceList,
   System.int Option,
   System.bool DoLocalCheck,
   ref System.bool LocalCheckResult
)
```

### C++/CLI

```cpp
void IDeleteFaces3(
   System.int NumOfFaces,
   Face^% FaceList,
   System.int Option,
   System.bool DoLocalCheck,
   System.bool% LocalCheckResult
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`:
- `FaceList`:
- `Option`:
- `DoLocalCheck`:
- `LocalCheckResult`:

## VBA Syntax

See [Body::IDeleteFaces3](ms-its:sldworksapivb6.chm::/sldworks~Body~IDeleteFaces3.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
