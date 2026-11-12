---
title: "GetMeshDataAtIndex Method (Scanto3DClass)"
project: "SOLIDWORKS Scanto3D API Help"
interface: "Scanto3DClass"
member: "GetMeshDataAtIndex"
kind: "method"
source: "swscanto3dapi/SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.Scanto3DClass~GetMeshDataAtIndex.html"
---

# GetMeshDataAtIndex Method (Scanto3DClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function GetMeshDataAtIndex( _
   ByVal Index As System.Integer, _
   ByRef Points As System.Object, _
   ByRef Facets As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As Scanto3DClass
Dim Index As System.Integer
Dim Points As System.Object
Dim Facets As System.Object
Dim value As System.Boolean

value = instance.GetMeshDataAtIndex(Index, Points, Facets)
```

### C#

```csharp
public virtual System.bool GetMeshDataAtIndex(
   System.int Index,
   out System.object Points,
   out System.object Facets
)
```

### C++/CLI

```cpp
public:
virtual System.bool GetMeshDataAtIndex(
   System.int Index,
   [Out] System.Object^ Points,
   [Out] System.Object^ Facets
)
```

### Parameters

- `Index`:
- `Points`:
- `Facets`:

## See Also

[Scanto3DClass Class](SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.Scanto3DClass.html)
[Scanto3DClass Members](SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.Scanto3DClass_members.html)
