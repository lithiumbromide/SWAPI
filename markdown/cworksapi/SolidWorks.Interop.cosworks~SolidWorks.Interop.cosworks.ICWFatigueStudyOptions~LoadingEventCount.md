---
title: "LoadingEventCount Property (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "LoadingEventCount"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~LoadingEventCount.html"
---

# LoadingEventCount Property (ICWFatigueStudyOptions)

Gets the number of loading events in the fatigue study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property LoadingEventCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
Dim value As System.Integer

value = instance.LoadingEventCount
```

### C#

```csharp
System.int LoadingEventCount {get;}
```

### C++/CLI

```cpp
property System.int LoadingEventCount {
   System.int get();
}
```

### Property Value

Number of loading events

## VBA Syntax

See [CWFatigueStudyOptions::LoadingEventCount](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~LoadingEventCount.html).

## Examples

See the [ICWFatigueStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html) examples.

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)
[ICWFatigueStudyOptions::GetFatigueEvent Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~GetFatigueEvent.html)
[ICWFatigueStudyOptions::DeleteFatigueEvent Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~DeleteFatigueEvent.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
