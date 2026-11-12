---
title: "NoOfShearModuli Property (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "NoOfShearModuli"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~NoOfShearModuli.html"
---

# NoOfShearModuli Property (ICWMaterial)

Gets or sets the number of shear moduli for the viscoelastic material model used in nonlinear studies only.

## Syntax

### Visual Basic (Declaration)

```vb
Property NoOfShearModuli As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim value As System.Integer

instance.NoOfShearModuli = value

value = instance.NoOfShearModuli
```

### C#

```csharp
System.int NoOfShearModuli {get; set;}
```

### C++/CLI

```cpp
property System.int NoOfShearModuli {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Number of shear moduli

## VBA Syntax

See [CWMaterial::NoOfShearModuli](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~NoOfShearModuli.html).

## Remarks

Number of shear moduli for the viscelastic material model are valid in nonlinear studies only.

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)

## Availability

Simulation Simulation API 2008 SP1.0
