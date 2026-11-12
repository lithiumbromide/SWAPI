---
title: "SolutionType Property (ICWThermalStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWThermalStudyOptions"
member: "SolutionType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~SolutionType.html"
---

# SolutionType Property (ICWThermalStudyOptions)

Gets or sets the thermal solution type.

## Syntax

### Visual Basic (Declaration)

```vb
Property SolutionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWThermalStudyOptions
Dim value As System.Integer

instance.SolutionType = value

value = instance.SolutionType
```

### C#

```csharp
System.int SolutionType {get; set;}
```

### C++/CLI

```cpp
property System.int SolutionType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Thermal solution as defined in [swsThermalSolutionType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsThermalSolutionType_e.html)

## VBA Syntax

See [CWThermalStudyOptions::SolutionType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWThermalStudyOptions~SolutionType.html).

## Examples

See the [ICWThermalStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html) examples.

## See Also

[ICWThermalStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html)
[ICWThermalStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
