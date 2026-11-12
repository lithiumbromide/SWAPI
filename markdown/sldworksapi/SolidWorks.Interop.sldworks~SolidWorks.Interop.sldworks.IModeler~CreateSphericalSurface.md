---
title: "CreateSphericalSurface Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreateSphericalSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSphericalSurface.html"
---

# CreateSphericalSurface Method (IModeler)

Obsolete. Superseded by [IModeler::CreateSphericalSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateSphericalSurface2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSphericalSurface( _
   ByVal Center As System.Object, _
   ByVal Radius As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Center As System.Object
Dim Radius As System.Double
Dim value As System.Object

value = instance.CreateSphericalSurface(Center, Radius)
```

### C#

```csharp
System.object CreateSphericalSurface(
   System.object Center,
   System.double Radius
)
```

### C++/CLI

```cpp
System.Object^ CreateSphericalSurface(
   System.Object^ Center,
   System.double Radius
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Center`:
- `Radius`:

## VBA Syntax

See [Modeler::CreateSphericalSurface](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreateSphericalSurface.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
