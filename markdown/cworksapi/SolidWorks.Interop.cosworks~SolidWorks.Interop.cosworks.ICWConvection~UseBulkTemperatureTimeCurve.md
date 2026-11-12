---
title: "UseBulkTemperatureTimeCurve Property (ICWConvection)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWConvection"
member: "UseBulkTemperatureTimeCurve"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~UseBulkTemperatureTimeCurve.html"
---

# UseBulkTemperatureTimeCurve Property (ICWConvection)

Obsolete. Superseded by [ICWConvection::UseBulkTemperatureTimeCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~UseBulkTemperatureTimeCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseBulkTemperatureTimeCurve As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWConvection
Dim value As System.Integer

instance.UseBulkTemperatureTimeCurve = value

value = instance.UseBulkTemperatureTimeCurve
```

### C#

```csharp
System.int UseBulkTemperatureTimeCurve {get; set;}
```

### C++/CLI

```cpp
property System.int UseBulkTemperatureTimeCurve {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to use bulk temperature curve, 0 to not

## VBA Syntax

See [CWConvection::UseBulkTemperatureTimeCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWConvection~UseBulkTemperatureTimeCurve.html).

## See Also

[ICWConvection Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection.html)
[ICWConvection Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection_members.html)
[ICWConvection::GetBulkTemperatureTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~GetBulkTemperatureTimeCurve.html)
[ICWConvection::SetBulkTemperatureTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~SetBulkTemperatureTimeCurve.html)
[ICWConvection::BulkAmbientTemperature Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~BulkAmbientTemperature.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
