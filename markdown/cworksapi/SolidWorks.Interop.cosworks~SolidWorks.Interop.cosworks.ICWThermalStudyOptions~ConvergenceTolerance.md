---
title: "ConvergenceTolerance Property (ICWThermalStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWThermalStudyOptions"
member: "ConvergenceTolerance"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~ConvergenceTolerance.html"
---

# ConvergenceTolerance Property (ICWThermalStudyOptions)

Gets or sets the convergence tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Property ConvergenceTolerance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWThermalStudyOptions
Dim value As System.Double

instance.ConvergenceTolerance = value

value = instance.ConvergenceTolerance
```

### C#

```csharp
System.double ConvergenceTolerance {get; set;}
```

### C++/CLI

```cpp
property System.double ConvergenceTolerance {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Convergence tolerance

## VBA Syntax

See [CWThermalStudyOptions::ConvergenceTolerance](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWThermalStudyOptions~ConvergenceTolerance.html).

## See Also

[ICWThermalStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html)
[ICWThermalStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
