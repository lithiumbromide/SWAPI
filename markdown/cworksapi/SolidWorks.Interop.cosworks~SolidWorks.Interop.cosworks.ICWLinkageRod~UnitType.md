---
title: "UnitType Property (ICWLinkageRod)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLinkageRod"
member: "UnitType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod~UnitType.html"
---

# UnitType Property (ICWLinkageRod)

Sets the units for this linkage rod connector.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property UnitType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLinkageRod

instance.UnitType = value
```

### C#

```csharp
System.int UnitType {set;}
```

### C++/CLI

```cpp
property System.int UnitType {
   void set (    System.int value);
}
```

### Property Value

Units as defined by [swsUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsUnit_e.html)

## VBA Syntax

See [CWLinkageRod::UnitType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLinkageRod~UnitType.html).

## See Also

[ICWLinkageRod Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html)
[ICWLinkageRod Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
