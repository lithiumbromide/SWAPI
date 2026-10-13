---
title: "UnitType Property (ICWCable)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCable"
member: "UnitType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable~UnitType.html"
---

# UnitType Property (ICWCable)

Sets the unit system for this cable.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property UnitType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCable

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

Unit system as defined in [swsUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsUnit_e.html)

## VBA Syntax

See [CWCable::UnitType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCable~UnitType.html).

## See Also

[ICWCable Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html)
[ICWCable Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable_members.html)
