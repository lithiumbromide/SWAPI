---
title: "LoadingType Property (ICWFatigueEvent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueEvent"
member: "LoadingType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~LoadingType.html"
---

# LoadingType Property (ICWFatigueEvent)

Gets or sets the type of fatigue loading to determine the stress peaks and alternating stresses.

## Syntax

### Visual Basic (Declaration)

```vb
Property LoadingType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueEvent
Dim value As System.Integer

instance.LoadingType = value

value = instance.LoadingType
```

### C#

```csharp
System.int LoadingType {get; set;}
```

### C++/CLI

```cpp
property System.int LoadingType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Fatigue loading type as defined in [swsFatigueLoadingType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueLoadingType_e.html) (see **Remarks**)

## VBA Syntax

See [CWFatigueEvent::LoadingType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueEvent~LoadingType.html).

## Examples

See the [ICWFatigueEvent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html) examples.

## Remarks

This property is valid only if this is a constant amplitude fatigue event.

## See Also

[ICWFatigueEvent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html)
[ICWFatigueEvent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent_members.html)
[ICWFatigueEvent::Cycles Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~Cycles.html)
[ICWFatigueEvent::LoadingRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~LoadingRatio.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
