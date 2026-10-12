---
title: "Layers Property (ICWMeshControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMeshControl"
member: "Layers"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~Layers.html"
---

# Layers Property (ICWMeshControl)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Property Layers As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMeshControl
Dim value As System.Integer

instance.Layers = value

value = instance.Layers
```

### C#

```csharp
System.int Layers {get; set;}
```

### C++/CLI

```cpp
property System.int Layers {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Number of layers

## VBA Syntax

See [CWMeshControl::Layers](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMeshControl~Layers.html).

## See Also

[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWMeshControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl_members.html)
[ICWMeshControl::Ratio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~Ratio.html)

## Availability

SOLIDWORKS Simulation API 2008 sP1.0
