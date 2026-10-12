---
title: "NoOfRepeats Property (ICWFatigueEvent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueEvent"
member: "NoOfRepeats"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~NoOfRepeats.html"
---

# NoOfRepeats Property (ICWFatigueEvent)

Gets or sets the number of times to repeat the curve data.

## Syntax

### Visual Basic (Declaration)

```vb
Property NoOfRepeats As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueEvent
Dim value As System.Integer

instance.NoOfRepeats = value

value = instance.NoOfRepeats
```

### C#

```csharp
System.int NoOfRepeats {get; set;}
```

### C++/CLI

```cpp
property System.int NoOfRepeats {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Number of times to repeat the curve data (see **Remarks**)

## VBA Syntax

See [CWFatigueEvent::NoOfRepeats](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueEvent~NoOfRepeats.html).

## Examples

See the [ICWFatigueEvent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html) examples.

## Remarks

This property is valid only if this is a variable amplitude fatigue event.

## See Also

[ICWFatigueEvent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html)
[ICWFatigueEvent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent_members.html)
[ICWFatigueEvent::StartTimes Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~StartTimes.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
