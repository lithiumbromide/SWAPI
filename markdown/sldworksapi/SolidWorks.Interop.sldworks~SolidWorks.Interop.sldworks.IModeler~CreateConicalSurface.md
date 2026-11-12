---
title: "CreateConicalSurface Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreateConicalSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateConicalSurface.html"
---

# CreateConicalSurface Method (IModeler)

Obsolete. Superseded by [IModeler::CreateConicalSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateConicalSurface2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateConicalSurface( _
   ByVal Center As System.Object, _
   ByVal Direction As System.Object, _
   ByVal Radius As System.Double, _
   ByVal SemiAngle As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Center As System.Object
Dim Direction As System.Object
Dim Radius As System.Double
Dim SemiAngle As System.Double
Dim value As System.Object

value = instance.CreateConicalSurface(Center, Direction, Radius, SemiAngle)
```

### C#

```csharp
System.object CreateConicalSurface(
   System.object Center,
   System.object Direction,
   System.double Radius,
   System.double SemiAngle
)
```

### C++/CLI

```cpp
System.Object^ CreateConicalSurface(
   System.Object^ Center,
   System.Object^ Direction,
   System.double Radius,
   System.double SemiAngle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Center`:
- `Direction`:
- `Radius`:
- `SemiAngle`:

## VBA Syntax

See [Modeler::CreateConicalSurface](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreateConicalSurface.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
