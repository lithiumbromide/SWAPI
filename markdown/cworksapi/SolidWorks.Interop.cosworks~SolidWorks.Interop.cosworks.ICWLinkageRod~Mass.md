---
title: "Mass Property (ICWLinkageRod)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLinkageRod"
member: "Mass"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod~Mass.html"
---

# Mass Property (ICWLinkageRod)

Adds the specified mass to force calculations of this linkage rod connector.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property Mass As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLinkageRod

instance.Mass = value
```

### C#

```csharp
System.double Mass {set;}
```

### C++/CLI

```cpp
property System.double Mass {
   void set (    System.double value);
}
```

### Property Value

0.0 <= mass in kilograms <= 1000000000000000042420637374017961984.0

## VBA Syntax

See [CWLinkageRod::Mass](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLinkageRod~Mass.html).

## Remarks

This property is valid only if [ICWLinkageRoad::IncludeMass](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod~IncludeMass.html) is true.

## See Also

[ICWLinkageRod Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html)
[ICWLinkageRod Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
