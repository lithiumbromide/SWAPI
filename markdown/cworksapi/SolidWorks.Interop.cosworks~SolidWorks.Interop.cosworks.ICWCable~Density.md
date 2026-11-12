---
title: "Density Property (ICWCable)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCable"
member: "Density"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable~Density.html"
---

# Density Property (ICWCable)

Adds the specified mass to force calculations of this cable connector.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property Density As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCable

instance.Density = value
```

### C#

```csharp
System.double Density {set;}
```

### C++/CLI

```cpp
property System.double Density {
   void set (    System.double value);
}
```

### Property Value

0.0 <= mass in kilograms <= 1000000000000000042420637374017961984.0

## VBA Syntax

See [CWCable::Density](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCable~Density.html).

## See Also

[ICWCable Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html)
[ICWCable Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable_members.html)

## Availability

SOLIDWORKS Simulation API 2026 SP0
