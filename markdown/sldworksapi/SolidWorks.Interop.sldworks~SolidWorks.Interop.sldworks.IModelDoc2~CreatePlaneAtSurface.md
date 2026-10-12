---
title: "CreatePlaneAtSurface Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreatePlaneAtSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtSurface.html"
---

# CreatePlaneAtSurface Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::CreatePlaneAtSurface3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreatePlaneAtSurface3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub CreatePlaneAtSurface( _
   ByVal InterIndex As System.Integer, _
   ByVal ProjOpt As System.Boolean, _
   ByVal ReverseDir As System.Boolean, _
   ByVal NormalPlane As System.Boolean, _
   ByVal Angle As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim InterIndex As System.Integer
Dim ProjOpt As System.Boolean
Dim ReverseDir As System.Boolean
Dim NormalPlane As System.Boolean
Dim Angle As System.Double

instance.CreatePlaneAtSurface(InterIndex, ProjOpt, ReverseDir, NormalPlane, Angle)
```

### C#

```csharp
void CreatePlaneAtSurface(
   System.int InterIndex,
   System.bool ProjOpt,
   System.bool ReverseDir,
   System.bool NormalPlane,
   System.double Angle
)
```

### C++/CLI

```cpp
void CreatePlaneAtSurface(
   System.int InterIndex,
   System.bool ProjOpt,
   System.bool ReverseDir,
   System.bool NormalPlane,
   System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InterIndex`:
- `ProjOpt`:
- `ReverseDir`:
- `NormalPlane`:
- `Angle`:

## VBA Syntax

See [ModelDoc2::CreatePlaneAtSurface](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreatePlaneAtSurface.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
