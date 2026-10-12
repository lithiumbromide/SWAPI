---
title: "EndEdit Method (ICWTopologyMinimizeMaximumDisplacementGoal)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyMinimizeMaximumDisplacementGoal"
member: "EndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal~EndEdit.html"
---

# EndEdit Method (ICWTopologyMinimizeMaximumDisplacementGoal)

Ends editing this minimize maximum displacement goal.

## Syntax

### Visual Basic (Declaration)

```vb
Function EndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyMinimizeMaximumDisplacementGoal
Dim value As System.Integer

value = instance.EndEdit()
```

### C#

```csharp
System.int EndEdit()
```

### C++/CLI

```cpp
System.int EndEdit();
```

### Return Value

Result code as defined in [swsTopologyStudy_MinMaxDisplacementGoalErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_MinMaxDisplacementGoalErrors_e.html)

## VBA Syntax

See [CWTopologyMinimizeMaximumDisplacementGoal::EndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyMinimizeMaximumDisplacementGoal~EndEdit.html).

## Examples

See the [ICWTopologyMinimizeMaximumDisplacementGoal](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal.html) example.

## Remarks

To begin editing this goal, call [ICWTopologyMinimizeMaximumDisplacementGoal::BeginEdit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal~BeginEdit.html).

## See Also

[ICWTopologyMinimizeMaximumDisplacementGoal Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal.html)
[ICWTopologyMinimizeMaximumDisplacementGoal Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
