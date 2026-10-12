---
title: "IncludeCreep2 Property (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "IncludeCreep2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~IncludeCreep2.html"
---

# IncludeCreep2 Property (ICWMaterial)

Gets or sets whether to include creep effect for the material model in nonlinear studies only.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeCreep2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim value As System.Boolean

instance.IncludeCreep2 = value

value = instance.IncludeCreep2
```

### C#

```csharp
System.bool IncludeCreep2 {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeCreep2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

- -1 or true = Include creep effect
- 0 or false = Do not include creep effect

## Remarks

Creep effect is valid for nonlinear studies only.

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
