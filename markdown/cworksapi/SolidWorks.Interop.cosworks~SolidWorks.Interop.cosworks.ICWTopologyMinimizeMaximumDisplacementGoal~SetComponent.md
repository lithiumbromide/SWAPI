---
title: "SetComponent Method (ICWTopologyMinimizeMaximumDisplacementGoal)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyMinimizeMaximumDisplacementGoal"
member: "SetComponent"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal~SetComponent.html"
---

# SetComponent Method (ICWTopologyMinimizeMaximumDisplacementGoal)

Sets the displacement component of this minimize maximum displacement goal.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetComponent( _
   ByVal NDispComponent As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyMinimizeMaximumDisplacementGoal
Dim NDispComponent As System.Integer
Dim value As System.Integer

value = instance.SetComponent(NDispComponent)
```

### C#

```csharp
System.int SetComponent(
   System.int NDispComponent
)
```

### C++/CLI

```cpp
System.int SetComponent(
   System.int NDispComponent
)
```

### Parameters

- `NDispComponent`: Displacement component as defined in [swsTopologyStudyDisplacementComponentType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyDisplacementComponentType_e.html)

### Return Value

Result code as defined in [swsTopologyStudy_MinMaxDisplacementGoalErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_MinMaxDisplacementGoalErrors_e.html)

## VBA Syntax

See [CWTopologyMinimizeMaximumDisplacementGoal::SetComponent](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyMinimizeMaximumDisplacementGoal~SetComponent.html).

## Examples

See the [ICWTopologyMinimizeMaximumDisplacementGoal](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal.html) example.

## See Also

[ICWTopologyMinimizeMaximumDisplacementGoal Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal.html)
[ICWTopologyMinimizeMaximumDisplacementGoal Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
