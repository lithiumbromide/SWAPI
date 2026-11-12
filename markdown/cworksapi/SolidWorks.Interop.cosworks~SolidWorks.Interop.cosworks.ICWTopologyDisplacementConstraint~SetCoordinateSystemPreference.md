---
title: "SetCoordinateSystemPreference Method (ICWTopologyDisplacementConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDisplacementConstraint"
member: "SetCoordinateSystemPreference"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetCoordinateSystemPreference.html"
---

# SetCoordinateSystemPreference Method (ICWTopologyDisplacementConstraint)

Sets the coordinate system preference for this topology study displacement constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCoordinateSystemPreference( _
   ByVal NCSPreference As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDisplacementConstraint
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

Result code as defined in [swsTopologyStudy_DisplacementConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_DisplacementConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyDisplacementConstraint::SetCoordinateSystemPreference](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyDisplacementConstraint~SetCoordinateSystemPreference.html).

## Examples

See the [ICWTopologyDisplacementConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html) example.

## Remarks

This method is valid only if [ICWTopologyDisplacementConstraint::SetComponent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetComponent.html) sets something other than [swsTopologyStudyDisplacementComponentType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyDisplacementComponentType_e.html).swsTopologyStudyDisplacementCompType_URES (URES: Resultant Displacement (Absolute)).

If NCSPreference is set to swsTopologyStudyDisplacementCoordinateSysOption_e.swsTopologyDisplacementCoordinateSysOption_UserDefine, then use [ICWTopologyDisplacementConstraint::SetCoordinateSystem](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetCoordinateSystem.html) to set the coordinate system.

## See Also

[ICWTopologyDisplacementConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html)
[ICWTopologyDisplacementConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
