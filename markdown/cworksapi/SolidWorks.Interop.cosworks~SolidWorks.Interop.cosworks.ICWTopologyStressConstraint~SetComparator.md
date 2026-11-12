---
title: "SetComparator Method (ICWTopologyStressConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStressConstraint"
member: "SetComparator"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint~SetComparator.html"
---

# SetComparator Method (ICWTopologyStressConstraint)

Sets the comparator to use in the equation of this topology study stress constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetComparator( _
   ByVal NComparator As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStressConstraint
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

- `NComparator`: [swsTopologyStudyConstraintComparator_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyConstraintComparator_e.html).swsTopologyConstraintComparator_IsLessThan

### Return Value

Result code as defined in [swsTopologyStudy_StressConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_StressConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyStressConstraint::SetComparator](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStressConstraint~SetComparator.html).

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
