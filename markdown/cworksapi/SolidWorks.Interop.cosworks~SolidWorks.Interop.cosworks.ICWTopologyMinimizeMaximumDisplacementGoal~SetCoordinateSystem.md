---
title: "SetCoordinateSystem Method (ICWTopologyMinimizeMaximumDisplacementGoal)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyMinimizeMaximumDisplacementGoal"
member: "SetCoordinateSystem"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal~SetCoordinateSystem.html"
---

# SetCoordinateSystem Method (ICWTopologyMinimizeMaximumDisplacementGoal)

Sets the coordinate system for this minimize maximum displacement goal.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCoordinateSystem( _
   ByVal DispatchCS As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyMinimizeMaximumDisplacementGoal
Dim DispatchCS As System.Object
Dim value As System.Integer

value = instance.SetCoordinateSystem(DispatchCS)
```

### C#

```csharp
System.int SetCoordinateSystem(
   System.object DispatchCS
)
```

### C++/CLI

```cpp
System.int SetCoordinateSystem(
   System.Object^ DispatchCS
)
```

### Parameters

- `DispatchCS`: Cartesian coordinate system object

### Return Value

Result code as defined in [swsTopologyStudy_MinMaxDisplacementGoalErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_MinMaxDisplacementGoalErrors_e.html)

## VBA Syntax

See [CWTopologyMinimizeMaximumDisplacementGoal::SetCoordinateSystem](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyMinimizeMaximumDisplacementGoal~SetCoordinateSystem.html).

## Examples

See the [ICWTopologyMinimizeMaximumDisplacementGoal](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal.html) example.

## Remarks

This method is valid:

- only for a Cartesian coordinate system,

- and -

- if [ICWTopologyMinimizeMaximumDisplacementGoal::SetCoordinateSystemPreference](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal~SetCoordinateSystemPreference.html) sets [swsTopologyStudyDisplacementCoordinateSysOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyDisplacementCoordinateSysOption_e.html).swsTopologyDisplacementCoordinateSysOption_UserDefine,

- and -

- if [ICWTopologyMinimizeMaximumDisplacementGoal::SetComponent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal~SetComponent.html) sets any displacement component other than [swsTopologyStudyDisplacementComponentType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyDisplacementComponentType_e.html).swsTopologyDisplacementCompType_URES.

## See Also

[ICWTopologyMinimizeMaximumDisplacementGoal Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal.html)
[ICWTopologyMinimizeMaximumDisplacementGoal Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal_members.html)
[ICWTopologyMinimizeMaximumDisplacementGoal::RemoveCoordinateSys Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal~RemoveCoordinateSys.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
