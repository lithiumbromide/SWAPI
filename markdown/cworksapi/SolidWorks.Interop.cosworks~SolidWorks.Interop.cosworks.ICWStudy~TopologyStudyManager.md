---
title: "TopologyStudyManager Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "TopologyStudyManager"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~TopologyStudyManager.html"
---

# TopologyStudyManager Property (ICWStudy)

Gets the manager of this topology study's goals, constraints, and manufacturing controls.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TopologyStudyManager As CWTopologyStudyManager
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWTopologyStudyManager

value = instance.TopologyStudyManager
```

### C#

```csharp
CWTopologyStudyManager TopologyStudyManager {get;}
```

### C++/CLI

```cpp
property CWTopologyStudyManager^ TopologyStudyManager {
   CWTopologyStudyManager^ get();
}
```

### Property Value

[ICWTopologyStudyManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)

## VBA Syntax

See [CWStudy::TopologyStudyManager](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~TopologyStudyManager.html).

## Examples

[Create Topology Study (VBA)](Create_Topology_Study_Example_VB.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWTopologyDisplacementConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html)
[ICWTopologyMassConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint.html)
[ICWTopologyMinimizeMaximumDisplacementGoal Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal.html)
[ICWTopologyDemoldControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl.html)
[ICWTopologyFactorOfSafetyConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint.html)
[ICWTopologyFrequencyConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint.html)
[ICWTopologyPreservedRegionControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl.html)
[ICWTopologyStressConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint.html)
[ICWTopologyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions.html)
[ICWTopologySymmetryControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl.html)
[ICWTopologyThicknessControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
