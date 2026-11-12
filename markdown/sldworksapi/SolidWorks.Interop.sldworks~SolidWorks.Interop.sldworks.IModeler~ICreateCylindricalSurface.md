---
title: "ICreateCylindricalSurface Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateCylindricalSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateCylindricalSurface.html"
---

# ICreateCylindricalSurface Method (IModeler)

Obsolete. Superseded by [IModeler::ICreateCylindricalSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateCylindricalSurface2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateCylindricalSurface( _
   ByRef Center As System.Double, _
   ByRef Direction As System.Double, _
   ByVal Radius As System.Double _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Center As System.Double
Dim Direction As System.Double
Dim Radius As System.Double
Dim value As Surface

value = instance.ICreateCylindricalSurface(Center, Direction, Radius)
```

### C#

```csharp
Surface ICreateCylindricalSurface(
   ref System.double Center,
   ref System.double Direction,
   System.double Radius
)
```

### C++/CLI

```cpp
Surface^ ICreateCylindricalSurface(
   System.double% Center,
   System.double% Direction,
   System.double Radius
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Center`:
- `Direction`:
- `Radius`:

## VBA Syntax

See [Modeler::ICreateCylindricalSurface](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreateCylindricalSurface.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
