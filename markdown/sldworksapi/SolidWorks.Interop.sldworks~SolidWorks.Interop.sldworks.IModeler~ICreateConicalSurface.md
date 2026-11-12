---
title: "ICreateConicalSurface Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateConicalSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateConicalSurface.html"
---

# ICreateConicalSurface Method (IModeler)

Obsolete. Superseded by [IModeler::ICreateConicalSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateCylindricalSurface2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateConicalSurface( _
   ByRef Center As System.Double, _
   ByRef Direction As System.Double, _
   ByVal Radius As System.Double, _
   ByVal SemiAngle As System.Double _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Center As System.Double
Dim Direction As System.Double
Dim Radius As System.Double
Dim SemiAngle As System.Double
Dim value As Surface

value = instance.ICreateConicalSurface(Center, Direction, Radius, SemiAngle)
```

### C#

```csharp
Surface ICreateConicalSurface(
   ref System.double Center,
   ref System.double Direction,
   System.double Radius,
   System.double SemiAngle
)
```

### C++/CLI

```cpp
Surface^ ICreateConicalSurface(
   System.double% Center,
   System.double% Direction,
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

See [Modeler::ICreateConicalSurface](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreateConicalSurface.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
