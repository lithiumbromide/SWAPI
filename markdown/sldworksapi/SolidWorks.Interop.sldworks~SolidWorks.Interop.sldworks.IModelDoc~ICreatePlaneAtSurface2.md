---
title: "ICreatePlaneAtSurface2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ICreatePlaneAtSurface2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreatePlaneAtSurface2.html"
---

# ICreatePlaneAtSurface2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ICreatePlaneAtSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreatePlaneAtSurface2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreatePlaneAtSurface2( _
   ByVal InterIndex As System.Integer, _
   ByVal ProjOpt As System.Boolean, _
   ByVal ReverseDir As System.Boolean, _
   ByVal NormalPlane As System.Boolean, _
   ByVal Angle As System.Double _
) As RefPlane
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim InterIndex As System.Integer
Dim ProjOpt As System.Boolean
Dim ReverseDir As System.Boolean
Dim NormalPlane As System.Boolean
Dim Angle As System.Double
Dim value As RefPlane

value = instance.ICreatePlaneAtSurface2(InterIndex, ProjOpt, ReverseDir, NormalPlane, Angle)
```

### C#

```csharp
RefPlane ICreatePlaneAtSurface2(
   System.int InterIndex,
   System.bool ProjOpt,
   System.bool ReverseDir,
   System.bool NormalPlane,
   System.double Angle
)
```

### C++/CLI

```cpp
RefPlane^ ICreatePlaneAtSurface2(
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

See [ModelDoc::ICreatePlaneAtSurface2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ICreatePlaneAtSurface2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
