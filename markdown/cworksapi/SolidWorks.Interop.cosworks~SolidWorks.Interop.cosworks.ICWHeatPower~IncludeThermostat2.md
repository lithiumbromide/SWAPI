---
title: "IncludeThermostat2 Property (ICWHeatPower)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatPower"
member: "IncludeThermostat2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~IncludeThermostat2.html"
---

# IncludeThermostat2 Property (ICWHeatPower)

Gets or sets whether to include thermostat effects in heat power for transient thermal studies.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeThermostat2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatPower
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

-1 or true to include thermostat, 0 or false to not

## Examples

See the [ICWHeatPower](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html) examples.

## Remarks

Thermostat is used for transient [thermal](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWThermalStudyOptions.html) studies only.

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWHeatPower Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html)
[ICWHeatPower Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
