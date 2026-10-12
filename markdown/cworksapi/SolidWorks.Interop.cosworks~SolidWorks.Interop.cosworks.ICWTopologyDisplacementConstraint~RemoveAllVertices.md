---
title: "RemoveAllVertices Method (ICWTopologyDisplacementConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDisplacementConstraint"
member: "RemoveAllVertices"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~RemoveAllVertices.html"
---

# RemoveAllVertices Method (ICWTopologyDisplacementConstraint)

Removes all load-bearing face vertexes from this topology study displacement constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveAllVertices()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDisplacementConstraint

instance.RemoveAllVertices()
```

### C#

```csharp
void RemoveAllVertices()
```

### C++/CLI

```cpp
void RemoveAllVertices();
```

## VBA Syntax

See [CWTopologyDisplacementConstraint::RemoveAllVertices](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyDisplacementConstraint~RemoveAllVertices.html).

## Remarks

This method is valid only if [ICWTopologyDisplacementConstraint::SetLocationPreference](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetLocationPreference.html) sets [swsTopologyStudyDisplacementConstraintLocationOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyDisplacementConstraintLocationOption_e.html).swsTopologyDisplacementConstraintLocationOption_UserDefine.

## See Also

[ICWTopologyDisplacementConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html)
[ICWTopologyDisplacementConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint_members.html)
[ICWTopologyDisplacementConstraint::SetVertices Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetVertices.html)

## Availability

SOLIDWORKS Simulation API 2020 SP0
