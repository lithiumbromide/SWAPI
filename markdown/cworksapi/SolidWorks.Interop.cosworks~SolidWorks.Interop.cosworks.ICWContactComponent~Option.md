---
title: "Option Property (ICWContactComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent"
member: "Option"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~Option.html"
---

# Option Property (ICWContactComponent)

Gets or sets the mesh compatibility for this contact.

## Syntax

### Visual Basic (Declaration)

```vb
Property Option As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactComponent
Dim value As System.Integer

instance.Option = value

value = instance.Option
```

### C#

```csharp
System.int Option {get; set;}
```

### C++/CLI

```cpp
property System.int Option {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Mesh compatibility as defined in [swsMeshCompatibility_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMeshCompatibility_e.html)

## VBA Syntax

See [CWContactComponent::Option](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactComponent~Option.html).

## Examples

See the [ICWContactComponent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html) examples.

## See Also

[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
