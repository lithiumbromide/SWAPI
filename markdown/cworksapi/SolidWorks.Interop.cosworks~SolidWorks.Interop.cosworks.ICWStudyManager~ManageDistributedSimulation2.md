---
title: "ManageDistributedSimulation2 Method (ICWStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyManager"
member: "ManageDistributedSimulation2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~ManageDistributedSimulation2.html"
---

# ManageDistributedSimulation2 Method (ICWStudyManager)

Sets up network simulation.

## Syntax

### Visual Basic (Declaration)

```vb
Function ManageDistributedSimulation2( _
   ByVal BOffLoad As System.Boolean, _
   ByVal ComputerNames As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyManager
Dim BOffLoad As System.Boolean
Dim ComputerNames As System.Object
Dim value As System.Integer

value = instance.ManageDistributedSimulation2(BOffLoad, ComputerNames)
```

### C#

```csharp
System.int ManageDistributedSimulation2(
   System.bool BOffLoad,
   System.object ComputerNames
)
```

### C++/CLI

```cpp
System.int ManageDistributedSimulation2(
   System.bool BOffLoad,
   System.Object^ ComputerNames
)
```

### Parameters

- `BOffLoad`: -1 or true to offload the coordinating computer's simulation processing to other computers on the network, 0 or false to let the coordinating computer participate in network simulation
- `ComputerNames`: Array of names of computers participating in network simulation

### Return Value

Error code as defined in [swsDistributedSimulationError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDistributedSimulationError_e.html)

## VBA Syntax

See [CWStudyManager::ManageDistributedSimulation2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyManager~ManageDistributedSimulation2.html).

## See Also

[ICWStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager.html)
[ICWStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
