---
title: "FixedTimeIncrement Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "FixedTimeIncrement"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~FixedTimeIncrement.html"
---

# FixedTimeIncrement Property (ICWNonLinearStudyOptions)

Gets or sets a value for the solution increment.

## Syntax

### Visual Basic (Declaration)

```vb
Property FixedTimeIncrement As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Double

instance.FixedTimeIncrement = value

value = instance.FixedTimeIncrement
```

### C#

```csharp
System.double FixedTimeIncrement {get; set;}
```

### C++/CLI

```cpp
property System.double FixedTimeIncrement {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Fixed solution increment

## VBA Syntax

See [CWNonLinearStudyOptions::FixedTimeIncrement](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~FixedTimeIncrement.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinearStudyOptions::GetAutomaticTimeIncrement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~GetAutomaticTimeIncrement.html)
[ICWNonLinearStudyOptions::SetAutomaticTimeIncrement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SetAutomaticTimeIncrement.html)
[ICWNonLinearStudyOptions::EndTime Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~EndTime.html)
[ICWNonLinearStudyOptions::StartTime Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~StartTime.html)
[ICWNonLinearStudyOptions::TimeIncrement Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~TimeIncrement.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
