---
title: "EndTime Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "EndTime"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~EndTime.html"
---

# EndTime Property (ICWNonLinearStudyOptions)

Gets or sets the end time (solution time) for the nonlinear study.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndTime As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Double

instance.EndTime = value

value = instance.EndTime
```

### C#

```csharp
System.double EndTime {get; set;}
```

### C++/CLI

```cpp
property System.double EndTime {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

End time

## VBA Syntax

See [CWNonLinearStudyOptions::EndTime](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~EndTime.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinearStudyOptions::GetAutomaticTimeIncrement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~GetAutomaticTimeIncrement.html)
[ICWNonLinearStudyOptions::SetAutomaticTimeIncrement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SetAutomaticTimeIncrement.html)
[ICWNonLinearStudyOptions::FixedTimeIncrement Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~FixedTimeIncrement.html)
[ICWNonLinearStudyOptions::StartTime Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~StartTime.html)
[ICWNonLinearStudyOptions::TimeIncrement Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~TimeIncrement.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
