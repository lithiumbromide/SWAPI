---
title: "IGetTessTriangles Method (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "IGetTessTriangles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~IGetTessTriangles.html"
---

# IGetTessTriangles Method (IComponent)

Obsolete. Superseded by [IComponent2::IGetTessTriangles](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IGetTessTriangles.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTessTriangles( _
   ByVal NoConversion As System.Boolean _
) As System.Single
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim NoConversion As System.Boolean
Dim value As System.Single

value = instance.IGetTessTriangles(NoConversion)
```

### C#

```csharp
System.float IGetTessTriangles(
   System.bool NoConversion
)
```

### C++/CLI

```cpp
System.float IGetTessTriangles(
   System.bool NoConversion
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NoConversion`:

## VBA Syntax

See [Component::IGetTessTriangles](ms-its:sldworksapivb6.chm::/sldworks~Component~IGetTessTriangles.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
