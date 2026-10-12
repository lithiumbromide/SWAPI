---
title: "ThermalCoefficient Property (ICWCable)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCable"
member: "ThermalCoefficient"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable~ThermalCoefficient.html"
---

# ThermalCoefficient Property (ICWCable)

Sets the thermal expansion coefficient for the custom material of this cable connector.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property ThermalCoefficient As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCable

instance.ThermalCoefficient = value
```

### C#

```csharp
System.double ThermalCoefficient {set;}
```

### C++/CLI

```cpp
property System.double ThermalCoefficient {
   void set (    System.double value);
}
```

### Property Value

0.0 <= Thermal expansion coefficient /Kelvin <= 1000000000000000042420637374017961984.0

## VBA Syntax

See [CWCable::ThermalCoefficient](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCable~ThermalCoefficient.html).

## Remarks

This property is valid only if [ICWCable::MaterialSource](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable~MaterialSource.html) is set to 1 (custom defined).

## See Also

[ICWCable Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html)
[ICWCable Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable_members.html)

## Availability

SOLIDWORKS Simulation API 2026 SP0
