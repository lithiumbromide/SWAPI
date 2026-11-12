---
title: "SetName Method (ICWTopologyDisplacementConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDisplacementConstraint"
member: "SetName"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetName.html"
---

# SetName Method (ICWTopologyDisplacementConstraint)

Sets the name of this topology study displacement constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetName( _
   ByVal SName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDisplacementConstraint
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

- `SName`: Name of the topology study displacement constraint

### Return Value

Result code as defined in [swsTopologyStudy_DisplacementConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_DisplacementConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyDisplacementConstraint::SetName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyDisplacementConstraint~SetName.html).

## See Also

[ICWTopologyDisplacementConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html)
[ICWTopologyDisplacementConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint_members.html)
[ICWTopologyDisplacementConstraint::GetName Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~GetName.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
