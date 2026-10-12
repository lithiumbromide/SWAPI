---
title: "GetClusterComputers Method (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "GetClusterComputers"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~GetClusterComputers.html"
---

# GetClusterComputers Method (ICWStudy)

Gets the list of names of the computers participating in this study's distributed simulation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetClusterComputers( _
   ByRef ComputerNames As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim ComputerNames As System.Object
Dim value As System.Integer

value = instance.GetClusterComputers(ComputerNames)
```

### C#

```csharp
System.int GetClusterComputers(
   out System.object ComputerNames
)
```

### C++/CLI

```cpp
System.int GetClusterComputers(
   [Out] System.Object^ ComputerNames
)
```

### Parameters

- `ComputerNames`: Array of computer names

### Return Value

Error code as defined in [swsDistributedSimulationError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDistributedSimulationError_e.html)

## VBA Syntax

See [CWStudy::GetClusterComputers](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~GetClusterComputers.html).

## Remarks

This method is valid only if:

- The license is SOLIDWORKS Simulation Professional or Premium.
- [ICWStudy::IsSimulationDistributable](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~IsSimulationDistributable.html) is true.
- [ICWStudy::OffLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~OffLoad.html) is true.

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::SetClusterComputers Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~SetClusterComputers.html)
[ICWStudy::IsSimulationDistributable Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~IsSimulationDistributable.html)
[ICWStudy::OffLoad Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~OffLoad.html)
[ICWStudyManager::ManageDistributedSimulation Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~ManageDistributedSimulation.html)
[ICWStudyManager::SetDistributedSimulation Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~SetDistributedSimulation.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
