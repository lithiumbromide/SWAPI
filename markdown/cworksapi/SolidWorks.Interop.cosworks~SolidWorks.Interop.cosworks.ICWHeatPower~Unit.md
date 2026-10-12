---
title: "Unit Property (ICWHeatPower)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatPower"
member: "Unit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~Unit.html"
---

# Unit Property (ICWHeatPower)

Gets or sets the units of heat power.

## Syntax

### Visual Basic (Declaration)

```vb
Property Unit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatPower
Dim value As System.Integer

instance.Unit = value

value = instance.Unit
```

### C#

```csharp
System.int Unit {get; set;}
```

### C++/CLI

```cpp
property System.int Unit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Units as defined in [swsUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnit_e.html)

## VBA Syntax

See [CWHeatPower::Unit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatPower~Unit.html).

## Examples

See the [ICWHeatPower](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html) examples.

## See Also

[ICWHeatPower Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html)
[ICWHeatPower Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower_members.html)
[ICWHeatPower::HPValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~HPValue.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
