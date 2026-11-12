---
title: "MooneyRivlinConstants Property (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "MooneyRivlinConstants"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~MooneyRivlinConstants.html"
---

# MooneyRivlinConstants Property (ICWMaterial)

Gets or sets the Mooney Rivlin constants for the MooneyRivlin material model used in nonlinear studies only.

## Syntax

### Visual Basic (Declaration)

```vb
Property MooneyRivlinConstants As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim value As System.Integer

instance.MooneyRivlinConstants = value

value = instance.MooneyRivlinConstants
```

### C#

```csharp
System.int MooneyRivlinConstants {get; set;}
```

### C++/CLI

```cpp
property System.int MooneyRivlinConstants {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Number of Mooney Rivlin constants

## VBA Syntax

See [CWMaterial::MooneyRivlinConstants](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~MooneyRivlinConstants.html).

## Remarks

Mooney Rivlin constants are valid in nonlinear studies only.

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
