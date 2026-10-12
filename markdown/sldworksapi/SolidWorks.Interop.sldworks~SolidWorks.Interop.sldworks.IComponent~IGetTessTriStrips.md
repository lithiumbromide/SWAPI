---
title: "IGetTessTriStrips Method (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "IGetTessTriStrips"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~IGetTessTriStrips.html"
---

# IGetTessTriStrips Method (IComponent)

Obsolete. Superseded by [IComponent2::IGetTessTriStrips](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IGetTessTriStrips.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTessTriStrips( _
   ByVal NoConversion As System.Boolean _
) As System.Single
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim NoConversion As System.Boolean
Dim value As System.Single

value = instance.IGetTessTriStrips(NoConversion)
```

### C#

```csharp
System.float IGetTessTriStrips(
   System.bool NoConversion
)
```

### C++/CLI

```cpp
System.float IGetTessTriStrips(
   System.bool NoConversion
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NoConversion`:

## VBA Syntax

See [Component::IGetTessTriStrips](ms-its:sldworksapivb6.chm::/sldworks~Component~IGetTessTriStrips.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
