---
title: "EndEdit Method (ICWTopologyDisplacementConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDisplacementConstraint"
member: "EndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~EndEdit.html"
---

# EndEdit Method (ICWTopologyDisplacementConstraint)

Ends editing this topology study displacement constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function EndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDisplacementConstraint
Dim value As System.Integer

value = instance.EndEdit()
```

### C#

```csharp
System.int EndEdit()
```

### C++/CLI

```cpp
System.int EndEdit();
```

### Return Value

Result code as defined in [swsTopologyStudy_DisplacementConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_DisplacementConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyDisplacementConstraint::EndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyDisplacementConstraint~EndEdit.html).

## Examples

See the [ICWTopologyDisplacementConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html) example.

## Remarks

To begin editing this displacement constraint, call [ICWTopologyDisplacementConstraint::BeginEdit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~BeginEdit.html).

## See Also

[ICWTopologyDisplacementConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html)
[ICWTopologyDisplacementConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
