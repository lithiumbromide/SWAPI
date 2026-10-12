---
title: "Cycles Property (ICWFatigueEvent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueEvent"
member: "Cycles"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~Cycles.html"
---

# Cycles Property (ICWFatigueEvent)

Obsolete. Superseded by [ICWFatigueEvent::Cycles2.](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~Cycles2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property Cycles As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueEvent
Dim value As System.Integer

instance.Cycles = value

value = instance.Cycles
```

### C#

```csharp
System.int Cycles {get; set;}
```

### C++/CLI

```cpp
property System.int Cycles {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Number of cycles (see **Remarks**)

## VBA Syntax

See [CWFatigueEvent::Cycles](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueEvent~Cycles.html).

## Remarks

This property is valid only if this is a constant amplitude fatigue event.

## See Also

[ICWFatigueEvent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html)
[ICWFatigueEvent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent_members.html)
[ICWFatigueEvent::LoadingRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~LoadingRatio.html)
[ICWFatigueEvent::LoadingType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~LoadingType.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
