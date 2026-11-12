---
title: "FatigueEventBeginEdit Method (ICWFatigueEvent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueEvent"
member: "FatigueEventBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~FatigueEventBeginEdit.html"
---

# FatigueEventBeginEdit Method (ICWFatigueEvent)

Starts editing the fatigue event.

## Syntax

### Visual Basic (Declaration)

```vb
Sub FatigueEventBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueEvent

instance.FatigueEventBeginEdit()
```

### C#

```csharp
void FatigueEventBeginEdit()
```

### C++/CLI

```cpp
void FatigueEventBeginEdit();
```

## VBA Syntax

See [CWFatigueEvent::FatigueEventBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueEvent~FatigueEventBeginEdit.html).

## Examples

See the [ICWFatigueEvent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html) examples.

## Remarks

To start editing a fatigue event, you must call this method. You must call [ICWFatigueEvent::FatigueEventEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFatigueEvent~FatigueEventEndEdit.html) to end editing a fatigue event. Changes are not applied unless you call both methods.

## See Also

[ICWFatigueEvent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html)
[ICWFatigueEvent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
