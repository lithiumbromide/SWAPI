---
title: "UseTimeCurve Property (ICWBearingLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingLoad"
member: "UseTimeCurve"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~UseTimeCurve.html"
---

# UseTimeCurve Property (ICWBearingLoad)

Obsolete. Superseded by [ICWBearingLoad::UseTimeCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~UseTimeCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseTimeCurve As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingLoad
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

See [CWBearingLoad::UseTimeCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingLoad~UseTimeCurve.html).

## See Also

[ICWBearingLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html)
[ICWBearingLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad_members.html)
[ICWBearingLoad::GetTimeCurve Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~GetTimeCurve.html)
[ICWBearingLoad::SetTimeCurve Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~SetTimeCurve.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
