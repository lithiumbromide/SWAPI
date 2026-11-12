---
title: "CreateCylindricalSurface Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreateCylindricalSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCylindricalSurface.html"
---

# CreateCylindricalSurface Method (IModeler)

Obsolete. Superseded by [IModeler::CreateCylindricalSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateCylindricalSurface2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCylindricalSurface( _
   ByVal Center As System.Object, _
   ByVal Direction As System.Object, _
   ByVal Radius As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Center As System.Object
Dim Direction As System.Object
Dim Radius As System.Double
Dim value As System.Object

value = instance.CreateCylindricalSurface(Center, Direction, Radius)
```

### C#

```csharp
System.object CreateCylindricalSurface(
   System.object Center,
   System.object Direction,
   System.double Radius
)
```

### C++/CLI

```cpp
System.Object^ CreateCylindricalSurface(
   System.Object^ Center,
   System.Object^ Direction,
   System.double Radius
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Center`:
- `Direction`:
- `Radius`:

## VBA Syntax

See [Modeler::CreateCylindricalSurface](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreateCylindricalSurface.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
