---
title: "FatigueEventEndEdit Method (ICWFatigueEvent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueEvent"
member: "FatigueEventEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~FatigueEventEndEdit.html"
---

# FatigueEventEndEdit Method (ICWFatigueEvent)

Ends editing the fatigue event.

## Syntax

### Visual Basic (Declaration)

```vb
Function FatigueEventEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueEvent
Dim value As System.Integer

value = instance.FatigueEventEndEdit()
```

### C#

```csharp
System.int FatigueEventEndEdit()
```

### C++/CLI

```cpp
System.int FatigueEventEndEdit();
```

### Return Value

Error as defined in [swsFatigueEventEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueEventEndEditError_e.html)

## VBA Syntax

See [CWFatigueEvent::FatigueEventEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueEvent~FatigueEventEndEdit.html).

## Examples

See the [ICWFatigueEvent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html) examples.

## Remarks

You must call [ICWFatigueEvent::FatigueEventBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFatigueEvent~FatigueEventBeginEdit.html) to start editing a fatigue event. To end editing a fatigue event, you must call this method. Changes are not applied unless you call both methods.

## See Also

[ICWFatigueEvent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html)
[ICWFatigueEvent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
