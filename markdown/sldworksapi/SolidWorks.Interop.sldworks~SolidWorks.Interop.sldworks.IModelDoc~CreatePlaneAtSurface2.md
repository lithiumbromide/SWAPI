---
title: "CreatePlaneAtSurface2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreatePlaneAtSurface2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreatePlaneAtSurface2.html"
---

# CreatePlaneAtSurface2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreatePlaneAtSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreatePlaneAtSurface2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreatePlaneAtSurface2( _
   ByVal InterIndex As System.Integer, _
   ByVal ProjOpt As System.Boolean, _
   ByVal ReverseDir As System.Boolean, _
   ByVal NormalPlane As System.Boolean, _
   ByVal Angle As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim InterIndex As System.Integer
Dim ProjOpt As System.Boolean
Dim ReverseDir As System.Boolean
Dim NormalPlane As System.Boolean
Dim Angle As System.Double
Dim value As System.Object

value = instance.CreatePlaneAtSurface2(InterIndex, ProjOpt, ReverseDir, NormalPlane, Angle)
```

### C#

```csharp
System.object CreatePlaneAtSurface2(
   System.int InterIndex,
   System.bool ProjOpt,
   System.bool ReverseDir,
   System.bool NormalPlane,
   System.double Angle
)
```

### C++/CLI

```cpp
System.Object^ CreatePlaneAtSurface2(
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

See [ModelDoc::CreatePlaneAtSurface2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreatePlaneAtSurface2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
