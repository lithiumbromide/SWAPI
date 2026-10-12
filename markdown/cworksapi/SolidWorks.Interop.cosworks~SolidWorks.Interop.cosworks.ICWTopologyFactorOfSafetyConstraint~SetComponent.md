---
title: "SetComponent Method (ICWTopologyFactorOfSafetyConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyFactorOfSafetyConstraint"
member: "SetComponent"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint~SetComponent.html"
---

# SetComponent Method (ICWTopologyFactorOfSafetyConstraint)

Sets the component of this topology study Factor Of Safety constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetComponent( _
   ByVal NComponent As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyFactorOfSafetyConstraint
Dim NComponent As System.Integer
Dim value As System.Integer

value = instance.SetComponent(NComponent)
```

### C#

```csharp
System.int SetComponent(
   System.int NComponent
)
```

### C++/CLI

```cpp
System.int SetComponent(
   System.int NComponent
)
```

### Parameters

- `NComponent`: [swsTopologyStudyFactorOfSafetyComponentType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyFactorOfSafetyComponentType_e.html).swsTopologyFactorOfSafetyCompType_MaxVONMises

### Return Value

Result code as defined in [swsTopologyStudy_FOSConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_FOSConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyFactorOfSafetyConstraint::SetComponent](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyFactorOfSafetyConstraint~SetComponent.html).

## Examples

See the [ICWTopologyFactorOfSafetyConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint.html) example.

## Remarks

This Factor Of Safety constraint equation:

```
FOS_component comparator value
```

## See Also

[ICWTopologyFactorOfSafetyConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint.html)
[ICWTopologyFactorOfSafetyConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
