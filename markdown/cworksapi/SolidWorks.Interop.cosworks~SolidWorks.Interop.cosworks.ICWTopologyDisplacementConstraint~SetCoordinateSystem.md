---
title: "SetCoordinateSystem Method (ICWTopologyDisplacementConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDisplacementConstraint"
member: "SetCoordinateSystem"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetCoordinateSystem.html"
---

# SetCoordinateSystem Method (ICWTopologyDisplacementConstraint)

Sets the coordinate system of this topology study displacement constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCoordinateSystem( _
   ByVal DispatchCS As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDisplacementConstraint
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

Result code as defined in [swsTopologyStudy_DisplacementConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_DisplacementConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyDisplacementConstraint::SetCoordinateSystem](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyDisplacementConstraint~SetCoordinateSystem.html).

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
[ICWTopologyDisplacementConstraint::RemoveCoordinateSys Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~RemoveCoordinateSys.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
