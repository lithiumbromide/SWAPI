---
title: "ReverseDirection Property (ICWHeatPower)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatPower"
member: "ReverseDirection"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~ReverseDirection.html"
---

# ReverseDirection Property (ICWHeatPower)

Obsolete. Superseded by [ICWHeatPower::ReverseDirection2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~ReverseDirection2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseDirection As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatPower
Dim value As System.Integer

instance.ReverseDirection = value

value = instance.ReverseDirection
```

### C#

```csharp
System.int ReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.int ReverseDirection {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to reverse direction, 0 to not

## VBA Syntax

See [CWHeatPower::ReverseDirection](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatPower~ReverseDirection.html).

## See Also

[ICWHeatPower Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html)
[ICWHeatPower Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower_members.html)
[ICWHeatPower::HPValue Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~HPValue.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
