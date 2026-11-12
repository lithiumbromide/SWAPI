---
title: "TimeSteps Property (ICWThermalStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWThermalStudyOptions"
member: "TimeSteps"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~TimeSteps.html"
---

# TimeSteps Property (ICWThermalStudyOptions)

Gets or sets the time step at which you want to use the temperature profile as an initial condition. Used for thermal transient studies only.

## Syntax

### Visual Basic (Declaration)

```vb
Property TimeSteps As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWThermalStudyOptions
Dim value As System.Integer

instance.TimeSteps = value

value = instance.TimeSteps
```

### C#

```csharp
System.int TimeSteps {get; set;}
```

### C++/CLI

```cpp
property System.int TimeSteps {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Time step

## VBA Syntax

See [CWThermalStudyOptions::TimeSteps](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWThermalStudyOptions~TimeSteps.html).

## See Also

[ICWThermalStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html)
[ICWThermalStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
