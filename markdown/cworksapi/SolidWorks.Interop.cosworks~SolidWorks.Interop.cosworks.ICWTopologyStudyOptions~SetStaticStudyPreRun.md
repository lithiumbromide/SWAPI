---
title: "SetStaticStudyPreRun Method (ICWTopologyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyOptions"
member: "SetStaticStudyPreRun"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions~SetStaticStudyPreRun.html"
---

# SetStaticStudyPreRun Method (ICWTopologyStudyOptions)

Sets whether to have the solver run a static analysis before running the topology optimization algorithm.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetStaticStudyPreRun( _
   ByVal NPreRun As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyOptions
Dim NPreRun As System.Integer

instance.SetStaticStudyPreRun(NPreRun)
```

### C#

```csharp
void SetStaticStudyPreRun(
   System.int NPreRun
)
```

### C++/CLI

```cpp
void SetStaticStudyPreRun(
   System.int NPreRun
)
```

### Parameters

- `NPreRun`: 1 to run a static analysis first (default), 0 to not

## VBA Syntax

See [CWTopologyStudyOptions::SetStaticStudyPreRun](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyOptions~SetStaticStudyPreRun.html).

## See Also

[ICWTopologyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions.html)
[ICWTopologyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
