---
title: "UseTemperatureCurve Property (ICWRadiation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRadiation"
member: "UseTemperatureCurve"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~UseTemperatureCurve.html"
---

# UseTemperatureCurve Property (ICWRadiation)

Obsolete. Superseded by [ICWRadiation::UseTemperatureCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~UseTemperatureCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseTemperatureCurve As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRadiation
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

See [CWRadiation::UseTemperatureCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRadiation~UseTemperatureCurve.html).

## See Also

[ICWRadiation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html)
[ICWRadiation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation_members.html)
[ICWRadiation::GetTemperatureCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~GetTemperatureCurve.html)
[ICWRadiation::SetTemperatureCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~SetTemperatureCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
