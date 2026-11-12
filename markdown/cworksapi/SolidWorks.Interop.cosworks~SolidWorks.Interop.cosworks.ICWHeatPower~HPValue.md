---
title: "HPValue Property (ICWHeatPower)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatPower"
member: "HPValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~HPValue.html"
---

# HPValue Property (ICWHeatPower)

Gets or sets the heat power value for heat power.

## Syntax

### Visual Basic (Declaration)

```vb
Property HPValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatPower
Dim value As System.Double

instance.HPValue = value

value = instance.HPValue
```

### C#

```csharp
System.double HPValue {get; set;}
```

### C++/CLI

```cpp
property System.double HPValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Heat power value

## VBA Syntax

See [CWHeatPower::HPValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatPower~HPValue.html).

## Examples

See the [ICWHeatPower](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html) examples.

## See Also

[ICWHeatPower Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html)
[ICWHeatPower Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower_members.html)
[ICWHeatPower::Unit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~Unit.html)
[ICWHeatPower::ReverseDirection Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~ReverseDirection.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
