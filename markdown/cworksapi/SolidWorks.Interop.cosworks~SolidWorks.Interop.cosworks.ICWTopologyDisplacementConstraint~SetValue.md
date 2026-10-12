---
title: "SetValue Method (ICWTopologyDisplacementConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDisplacementConstraint"
member: "SetValue"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetValue.html"
---

# SetValue Method (ICWTopologyDisplacementConstraint)

Sets the value in the equation of this topology study displacement constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetValue( _
   ByVal DValue As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDisplacementConstraint
Dim DValue As System.Double
Dim value As System.Integer

value = instance.SetValue(DValue)
```

### C#

```csharp
System.int SetValue(
   System.double DValue
)
```

### C++/CLI

```cpp
System.int SetValue(
   System.double DValue
)
```

### Parameters

- `DValue`: Value in the displacement constraint equation

### Return Value

Result code as defined in [swsTopologyStudy_DisplacementConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_DisplacementConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyDisplacementConstraint::SetValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyDisplacementConstraint~SetValue.html).

## Examples

See the [ICWTopologyDisplacementConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html) example.

## Remarks

DValue depends on [ICWTopologyDisplacementConstraint::SetValuationPreference](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetValuationPreference.html).

This displacement constraint equation:

```
disp_component comparator DValue
```

## See Also

[ICWTopologyDisplacementConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html)
[ICWTopologyDisplacementConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint_members.html)
[ICWTopologyDisplacementConstraint::SetUnit Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetUnit.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
