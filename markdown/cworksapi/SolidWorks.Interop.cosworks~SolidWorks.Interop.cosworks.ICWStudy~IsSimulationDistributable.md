---
title: "IsSimulationDistributable Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "IsSimulationDistributable"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~IsSimulationDistributable.html"
---

# IsSimulationDistributable Property (ICWStudy)

Gets whether this study supports network simulation.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsSimulationDistributable As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As System.Boolean

value = instance.IsSimulationDistributable
```

### C#

```csharp
System.bool IsSimulationDistributable {get;}
```

### C++/CLI

```cpp
property System.bool IsSimulationDistributable {
   System.bool get();
}
```

### Property Value

True if this study supports network simulation, false if not

## VBA Syntax

See [CWStudy::IsSimulationDistributable](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~IsSimulationDistributable.html).

## Remarks

This method is valid only for SOLIDWORKS Simulation Professional or Premium.

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::OffLoad Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~OffLoad.html)
[ICWStudyManager::ManageDistributedSimulation Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~ManageDistributedSimulation.html)
[ICWStudyManager::SetDistributedSimulation Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~SetDistributedSimulation.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
