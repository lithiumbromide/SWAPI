---
title: "SetIterationOption Method (ICWTopologyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyOptions"
member: "SetIterationOption"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions~SetIterationOption.html"
---

# SetIterationOption Method (ICWTopologyStudyOptions)

Sets the method for calculating the maximum number of iterations needed by the optimization algorithm to reach convergence.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetIterationOption( _
   ByVal NIterationOption As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyOptions
Dim NIterationOption As System.Integer

instance.SetIterationOption(NIterationOption)
```

### C#

```csharp
void SetIterationOption(
   System.int NIterationOption
)
```

### C++/CLI

```cpp
void SetIterationOption(
   System.int NIterationOption
)
```

### Parameters

- `NIterationOption`: Iteration option as defined in [swsTopologyIterationOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyIterationOption_e.html)

## VBA Syntax

See [CWTopologyStudyOptions::SetIterationOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyOptions~SetIterationOption.html).

## See Also

[ICWTopologyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions.html)
[ICWTopologyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
