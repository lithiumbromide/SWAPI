---
title: "SetCoordinateSystemPreference Method (ICWTopologyMinimizeMaximumDisplacementGoal)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyMinimizeMaximumDisplacementGoal"
member: "SetCoordinateSystemPreference"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal~SetCoordinateSystemPreference.html"
---

# SetCoordinateSystemPreference Method (ICWTopologyMinimizeMaximumDisplacementGoal)

Sets the coordinate system preference for this minimize maximum displacement goal.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCoordinateSystemPreference( _
   ByVal NCSPreference As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyMinimizeMaximumDisplacementGoal
Dim NCSPreference As System.Integer
Dim value As System.Integer

value = instance.SetCoordinateSystemPreference(NCSPreference)
```

### C#

```csharp
System.int SetCoordinateSystemPreference(
   System.int NCSPreference
)
```

### C++/CLI

```cpp
System.int SetCoordinateSystemPreference(
   System.int NCSPreference
)
```

### Parameters

- `NCSPreference`: Coodinate system preference as defined in [swsTopologyStudyDisplacementCoordinateSysOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyDisplacementCoordinateSysOption_e.html)

### Return Value

Result code as defined in [swsTopologyStudy_MinMaxDisplacementGoalErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_MinMaxDisplacementGoalErrors_e.html)

## VBA Syntax

See [CWTopologyMinimizeMaximumDisplacementGoal::SetCoordinateSystemPreference](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyMinimizeMaximumDisplacementGoal~SetCoordinateSystemPreference.html).

## Examples

See the [ICWTopologyMinimizeMaximumDisplacementGoal](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal.html) example.

## Remarks

This method is valid for all displacement components except [swsTopologyStudyDisplacementComponentType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyDisplacementComponentType_e.html).swsTopologyStudyDisplacementCompType_URES (URES: Resultant Displacement (Absolute)).

If NCSPreference is set to swsTopologyStudyDisplacementCoordinateSysOption_e.swsTopologyDisplacementCoordinateSysOption_UserDefine, then use [ICWTopologyMinimizeMaximumDisplacementGoal::SetCoordinateSystem](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal~SetCoordinateSystem.html) to set the coordinate system.

## See Also

[ICWTopologyMinimizeMaximumDisplacementGoal Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal.html)
[ICWTopologyMinimizeMaximumDisplacementGoal Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
