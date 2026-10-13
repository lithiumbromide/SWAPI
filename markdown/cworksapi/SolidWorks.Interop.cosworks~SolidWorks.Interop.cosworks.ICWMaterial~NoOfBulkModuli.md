---
title: "NoOfBulkModuli Property (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "NoOfBulkModuli"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~NoOfBulkModuli.html"
---

# NoOfBulkModuli Property (ICWMaterial)

Gets or sets the number of bulk moduli for the viscoelastic material model used in nonlinear studies only.

## Syntax

### Visual Basic (Declaration)

```vb
Property NoOfBulkModuli As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim value As System.Integer

instance.NoOfBulkModuli = value

value = instance.NoOfBulkModuli
```

### C#

```csharp
System.int NoOfBulkModuli {get; set;}
```

### C++/CLI

```cpp
property System.int NoOfBulkModuli {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Number of bulk moduli

## VBA Syntax

See [CWMaterial::NoOfBulkModuli](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~NoOfBulkModuli.html).

## Remarks

Number of bulk moduli for the viscelastic material model are valid in nonlinear studies only.

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
