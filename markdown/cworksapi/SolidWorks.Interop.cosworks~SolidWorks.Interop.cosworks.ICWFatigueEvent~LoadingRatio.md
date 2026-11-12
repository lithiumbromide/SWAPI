---
title: "LoadingRatio Property (ICWFatigueEvent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueEvent"
member: "LoadingRatio"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~LoadingRatio.html"
---

# LoadingRatio Property (ICWFatigueEvent)

Gets or sets the loading ratio for this fatigue event.

## Syntax

### Visual Basic (Declaration)

```vb
Property LoadingRatio As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueEvent
Dim value As System.Double

instance.LoadingRatio = value

value = instance.LoadingRatio
```

### C#

```csharp
System.double LoadingRatio {get; set;}
```

### C++/CLI

```cpp
property System.double LoadingRatio {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Loading ratio; a negative value indicates a reversal of the load direction (see **Remarks**)

## VBA Syntax

See [CWFatigueEvent::LoadingRatio](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueEvent~LoadingRatio.html).

## Examples

See the [ICWFatigueEvent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html) examples.

## Remarks

This method is valid only if this is a constant amplitude fatigue event and only if [ICWFatigueEvent::LoadingType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFatigueEvent~LoadingType.html) = [swsFatigueLoadingType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueLoadingType_e.html).swsFatigueLoadingType_LoadingRatio.

## See Also

[ICWFatigueEvent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html)
[ICWFatigueEvent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent_members.html)
[ICWFatigueEvent::Cycles Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~Cycles.html)
[ICWFatigueEvent::LoadingType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~LoadingType.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
