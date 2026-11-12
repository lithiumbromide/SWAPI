---
title: "ICreateSphericalSurface Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateSphericalSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSphericalSurface.html"
---

# ICreateSphericalSurface Method (IModeler)

Obsolete. Superseded by [IModeler::ICreateSphericalSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateSphericalSurface2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateSphericalSurface( _
   ByRef Center As System.Double, _
   ByVal Radius As System.Double _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Center As System.Double
Dim Radius As System.Double
Dim value As Surface

value = instance.ICreateSphericalSurface(Center, Radius)
```

### C#

```csharp
Surface ICreateSphericalSurface(
   ref System.double Center,
   System.double Radius
)
```

### C++/CLI

```cpp
Surface^ ICreateSphericalSurface(
   System.double% Center,
   System.double Radius
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Center`:
- `Radius`:

## VBA Syntax

See [Modeler::ICreateSphericalSurface](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreateSphericalSurface.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
