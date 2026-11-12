---
title: "RelaxationFactor Property (ICWThermalStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWThermalStudyOptions"
member: "RelaxationFactor"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~RelaxationFactor.html"
---

# RelaxationFactor Property (ICWThermalStudyOptions)

Gets or sets the status of the relaxation factor.

## Syntax

### Visual Basic (Declaration)

```vb
Property RelaxationFactor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWThermalStudyOptions
Dim value As System.Integer

instance.RelaxationFactor = value

value = instance.RelaxationFactor
```

### C#

```csharp
System.int RelaxationFactor {get; set;}
```

### C++/CLI

```cpp
property System.int RelaxationFactor {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Thermal relaxation factor as defined in [swsThermalRelaxationFactor_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsThermalRelaxationFactor_e.html)

## VBA Syntax

See [CWThermalStudyOptions::RelaxationFactor](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWThermalStudyOptions~RelaxationFactor.html).

## See Also

[ICWThermalStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html)
[ICWThermalStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
