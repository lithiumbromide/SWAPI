---
title: "IncludeThermostat2 Property (ICWHeatFlux)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatFlux"
member: "IncludeThermostat2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~IncludeThermostat2.html"
---

# IncludeThermostat2 Property (ICWHeatFlux)

Gets or sets whether to include thermostat effects in this heat flux.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeThermostat2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatFlux
Dim value As System.Boolean

instance.IncludeThermostat2 = value

value = instance.IncludeThermostat2
```

### C#

```csharp
System.bool IncludeThermostat2 {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeThermostat2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to include thermostat effects, 0 or false to not

## Examples

See the [ICWHeatFlux](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html) examples.

## Remarks

Thermostat is used for transient thermal studies only.

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWHeatFlux Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html)
[ICWHeatFlux Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
