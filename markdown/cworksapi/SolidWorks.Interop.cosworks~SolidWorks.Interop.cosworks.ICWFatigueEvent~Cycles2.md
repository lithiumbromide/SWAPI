---
title: "Cycles2 Property (ICWFatigueEvent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueEvent"
member: "Cycles2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~Cycles2.html"
---

# Cycles2 Property (ICWFatigueEvent)

Gets or sets the number of cycles associated with this fatigue event.

## Syntax

### Visual Basic (Declaration)

```vb
Property Cycles2 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueEvent
Dim value As System.Double

instance.Cycles2 = value

value = instance.Cycles2
```

### C#

```csharp
System.double Cycles2 {get; set;}
```

### C++/CLI

```cpp
property System.double Cycles2 {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

1.0 <= Number of cycles <= 1e+36

## VBA Syntax

See [CWFatigueEvent::Cycles2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueEvent~Cycles2.html).

## Examples

See the [ICWFatigueEvent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html) examples.

## See Also

[ICWFatigueEvent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html)
[ICWFatigueEvent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent_members.html)
[ICWFatigueEvent::LoadingRatio Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~LoadingRatio.html)
[ICWFatigueEvent::LoadingType Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~LoadingType.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
