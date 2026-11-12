---
title: "StartTime Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "StartTime"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~StartTime.html"
---

# StartTime Property (ICWNonLinearStudyOptions)

Gets the start time.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property StartTime As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Double

value = instance.StartTime
```

### C#

```csharp
System.double StartTime {get;}
```

### C++/CLI

```cpp
property System.double StartTime {
   System.double get();
}
```

### Property Value

Start time

## VBA Syntax

See [CWNonLinearStudyOptions::StartTime](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~StartTime.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinearStudyOptions::GetAutomaticTimeIncrement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~GetAutomaticTimeIncrement.html)
[ICWNonLinearStudyOptions::SetAutomaticTimeIncrement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SetAutomaticTimeIncrement.html)
[ICWNonLinearStudyOptions::EndTime Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~EndTime.html)
[ICWNonLinearStudyOptions::FixedTimeIncrement Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~FixedTimeIncrement.html)
[ICWNonLinearStudyOptions::TimeIncrement Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~TimeIncrement.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
