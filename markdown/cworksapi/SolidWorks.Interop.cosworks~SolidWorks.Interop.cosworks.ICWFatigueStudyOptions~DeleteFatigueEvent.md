---
title: "DeleteFatigueEvent Method (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "DeleteFatigueEvent"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~DeleteFatigueEvent.html"
---

# DeleteFatigueEvent Method (ICWFatigueStudyOptions)

Deletes the specified fatigue event.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DeleteFatigueEvent( _
   ByVal SName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
Dim SName As System.String

instance.DeleteFatigueEvent(SName)
```

### C#

```csharp
void DeleteFatigueEvent(
   System.string SName
)
```

### C++/CLI

```cpp
void DeleteFatigueEvent(
   System.String^ SName
)
```

### Parameters

- `SName`: Name of the fatigue event to delete (see **Remarks**)

## VBA Syntax

See [CWFatigueStudyOptions::DeleteFatigueEvent](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~DeleteFatigueEvent.html).

## Remarks

To delete a fatigue event by name, you need to first find the name by iterating through all of the fatigue events:

1. Call [ICWFatigueStudyOptions::LoadingEventCount](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~LoadingEventCount.html) to get the number of fatigue events, `n`.
2. In a loop where i = 0 to `n` - 1, call [ICWFatigueStudyOptions::GetFatigueEvent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~GetFatigueEvent.html)(`i, ErrorCode`) to get each [ICWFatigueEvent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html).
3. Populate SName with [ICWFatigueEvent::Name](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~Name.html) of the fatigue event you want to delete.

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
