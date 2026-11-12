---
title: "ShearModulus Property (ICWCable)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCable"
member: "ShearModulus"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable~ShearModulus.html"
---

# ShearModulus Property (ICWCable)

Sets the shear modulus for the custom material of this cable connector.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property ShearModulus As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCable

instance.ShearModulus = value
```

### C#

```csharp
System.double ShearModulus {set;}
```

### C++/CLI

```cpp
property System.double ShearModulus {
   void set (    System.double value);
}
```

### Property Value

Shear modulus

## VBA Syntax

See [CWCable::ShearModulus](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCable~ShearModulus.html).

## See Also

[ICWCable Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html)
[ICWCable Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable_members.html)

## Availability

SOLIDWORKS Simulation API 2026 SP0
