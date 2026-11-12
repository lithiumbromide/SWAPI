---
title: "SolverType Property (ICWThermalStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWThermalStudyOptions"
member: "SolverType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~SolverType.html"
---

# SolverType Property (ICWThermalStudyOptions)

Gets or sets the solver type associated with the study.

## Syntax

### Visual Basic (Declaration)

```vb
Property SolverType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWThermalStudyOptions
Dim value As System.Integer

instance.SolverType = value

value = instance.SolverType
```

### C#

```csharp
System.int SolverType {get; set;}
```

### C++/CLI

```cpp
property System.int SolverType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Solver type as defined in [swsSolverType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSolverType_e.html) (see **Remarks**)

## VBA Syntax

See [CWThermalStudyOptions::SolverType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWThermalStudyOptions~SolverType.html).

## Examples

See the [ICWThermalStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html) examples.

## Remarks

The automatic option is not supported for thermal studies; it supports static, frequency, and buckling studies only.

## See Also

[ICWThermalStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html)
[ICWThermalStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
