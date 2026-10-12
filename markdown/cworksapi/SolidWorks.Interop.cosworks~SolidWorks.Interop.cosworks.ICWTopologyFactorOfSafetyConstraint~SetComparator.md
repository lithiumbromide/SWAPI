---
title: "SetComparator Method (ICWTopologyFactorOfSafetyConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyFactorOfSafetyConstraint"
member: "SetComparator"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint~SetComparator.html"
---

# SetComparator Method (ICWTopologyFactorOfSafetyConstraint)

Sets the comparator to use in the equation of this topology study Factor Of Safety constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetComparator( _
   ByVal NComparator As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyFactorOfSafetyConstraint
Dim NComparator As System.Integer
Dim value As System.Integer

value = instance.SetComparator(NComparator)
```

### C#

```csharp
System.int SetComparator(
   System.int NComparator
)
```

### C++/CLI

```cpp
System.int SetComparator(
   System.int NComparator
)
```

### Parameters

- `NComparator`: [swsTopologyStudyConstraintComparator_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyConstraintComparator_e.html).swsTopologyConstraintComparator_IsGreaterThan

### Return Value

Result code as defined in [swsTopologyStudy_FOSConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_FOSConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyFactorOfSafetyConstraint::SetComparator](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyFactorOfSafetyConstraint~SetComparator.html).

## Examples

See the [ICWTopologyFactorOfSafetyConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint.html) example.

## Remarks

The Factor Of Safety constraint equation:

```
FOS_component comparator value
```

## See Also

[ICWTopologyFactorOfSafetyConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint.html)
[ICWTopologyFactorOfSafetyConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
