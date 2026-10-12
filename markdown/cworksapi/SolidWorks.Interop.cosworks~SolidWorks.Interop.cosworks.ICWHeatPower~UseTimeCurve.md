---
title: "UseTimeCurve Property (ICWHeatPower)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatPower"
member: "UseTimeCurve"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~UseTimeCurve.html"
---

# UseTimeCurve Property (ICWHeatPower)

Obsolete. Superseded by [ICWHeatPower::UseTimeCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~UseTimeCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseTimeCurve As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatPower
Dim value As System.Integer

instance.UseTimeCurve = value

value = instance.UseTimeCurve
```

### C#

```csharp
System.int UseTimeCurve {get; set;}
```

### C++/CLI

```cpp
property System.int UseTimeCurve {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to use time curve, 0 to not

## VBA Syntax

See [CWHeatPower::UseTimeCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatPower~UseTimeCurve.html).

## See Also

[ICWHeatPower Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html)
[ICWHeatPower Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower_members.html)
[ICWHeatPower::GetTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~GetTimeCurve.html)
[ICWHeatPower::SetTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~SetTimeCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
