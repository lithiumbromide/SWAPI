---
title: "SetVertices Method (ICWTopologyDisplacementConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDisplacementConstraint"
member: "SetVertices"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetVertices.html"
---

# SetVertices Method (ICWTopologyDisplacementConstraint)

Sets the vertexes of a load-bearing face on which to apply this topology study displacement constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetVertices( _
   ByVal VerticesDispArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDisplacementConstraint
Dim VerticesDispArray As System.Object
Dim value As System.Integer

value = instance.SetVertices(VerticesDispArray)
```

### C#

```csharp
System.int SetVertices(
   System.object VerticesDispArray
)
```

### C++/CLI

```cpp
System.int SetVertices(
   System.Object^ VerticesDispArray
)
```

### Parameters

- `VerticesDispArray`: Array of vertexes

### Return Value

Result code as defined in [swsTopologyStudy_DisplacementConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_DisplacementConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyDisplacementConstraint::SetVertices](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyDisplacementConstraint~SetVertices.html).

## Examples

See the [ICWTopologyDisplacementConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html) example.

## Remarks

This method is valid only if [ICWTopologyDisplacementConstraint::SetLocationPreference](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetLocationPreference.html) sets [swsTopologyStudyDisplacementConstraintLocationOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyDisplacementConstraintLocationOption_e.html).swsTopologyDisplacementConstraintLocationOption_UserDefine.

## See Also

[ICWTopologyDisplacementConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html)
[ICWTopologyDisplacementConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint_members.html)
[ICWTopologyDisplacementConstraint::RemoveAllVertices Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~RemoveAllVertices.html)

## Availability

SOLIDWORKS Simulation API 2020 SP0
