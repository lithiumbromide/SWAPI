---
title: "SetConvergenceCheck Method (ICWTopologyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyOptions"
member: "SetConvergenceCheck"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions~SetConvergenceCheck.html"
---

# SetConvergenceCheck Method (ICWTopologyStudyOptions)

Sets whether to have the solver check for convergence with each iteration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetConvergenceCheck( _
   ByVal NConvergenceCheck As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyOptions
Dim NConvergenceCheck As System.Integer

instance.SetConvergenceCheck(NConvergenceCheck)
```

### C#

```csharp
void SetConvergenceCheck(
   System.int NConvergenceCheck
)
```

### C++/CLI

```cpp
void SetConvergenceCheck(
   System.int NConvergenceCheck
)
```

### Parameters

- `NConvergenceCheck`: Activation option for the convergence check as defined in [swsTopologyActivationOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyActivationOption_e.html)

## VBA Syntax

See [CWTopologyStudyOptions::SetConvergenceCheck](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyOptions~SetConvergenceCheck.html).

## Examples

See the [ICWTopologyStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions.html) example.

## Remarks

If NConvergenceCheck is set to swsTopologyActivationOption_e:

- ActivationOption_Activate, then the solver checks with each iteration whether the objective or the constraint has converged. If so, then it stops the solution. Numerical tolerances between iterations are relaxed (draft quality).
- ActivationOption_Deactivate, then the solver uses a smaller numerical tolerance (high quality), and both the objective and constraint need to be satisfied for the solver to stop.

## See Also

[ICWTopologyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions.html)
[ICWTopologyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
