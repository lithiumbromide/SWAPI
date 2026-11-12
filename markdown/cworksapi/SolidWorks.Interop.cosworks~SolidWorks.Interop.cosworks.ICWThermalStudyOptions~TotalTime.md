---
title: "TotalTime Property (ICWThermalStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWThermalStudyOptions"
member: "TotalTime"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~TotalTime.html"
---

# TotalTime Property (ICWThermalStudyOptions)

Gets or sets the total time. Used for thermal transient studies only.

## Syntax

### Visual Basic (Declaration)

```vb
Property TotalTime As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWThermalStudyOptions
Dim value As System.Double

instance.TotalTime = value

value = instance.TotalTime
```

### C#

```csharp
System.double TotalTime {get; set;}
```

### C++/CLI

```cpp
property System.double TotalTime {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Total time

## VBA Syntax

See [CWThermalStudyOptions::TotalTime](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWThermalStudyOptions~TotalTime.html).

## Examples

See the [ICWThermalStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html) examples.

## See Also

[ICWThermalStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html)
[ICWThermalStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions_members.html)
[ICWThermalStudyOptions::TimeIncrement Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~TimeIncrement.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
