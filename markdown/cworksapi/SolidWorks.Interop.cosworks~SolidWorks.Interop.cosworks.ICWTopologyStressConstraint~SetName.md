---
title: "SetName Method (ICWTopologyStressConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStressConstraint"
member: "SetName"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint~SetName.html"
---

# SetName Method (ICWTopologyStressConstraint)

Sets the name of this topology study stress constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetName( _
   ByVal SName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStressConstraint
Dim SName As System.String
Dim value As System.Integer

value = instance.SetName(SName)
```

### C#

```csharp
System.int SetName(
   System.string SName
)
```

### C++/CLI

```cpp
System.int SetName(
   System.String^ SName
)
```

### Parameters

- `SName`: Name of the stress constraint

### Return Value

Result code as defined in [swsTopologyStudy_StressConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_StressConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyStressConstraint::SetName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStressConstraint~SetName.html).

## Examples

See the [ICWTopologyStressConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint.html) example.

## See Also

[ICWTopologyStressConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint.html)
[ICWTopologyStressConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint_members.html)
[ICWTopologyStressConstraint::GetName Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint~GetName.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
