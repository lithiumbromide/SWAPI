---
title: "HFValue Property (ICWHeatFlux)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatFlux"
member: "HFValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~HFValue.html"
---

# HFValue Property (ICWHeatFlux)

Gets or sets the heat flux value used in thermal studies.

## Syntax

### Visual Basic (Declaration)

```vb
Property HFValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatFlux
Dim value As System.Double

instance.HFValue = value

value = instance.HFValue
```

### C#

```csharp
System.double HFValue {get; set;}
```

### C++/CLI

```cpp
property System.double HFValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Heat flux value

## VBA Syntax

See [CWHeatFlux::HFValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatFlux~HFValue.html).

## Examples

See the [ICWHeatFlux](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html) examples.

## Remarks

After setting this property, you must select the location of the thermostat in the model and pass it to [ICWHeatFlux::SetThermostat](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~SetThermostat.html).

## See Also

[ICWHeatFlux Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html)
[ICWHeatFlux Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux_members.html)
[ICWHeatFlux::Unit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~Unit.html)
[ICWHeatFlux::ReverseDirection Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~ReverseDirection.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
