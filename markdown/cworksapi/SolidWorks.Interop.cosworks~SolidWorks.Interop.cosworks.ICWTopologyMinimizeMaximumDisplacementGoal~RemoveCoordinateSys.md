---
title: "RemoveCoordinateSys Method (ICWTopologyMinimizeMaximumDisplacementGoal)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyMinimizeMaximumDisplacementGoal"
member: "RemoveCoordinateSys"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal~RemoveCoordinateSys.html"
---

# RemoveCoordinateSys Method (ICWTopologyMinimizeMaximumDisplacementGoal)

Removes the selected coordinate system from this minimize maximum displacement goal.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveCoordinateSys()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyMinimizeMaximumDisplacementGoal

instance.RemoveCoordinateSys()
```

### C#

```csharp
void RemoveCoordinateSys()
```

### C++/CLI

```cpp
void RemoveCoordinateSys();
```

## VBA Syntax

See [CWTopologyMinimizeMaximumDisplacementGoal::RemoveCoordinateSys](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyMinimizeMaximumDisplacementGoal~RemoveCoordinateSys.html).

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

## Availability

SOLIDWORKS Simulation API 2019 SP0
