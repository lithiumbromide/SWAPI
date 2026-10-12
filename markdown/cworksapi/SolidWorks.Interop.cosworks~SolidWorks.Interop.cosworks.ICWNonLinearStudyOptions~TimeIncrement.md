---
title: "TimeIncrement Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "TimeIncrement"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~TimeIncrement.html"
---

# TimeIncrement Property (ICWNonLinearStudyOptions)

Gets or sets the fixed time increment.

## Syntax

### Visual Basic (Declaration)

```vb
Property TimeIncrement As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Integer

instance.TimeIncrement = value

value = instance.TimeIncrement
```

### C#

```csharp
System.int TimeIncrement {get; set;}
```

### C++/CLI

```cpp
property System.int TimeIncrement {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Fixed time increment

## VBA Syntax

See [CWNonLinearStudyOptions::TimeIncrement](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~TimeIncrement.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinearStudyOptions::GetAutomaticTimeIncrement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~GetAutomaticTimeIncrement.html)
[ICWNonLinearStudyOptions::SetAutomaticTimeIncrement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SetAutomaticTimeIncrement.html)
[ICWNonLinearStudyOptions::EndTime Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~EndTime.html)
[ICWNonLinearStudyOptions::FixedTimeIncrement Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~FixedTimeIncrement.html)
[ICWNonLinearStudyOptions::StartTime Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~StartTime.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
