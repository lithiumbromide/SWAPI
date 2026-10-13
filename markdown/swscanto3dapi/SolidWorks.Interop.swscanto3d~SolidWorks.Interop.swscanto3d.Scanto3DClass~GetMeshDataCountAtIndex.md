---
title: "GetMeshDataCountAtIndex Method (Scanto3DClass)"
project: "SOLIDWORKS Scanto3D API Help"
interface: "Scanto3DClass"
member: "GetMeshDataCountAtIndex"
kind: "method"
source: "swscanto3dapi/SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.Scanto3DClass~GetMeshDataCountAtIndex.html"
---

# GetMeshDataCountAtIndex Method (Scanto3DClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function GetMeshDataCountAtIndex( _
   ByVal Index As System.Integer, _
   ByRef PointsCount As System.Integer, _
   ByRef FacetsCount As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As Scanto3DClass
Dim Index As System.Integer
Dim PointsCount As System.Integer
Dim FacetsCount As System.Integer
Dim value As System.Boolean

value = instance.GetMeshDataCountAtIndex(Index, PointsCount, FacetsCount)
```

### C#

```csharp
public virtual System.bool GetMeshDataCountAtIndex(
   System.int Index,
   out System.int PointsCount,
   out System.int FacetsCount
)
```

### C++/CLI

```cpp
public:
virtual System.bool GetMeshDataCountAtIndex(
   System.int Index,
   [Out] System.int PointsCount,
   [Out] System.int FacetsCount
)
```

### Parameters

- `Index`:
- `PointsCount`:
- `FacetsCount`:

## See Also

[Scanto3DClass Class](SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.Scanto3DClass.html)
[Scanto3DClass Members](SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.Scanto3DClass_members.html)
