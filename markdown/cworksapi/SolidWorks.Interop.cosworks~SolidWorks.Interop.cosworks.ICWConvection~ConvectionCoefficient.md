---
title: "ConvectionCoefficient Property (ICWConvection)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWConvection"
member: "ConvectionCoefficient"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~ConvectionCoefficient.html"
---

# ConvectionCoefficient Property (ICWConvection)

Gets or sets the convection coefficient used in defining convection for thermal studies.

## Syntax

### Visual Basic (Declaration)

```vb
Property ConvectionCoefficient As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWConvection
Dim value As System.Double

instance.ConvectionCoefficient = value

value = instance.ConvectionCoefficient
```

### C#

```csharp
System.double ConvectionCoefficient {get; set;}
```

### C++/CLI

```cpp
property System.double ConvectionCoefficient {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Convection coefficient

## VBA Syntax

See [CWConvection::ConvectionCoefficient](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWConvection~ConvectionCoefficient.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)
[Apply Thermostat-controlled Heat Power with Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power with Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)

## See Also

[ICWConvection Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection.html)
[ICWConvection Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
