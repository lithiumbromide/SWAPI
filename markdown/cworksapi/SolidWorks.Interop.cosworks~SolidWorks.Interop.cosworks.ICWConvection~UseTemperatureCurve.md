---
title: "UseTemperatureCurve Property (ICWConvection)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWConvection"
member: "UseTemperatureCurve"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~UseTemperatureCurve.html"
---

# UseTemperatureCurve Property (ICWConvection)

Obsolete. Superseded by [ICWConvection::UseTemperatureCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~UseTemperatureCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseTemperatureCurve As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWConvection
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

See [CWConvection::UseTemperatureCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWConvection~UseTemperatureCurve.html).

## See Also

[ICWConvection Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection.html)
[ICWConvection Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection_members.html)
[ICWConvection::GetTemperatureCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~GetTemperatureCurve.html)
[ICWConvection::SetTemperatureCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~SetTemperatureCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
