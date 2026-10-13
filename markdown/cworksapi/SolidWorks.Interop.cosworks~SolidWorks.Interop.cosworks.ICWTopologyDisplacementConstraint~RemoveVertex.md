---
title: "RemoveVertex Method (ICWTopologyDisplacementConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDisplacementConstraint"
member: "RemoveVertex"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~RemoveVertex.html"
---

# RemoveVertex Method (ICWTopologyDisplacementConstraint)

Obsolete. Superseded by [ICWTopologyDisplacementConstraint::RemoveAllVertices](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~RemoveAllVertices.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveVertex()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDisplacementConstraint

instance.RemoveVertex()
```

### C#

```csharp
void RemoveVertex()
```

### C++/CLI

```cpp
void RemoveVertex();
```

## VBA Syntax

See [CWTopologyDisplacementConstraint::RemoveVertex](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyDisplacementConstraint~RemoveVertex.html).

## Remarks

This method is valid only if [ICWTopologyDisplacementConstraint::SetLocationPreference](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetLocationPreference.html) sets [swsTopologyStudyDisplacementConstraintLocationOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyDisplacementConstraintLocationOption_e.html).swsTopologyDisplacementConstraintLocationOption_UserDefine.

## See Also

[ICWTopologyDisplacementConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html)
[ICWTopologyDisplacementConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint_members.html)
[ICWTopologyDisplacementConstraint::SetVertex Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetVertex.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
