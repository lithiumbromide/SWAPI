---
title: "MappingType Property (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "MappingType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~MappingType.html"
---

# MappingType Property (ICWCompositeShellOptions)

Gets or sets the type of ply angle direction reference mapping.

## Syntax

### Visual Basic (Declaration)

```vb
Property MappingType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim value As System.Integer

instance.MappingType = value

value = instance.MappingType
```

### C#

```csharp
System.int MappingType {get; set;}
```

### C++/CLI

```cpp
property System.int MappingType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Ply angle direction reference mapping as defined in [swsCompositeShellOptionsMappingType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCompositeShellOptionsMappingType_e.html)

## VBA Syntax

See [CWCompositeShellOptions::MappingType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCompositeShellOptions~MappingType.html).

## Examples

See the [ICWCompositeShellOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html) examples.

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[ICWCompositeShellOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
