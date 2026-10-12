---
title: "StartTimes Property (ICWFatigueEvent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueEvent"
member: "StartTimes"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~StartTimes.html"
---

# StartTimes Property (ICWFatigueEvent)

Gets or sets the start time for this fatigue event.

## Syntax

### Visual Basic (Declaration)

```vb
Property StartTimes As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueEvent
Dim value As System.Double

instance.StartTimes = value

value = instance.StartTimes
```

### C#

```csharp
System.double StartTimes {get; set;}
```

### C++/CLI

```cpp
property System.double StartTimes {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Start time in seconds for this event (see **Remarks**)

## VBA Syntax

See [CWFatigueEvent::StartTimes](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueEvent~StartTimes.html).

## Examples

See the [ICWFatigueEvent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html) examples.

## Remarks

This property is valid only if this is a variable amplitude fatigue event and only if there are multiple events in the fatigue study.

## See Also

[ICWFatigueEvent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html)
[ICWFatigueEvent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent_members.html)
[ICWFatigueEvent::NoOfRepeats Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~NoOfRepeats.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
