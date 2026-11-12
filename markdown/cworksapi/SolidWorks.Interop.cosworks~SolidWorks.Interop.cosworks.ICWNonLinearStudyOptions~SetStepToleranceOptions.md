---
title: "SetStepToleranceOptions Method (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "SetStepToleranceOptions"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SetStepToleranceOptions.html"
---

# SetStepToleranceOptions Method (ICWNonLinearStudyOptions)

Sets convergence and equilibrium parameters.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetStepToleranceOptions( _
   ByVal NEqilibriumIteration As System.Integer, _
   ByVal NMaxEqilibriumIteration As System.Integer, _
   ByVal DConvTol As System.Double, _
   ByVal DPlasticityTol As System.Double, _
   ByVal NSingularityEleFactor As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim NEqilibriumIteration As System.Integer
Dim NMaxEqilibriumIteration As System.Integer
Dim DConvTol As System.Double
Dim DPlasticityTol As System.Double
Dim NSingularityEleFactor As System.Double
Dim value As System.Integer

value = instance.SetStepToleranceOptions(NEqilibriumIteration, NMaxEqilibriumIteration, DConvTol, DPlasticityTol, NSingularityEleFactor)
```

### C#

```csharp
System.int SetStepToleranceOptions(
   System.int NEqilibriumIteration,
   System.int NMaxEqilibriumIteration,
   System.double DConvTol,
   System.double DPlasticityTol,
   System.double NSingularityEleFactor
)
```

### C++/CLI

```cpp
System.int SetStepToleranceOptions(
   System.int NEqilibriumIteration,
   System.int NMaxEqilibriumIteration,
   System.double DConvTol,
   System.double DPlasticityTol,
   System.double NSingularityEleFactor
)
```

### Parameters

- `NEqilibriumIteration`: Frequency of performing equilibrium in number of solution steps
- `NMaxEqilibriumIteration`: Maximum number of equilibrium iterations for any solution step
- `DConvTol`: Relative displacement tolerance used for equilibrium convergence
- `DPlasticityTol`: Tolerance for strain increment for models with creep or plasticity
- `NSingularityEleFactor`: Stiffness singularity elimination factor:

  - normal solution if set to 1
  - if <1.0, then the program modifies stiffness terms causing singularity to help convergence

  If normal solution fails, trying a different value; for example, 0 may help convergence.

### Return Value

Status as defined in [swsNonLinearStudyOptionsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsNonLinearStudyOptionsError_e.html)

## VBA Syntax

See [CWNonLinearStudyOptions::SetStepToleranceOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~SetStepToleranceOptions.html).

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinearStudyOptions::GetStepToleranceOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~GetStepToleranceOptions.html)

## Availability

SOLIDWORKS Simulation 2010 SP3.0
