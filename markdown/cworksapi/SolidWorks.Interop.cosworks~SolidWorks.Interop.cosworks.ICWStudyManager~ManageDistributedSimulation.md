---
title: "ManageDistributedSimulation Method (ICWStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyManager"
member: "ManageDistributedSimulation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~ManageDistributedSimulation.html"
---

# ManageDistributedSimulation Method (ICWStudyManager)

Obsolete. Superseded by [ICWStudyManager::ManageDistributedSimulation2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~ManageDistributedSimulation2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ManageDistributedSimulation( _
   ByVal BOffLoad As System.Integer, _
   ByVal ComputerNames As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyManager
Dim BOffLoad As System.Integer
Dim ComputerNames As System.Object
Dim value As System.Integer

value = instance.ManageDistributedSimulation(BOffLoad, ComputerNames)
```

### C#

```csharp
System.int ManageDistributedSimulation(
   System.int BOffLoad,
   System.object ComputerNames
)
```

### C++/CLI

```cpp
System.int ManageDistributedSimulation(
   System.int BOffLoad,
   System.Object^ ComputerNames
)
```

### Parameters

- `BOffLoad`: True to offload the coordinating computer's simulation processing to other computers on the network, false to let the coordinating computer participate in network simulation
- `ComputerNames`: Array of names of computers participating in network simulation

### Return Value

Error code as defined in [swsDistributedSimulationError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDistributedSimulationError_e.html)

## VBA Syntax

See [CWStudyManager::ManageDistributedSimulation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyManager~ManageDistributedSimulation.html).

## Remarks

This method is valid only for SOLIDWORKS Simulation Professional or Premium.

Network simulation requires the Intel Direct Sparse solver. Before running network simulation:

1. Set the solver type to [swsSolverType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSolverType_e.html).swsSolverTypeINTELCluster using one of:

  - [ICWBucklingStudyOptions::SolverType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~SolverType.html)
  - [ICWDynamicStudyOptions::SolverType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SolverType.html)
  - [ICWFrequencyStudyOptions::SolverType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~SolverType.html)
  - [ICWNonLinearStudyOptions::SolverType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SolverType.html)
  - [ICWStaticStudyOptions::SolverType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~SolverType.html)
  - [ICWThermalStudyOptions::SolverType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~SolverType.html)
2. Call [ICWStudyManager::SetDistributedSimulation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~SetDistributedSimulation.html) to enable network simulation.

## See Also

[ICWStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager.html)
[ICWStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager_members.html)
[ICWStudy::GetClusterComputers Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~GetClusterComputers.html)
[ICWStudy::SetClusterComputers Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~SetClusterComputers.html)
[ICWStudy::IsSimulationDistributable Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~IsSimulationDistributable.html)
[ICWStudy::OffLoad Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~OffLoad.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
