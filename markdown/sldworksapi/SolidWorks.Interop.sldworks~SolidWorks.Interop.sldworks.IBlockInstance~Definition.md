---
title: "Definition Property (IBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "IBlockInstance"
member: "Definition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance~Definition.html"
---

# Definition Property (IBlockInstance)

Obsolete. Superseded by [ISketchBlockInstance::Definition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~Definition.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Definition As BlockDefinition
```

### Visual Basic (Usage)

```vb
Dim instance As IBlockInstance
Dim value As BlockDefinition

value = instance.Definition
```

### C#

```csharp
BlockDefinition Definition {get;}
```

### C++/CLI

```cpp
property BlockDefinition^ Definition {
   BlockDefinition^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [BlockInstance::Definition](ms-its:sldworksapivb6.chm::/sldworks~BlockInstance~Definition.html).

## See Also

[IBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance.html)
[IBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance_members.html)
