---
title: "SetDistributedSimulation Method (ICWStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyManager"
member: "SetDistributedSimulation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~SetDistributedSimulation.html"
---

# SetDistributedSimulation Method (ICWStudyManager)

Obsolete. Superseded by [ICWStudyManager::SetDistributedSimulation2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~SetDistributedSimulation2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDistributedSimulation( _
   ByVal BNetSim As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyManager
Dim BNetSim As System.Integer
Dim value As System.Integer

value = instance.SetDistributedSimulation(BNetSim)
```

### C#

```csharp
System.int SetDistributedSimulation(
   System.int BNetSim
)
```

### C++/CLI

```cpp
System.int SetDistributedSimulation(
   System.int BNetSim
)
```

### Parameters

- `BNetSim`: True to enable network simulation, false to disable it

### Return Value

Error code as defined in [swsDistributedSimulationError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDistributedSimulationError_e.html)

## VBA Syntax

See [CWStudyManager::SetDistributedSimulation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyManager~SetDistributedSimulation.html).

## Remarks

This method is valid only for SOLIDWORKS Simulation Professional or Premium.

## See Also

[ICWStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager.html)
[ICWStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager_members.html)
[ICWStudyManager::ManageDistributedSimulation Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~ManageDistributedSimulation.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
