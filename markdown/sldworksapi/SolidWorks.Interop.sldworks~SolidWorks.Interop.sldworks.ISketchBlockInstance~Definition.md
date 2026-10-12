---
title: "Definition Property (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "Definition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Definition.html"
---

# Definition Property (ISketchBlockInstance)

Gets or sets the block definition for this block instance.

## Syntax

### Visual Basic (Declaration)

```vb
Property Definition As SketchBlockDefinition
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim value As SketchBlockDefinition

instance.Definition = value

value = instance.Definition
```

### C#

```csharp
SketchBlockDefinition Definition {get; set;}
```

### C++/CLI

```cpp
property SketchBlockDefinition^ Definition {
   SketchBlockDefinition^ get();
   void set (    SketchBlockDefinition^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Block definition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition.html) for this block instance

## VBA Syntax

See [SketchBlockInstance::Definition](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~Definition.html).

## Examples

[Get Block Instance in Part or Assembly (VBA)](Get_Block_Instance_in_Part_or_Assembly_Example_VB.htm)

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
