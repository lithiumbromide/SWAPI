---
title: "IncludeCreep Property (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "IncludeCreep"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~IncludeCreep.html"
---

# IncludeCreep Property (ICWMaterial)

Obsolete. Superseded by [ICWMaterial::IncludeCreep2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~IncludeCreep2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeCreep As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim value As System.Integer

instance.IncludeCreep = value

value = instance.IncludeCreep
```

### C#

```csharp
System.int IncludeCreep {get; set;}
```

### C++/CLI

```cpp
property System.int IncludeCreep {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

- 1 = Include creep effect
- 0 = Do not include creep effect

## VBA Syntax

See [CWMaterial::IncludeCreep](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~IncludeCreep.html).

## Remarks

Creep effect is valid for nonlinear studies only.

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
