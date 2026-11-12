---
title: "IReplaceSurfaces Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "IReplaceSurfaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IReplaceSurfaces.html"
---

# IReplaceSurfaces Method (IModeler)

Obsolete. Superseded by [IModeler::IReplaceSurfaces2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~IReplaceSurfaces2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IReplaceSurfaces( _
   ByVal NFaces As System.Integer, _
   ByRef FaceArray As Face, _
   ByRef NewSurfArray As Surface, _
   ByRef SenseArray As System.Integer, _
   ByVal Tolerance As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim NFaces As System.Integer
Dim FaceArray As Face
Dim NewSurfArray As Surface
Dim SenseArray As System.Integer
Dim Tolerance As System.Double
Dim value As System.Boolean

value = instance.IReplaceSurfaces(NFaces, FaceArray, NewSurfArray, SenseArray, Tolerance)
```

### C#

```csharp
System.bool IReplaceSurfaces(
   System.int NFaces,
   ref Face FaceArray,
   ref Surface NewSurfArray,
   ref System.int SenseArray,
   System.double Tolerance
)
```

### C++/CLI

```cpp
System.bool IReplaceSurfaces(
   System.int NFaces,
   Face^% FaceArray,
   Surface^% NewSurfArray,
   System.int% SenseArray,
   System.double Tolerance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NFaces`:
- `FaceArray`:
- `NewSurfArray`:
- `SenseArray`:
- `Tolerance`:

## VBA Syntax

See [Modeler::IReplaceSurfaces](ms-its:sldworksapivb6.chm::/sldworks~Modeler~IReplaceSurfaces.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
