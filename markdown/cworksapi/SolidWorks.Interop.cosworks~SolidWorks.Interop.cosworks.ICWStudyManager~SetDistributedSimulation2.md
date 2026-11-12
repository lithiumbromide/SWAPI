---
title: "SetDistributedSimulation2 Method (ICWStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyManager"
member: "SetDistributedSimulation2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~SetDistributedSimulation2.html"
---

# SetDistributedSimulation2 Method (ICWStudyManager)

Sets whether to enable network simulation.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDistributedSimulation2( _
   ByVal BNetSim As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyManager
Dim BNetSim As System.Boolean
Dim value As System.Integer

value = instance.SetDistributedSimulation2(BNetSim)
```

### C#

```csharp
System.int SetDistributedSimulation2(
   System.bool BNetSim
)
```

### C++/CLI

```cpp
System.int SetDistributedSimulation2(
   System.bool BNetSim
)
```

### Parameters

- `BNetSim`: -1 or true to enable network simulation, 0 or false to disable it

### Return Value

Error code as defined in [swsDistributedSimulationError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDistributedSimulationError_e.html)

## VBA Syntax

See [CWStudyManager::SetDistributedSimulation2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyManager~SetDistributedSimulation2.html).

## See Also

[ICWStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager.html)
[ICWStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
