---
title: "SetComponent Method (ICWTopologyStressConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStressConstraint"
member: "SetComponent"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint~SetComponent.html"
---

# SetComponent Method (ICWTopologyStressConstraint)

Sets the component to use in the equation of this topology study stress constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetComponent( _
   ByVal NComponent As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStressConstraint
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

- `NComponent`: [swsTopologyStudyStressComponentType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyStressComponentType_e.html).swsTopologyStressCompType_VONMises

### Return Value

Result code as defined in [swsTopologyStudy_StressConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_StressConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyStressConstraint::SetComponent](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStressConstraint~SetComponent.html).

## Examples

See the [ICWTopologyStressConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint.html) example.

## Remarks

This stress constraint equation:

```
stress_component comparator value
```

## See Also

[ICWTopologyStressConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint.html)
[ICWTopologyStressConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
