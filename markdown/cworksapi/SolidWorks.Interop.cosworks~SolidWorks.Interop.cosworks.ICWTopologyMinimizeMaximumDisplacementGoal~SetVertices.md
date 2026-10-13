---
title: "SetVertices Method (ICWTopologyMinimizeMaximumDisplacementGoal)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyMinimizeMaximumDisplacementGoal"
member: "SetVertices"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal~SetVertices.html"
---

# SetVertices Method (ICWTopologyMinimizeMaximumDisplacementGoal)

Sets the vertex locations of this minimize maximum displacement goal.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetVertices( _
   ByVal VerticesDispArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyMinimizeMaximumDisplacementGoal
Dim VerticesDispArray As System.Object
Dim value As System.Integer

value = instance.SetVertices(VerticesDispArray)
```

### C#

```csharp
System.int SetVertices(
   System.object VerticesDispArray
)
```

### C++/CLI

```cpp
System.int SetVertices(
   System.Object^ VerticesDispArray
)
```

### Parameters

- `VerticesDispArray`: Array of vertex objects

### Return Value

Result code as defined in [swsTopologyStudy_MinMaxDisplacementGoalErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_MinMaxDisplacementGoalErrors_e.html)

## VBA Syntax

See [CWTopologyMinimizeMaximumDisplacementGoal::SetVertices](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyMinimizeMaximumDisplacementGoal~SetVertices.html).

## Examples

See the [ICWTopologyMinimizeMaximumDisplacementGoal](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal.html) example.

## See Also

[ICWTopologyMinimizeMaximumDisplacementGoal Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal.html)
[ICWTopologyMinimizeMaximumDisplacementGoal Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal_members.html)
[ICWTopologyMinimizeMaximumDisplacementGoal::RemoveAllVertices Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal~RemoveAllVertices.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
