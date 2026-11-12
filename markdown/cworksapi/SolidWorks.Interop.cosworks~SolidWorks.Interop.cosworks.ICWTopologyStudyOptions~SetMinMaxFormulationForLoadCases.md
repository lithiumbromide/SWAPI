---
title: "SetMinMaxFormulationForLoadCases Method (ICWTopologyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyOptions"
member: "SetMinMaxFormulationForLoadCases"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions~SetMinMaxFormulationForLoadCases.html"
---

# SetMinMaxFormulationForLoadCases Method (ICWTopologyStudyOptions)

Sets whether to use the min max formulation for multiple load cases.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMinMaxFormulationForLoadCases( _
   ByVal NMinMaxFormulationForLoadCases As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyOptions
Dim NMinMaxFormulationForLoadCases As System.Integer

instance.SetMinMaxFormulationForLoadCases(NMinMaxFormulationForLoadCases)
```

### C#

```csharp
void SetMinMaxFormulationForLoadCases(
   System.int NMinMaxFormulationForLoadCases
)
```

### C++/CLI

```cpp
void SetMinMaxFormulationForLoadCases(
   System.int NMinMaxFormulationForLoadCases
)
```

### Parameters

- `NMinMaxFormulationForLoadCases`: Activation option for min max formulation for load cases as defined in [swsTopologyActivationOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyActivationOption_e.html)

## VBA Syntax

See [CWTopologyStudyOptions::SetMinMaxFormulationForLoadCases](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyOptions~SetMinMaxFormulationForLoadCases.html).

## Remarks

If NMinMaxFormulationForLoadCases is set to swsTopologyActivationOption_e.ActivationOption_Activate, then multiple load cases (defined with the Load Case Manager) can act on a component independently.

## See Also

[ICWTopologyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions.html)
[ICWTopologyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
