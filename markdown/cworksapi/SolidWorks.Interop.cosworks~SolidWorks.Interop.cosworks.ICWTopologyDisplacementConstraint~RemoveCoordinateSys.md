---
title: "RemoveCoordinateSys Method (ICWTopologyDisplacementConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDisplacementConstraint"
member: "RemoveCoordinateSys"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~RemoveCoordinateSys.html"
---

# RemoveCoordinateSys Method (ICWTopologyDisplacementConstraint)

Removes the selected coordinate system from this topology study displacement constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveCoordinateSys()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDisplacementConstraint

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

See [CWTopologyDisplacementConstraint::RemoveCoordinateSys](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyDisplacementConstraint~RemoveCoordinateSys.html).

## Examples

See the [ICWTopologyDisplacementConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html) example.

## Remarks

This method is valid only:

- for a Cartesian coordinate system,

- and -

- if [ICWTopologyDisplacementConstraint::SetCoordinateSystemPreference](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetCoordinateSystemPreference.html) sets [swsTopologyStudyDisplacementCoordinateSysOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyDisplacementCoordinateSysOption_e.html).swsTopologyDisplacementCoordinateSysOption_UserDefine,

- and -

- if [ICWTopologyDisplacementConstraint::SetComponent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetComponent.html) sets any displacement component other than [swsTopologyStudyDisplacementComponentType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyDisplacementComponentType_e.html).swsTopologyDisplacementCompType_URES.

## See Also

[ICWTopologyDisplacementConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html)
[ICWTopologyDisplacementConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint_members.html)
[ICWTopologyDisplacementConstraint::SetCoordinateSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetCoordinateSystem.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
