---
title: "ICWTopologyMinimizeMaximumDisplacementGoal Interface"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyMinimizeMaximumDisplacementGoal"
member: ""
kind: "interface"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal.html"
---

# ICWTopologyMinimizeMaximumDisplacementGoal Interface

Allows access to a minimize maximum displacement goal in a topology study. **NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICWTopologyMinimizeMaximumDisplacementGoal
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyMinimizeMaximumDisplacementGoal
```

### C#

```csharp
public interface ICWTopologyMinimizeMaximumDisplacementGoal
```

### C++/CLI

```cpp
public interface class ICWTopologyMinimizeMaximumDisplacementGoal
```

## VBA Syntax

See [CWTopologyMinimizeMaximumDisplacementGoal](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyMinimizeMaximumDisplacementGoal.html).

## Examples

[Create Topology Study (VBA)](Create_Topology_Study_Example_VB.htm)

## Remarks

The minimize maximum displacement goal automatically sets a default mass constraint that cannot be removed. Use [ICWTopologyMassConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint.html) to modify the default mass constraint as needed. Use [ICWTopologyStudyManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html) to add one more constraint as needed.

See the **Goals and Constraints** topic in the Simulation user-interface help for more information.

## Accessors

[ICWTopologyStudyManager::MinimizeMaximumDisplacementGoal](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~MinimizeMaximumDisplacementGoal.html)

[ICWTopologyStudyManager::CreateGoal](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~CreateGoal.html)

## See Also

[ICWTopologyMinimizeMaximumDisplacementGoal Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal_members.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
