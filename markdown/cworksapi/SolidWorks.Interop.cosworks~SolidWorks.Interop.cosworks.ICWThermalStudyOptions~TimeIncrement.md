---
title: "TimeIncrement Property (ICWThermalStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWThermalStudyOptions"
member: "TimeIncrement"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~TimeIncrement.html"
---

# TimeIncrement Property (ICWThermalStudyOptions)

Gets or sets the time increment. Used for thermal transient studies only.

## Syntax

### Visual Basic (Declaration)

```vb
Property TimeIncrement As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWThermalStudyOptions
Dim value As System.Double

instance.TimeIncrement = value

value = instance.TimeIncrement
```

### C#

```csharp
System.double TimeIncrement {get; set;}
```

### C++/CLI

```cpp
property System.double TimeIncrement {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Time increment

## VBA Syntax

See [CWThermalStudyOptions::TimeIncrement](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWThermalStudyOptions~TimeIncrement.html).

## Examples

See the [ICWThermalStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html) examples.

## See Also

[ICWThermalStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html)
[ICWThermalStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions_members.html)
[ICWThermalStudyOptions::TotalTime Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~TotalTime.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
