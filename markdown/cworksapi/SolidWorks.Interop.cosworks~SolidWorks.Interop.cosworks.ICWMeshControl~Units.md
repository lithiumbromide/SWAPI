---
title: "Units Property (ICWMeshControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMeshControl"
member: "Units"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~Units.html"
---

# Units Property (ICWMeshControl)

Gets or sets the units for the mesh control.

## Syntax

### Visual Basic (Declaration)

```vb
Property Units As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMeshControl
Dim value As System.Integer

instance.Units = value

value = instance.Units
```

### C#

```csharp
System.int Units {get; set;}
```

### C++/CLI

```cpp
property System.int Units {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Mesh control linear units as defined in [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)

## VBA Syntax

See [CWMeshControl::Units](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMeshControl~Units.html).

## See Also

[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWMeshControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
