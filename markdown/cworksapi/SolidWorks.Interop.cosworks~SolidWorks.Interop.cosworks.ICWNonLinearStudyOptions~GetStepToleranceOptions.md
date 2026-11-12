---
title: "GetStepToleranceOptions Method (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "GetStepToleranceOptions"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~GetStepToleranceOptions.html"
---

# GetStepToleranceOptions Method (ICWNonLinearStudyOptions)

Gets convergence and equilibrium parameters.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetStepToleranceOptions( _
   ByRef NEqilibriumIteration As System.Integer, _
   ByRef NMaxEqilibriumIteration As System.Integer, _
   ByRef DConvTol As System.Double, _
   ByRef DPlasticityTol As System.Double, _
   ByRef NSingularityEleFactor As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim NEqilibriumIteration As System.Integer
Dim NMaxEqilibriumIteration As System.Integer
Dim DConvTol As System.Double
Dim DPlasticityTol As System.Double
Dim NSingularityEleFactor As System.Double

instance.GetStepToleranceOptions(NEqilibriumIteration, NMaxEqilibriumIteration, DConvTol, DPlasticityTol, NSingularityEleFactor)
```

### C#

```csharp
void GetStepToleranceOptions(
   out System.int NEqilibriumIteration,
   out System.int NMaxEqilibriumIteration,
   out System.double DConvTol,
   out System.double DPlasticityTol,
   out System.double NSingularityEleFactor
)
```

### C++/CLI

```cpp
void GetStepToleranceOptions(
   [Out] System.int NEqilibriumIteration,
   [Out] System.int NMaxEqilibriumIteration,
   [Out] System.double DConvTol,
   [Out] System.double DPlasticityTol,
   [Out] System.double NSingularityEleFactor
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

## VBA Syntax

See [CWNonLinearStudyOptions::GetStepToleranceOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~GetStepToleranceOptions.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinearStudyOptions::SetStepToleranceOptions Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SetStepToleranceOptions.html)

## Availability

SOLIDWORKS Simulation 2010 SP3.0
