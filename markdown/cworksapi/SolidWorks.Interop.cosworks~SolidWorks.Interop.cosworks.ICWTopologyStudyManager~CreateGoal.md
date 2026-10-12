---
title: "CreateGoal Method (ICWTopologyStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyManager"
member: "CreateGoal"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~CreateGoal.html"
---

# CreateGoal Method (ICWTopologyStudyManager)

Adds the specified optimization goal to this topology study.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateGoal( _
   ByVal NGoalType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyManager
Dim NGoalType As System.Integer
Dim value As System.Integer

value = instance.CreateGoal(NGoalType)
```

### C#

```csharp
System.int CreateGoal(
   System.int NGoalType
)
```

### C++/CLI

```cpp
System.int CreateGoal(
   System.int NGoalType
)
```

### Parameters

- `NGoalType`: Type of optimization goal to create as defined in [swsTopologyStudyGoalType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyGoalType_e.html)

### Return Value

Result code as defined in [swsTopologyStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyError_e.html)

## VBA Syntax

See [CWTopologyStudyManager::CreateGoal](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyManager~CreateGoal.html).

## Examples

See the [ICWTopologyStudyManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html) example.

## Remarks

Only one optimization goal can be set in a topology study. A default constraint is automatically created in some cases.

| If the goal is... | Then its default constraint is... |
| --- | --- |
| Maximize stiffness (best stiffness to weight ratio) | Mass ( ICWTopologyMassConstraint ) |
| Minimize maximum displacement | Mass (ICWTopologyMassConstraint) |
| Minimize mass with displacement constraint | N/A |

It is not possible to remove the default constraint, either through the user interface or through the API, but it is possible to modify its properties.

You can add up to two different constraints for a given optimization goal.

## See Also

[ICWTopologyStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)
[ICWTopologyStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
