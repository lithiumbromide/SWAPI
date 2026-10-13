---
title: "SetIterationLimit Method (ICWTopologyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyOptions"
member: "SetIterationLimit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions~SetIterationLimit.html"
---

# SetIterationLimit Method (ICWTopologyStudyOptions)

Sets the maximum number of iterations for the optimization algorithm to reach convergence.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetIterationLimit( _
   ByVal NIterationLimit As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyOptions
Dim NIterationLimit As System.Integer

instance.SetIterationLimit(NIterationLimit)
```

### C#

```csharp
void SetIterationLimit(
   System.int NIterationLimit
)
```

### C++/CLI

```cpp
void SetIterationLimit(
   System.int NIterationLimit
)
```

### Parameters

- `NIterationLimit`: 20 < Iteration limit < 101

## VBA Syntax

See [CWTopologyStudyOptions::SetIterationLimit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyOptions~SetIterationLimit.html).

## Remarks

This method is valid only if [ICWTopologyStudyOptions::SetIterationOption](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions~SetIterationOption.html) is set to [swsTopologyIterationOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyIterationOption_e.html).IterationOption_UserDef.

## See Also

[ICWTopologyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions.html)
[ICWTopologyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
