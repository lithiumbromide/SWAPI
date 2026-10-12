---
title: "UseTemperatureCurve Property (ICWHeatPower)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatPower"
member: "UseTemperatureCurve"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~UseTemperatureCurve.html"
---

# UseTemperatureCurve Property (ICWHeatPower)

Obsolete. Superseded by [ICWHeatPower::UseTemperatureCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~UseTemperatureCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseTemperatureCurve As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatPower
Dim value As System.Integer

instance.UseTemperatureCurve = value

value = instance.UseTemperatureCurve
```

### C#

```csharp
System.int UseTemperatureCurve {get; set;}
```

### C++/CLI

```cpp
property System.int UseTemperatureCurve {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to use temperature curve, 0 to not

## VBA Syntax

See [CWHeatPower::UseTemperatureCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatPower~UseTemperatureCurve.html).

## See Also

[ICWHeatPower Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html)
[ICWHeatPower Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower_members.html)
[ICWHeatPower::GetTemperatureCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~GetTemperatureCurve.html)
[ICWHeatPower::SetTemperatureCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~SetTemperatureCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
