---
title: "BulkAmbientTemperature Property (ICWConvection)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWConvection"
member: "BulkAmbientTemperature"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~BulkAmbientTemperature.html"
---

# BulkAmbientTemperature Property (ICWConvection)

Gets or sets the bulk ambient temperature for defining convection for thermal studies.

## Syntax

### Visual Basic (Declaration)

```vb
Property BulkAmbientTemperature As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWConvection
Dim value As System.Double

instance.BulkAmbientTemperature = value

value = instance.BulkAmbientTemperature
```

### C#

```csharp
System.double BulkAmbientTemperature {get; set;}
```

### C++/CLI

```cpp
property System.double BulkAmbientTemperature {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Bulk ambient temperature

## VBA Syntax

See [CWConvection::BulkAmbientTemperature](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWConvection~BulkAmbientTemperature.html).

## Examples

[Apply Thermostat-controlled Heat Power with Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)
[Apply Thermostat-controlled Heat Power with Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power with Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)

## See Also

[ICWConvection Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection.html)
[ICWConvection Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection_members.html)
[ICWConvection::GetBulkTemperatureTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~GetBulkTemperatureTimeCurve.html)
[ICWConvection::SetBulkTemperatureTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~SetBulkTemperatureTimeCurve.html)
[ICWConvection::UseBulkTemperatureTimeCurve Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~UseBulkTemperatureTimeCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
