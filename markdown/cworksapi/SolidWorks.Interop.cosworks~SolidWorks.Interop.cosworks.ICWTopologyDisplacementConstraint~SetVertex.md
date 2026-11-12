---
title: "SetVertex Method (ICWTopologyDisplacementConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDisplacementConstraint"
member: "SetVertex"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetVertex.html"
---

# SetVertex Method (ICWTopologyDisplacementConstraint)

Obsolete. Superseded by [ICWTopologyDisplacementConstraint::SetVertices](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetVertices.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetVertex( _
   ByVal DispVertex As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDisplacementConstraint
Dim DispVertex As System.Object
Dim value As System.Integer

value = instance.SetVertex(DispVertex)
```

### C#

```csharp
System.int SetVertex(
   System.object DispVertex
)
```

### C++/CLI

```cpp
System.int SetVertex(
   System.Object^ DispVertex
)
```

### Parameters

- `DispVertex`: Vertex

### Return Value

Result code as defined in [swsTopologyStudy_DisplacementConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_DisplacementConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyDisplacementConstraint::SetVertex](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyDisplacementConstraint~SetVertex.html).

## Remarks

This method is valid only if [ICWTopologyDisplacementConstraint::SetLocationPreference](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetLocationPreference.html) sets [swsTopologyStudyDisplacementConstraintLocationOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyDisplacementConstraintLocationOption_e.html).swsTopologyDisplacementConstraintLocationOption_UserDefine.

## See Also

[ICWTopologyDisplacementConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html)
[ICWTopologyDisplacementConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint_members.html)
[ICWTopologyDisplacementConstraint::RemoveVertex Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~RemoveVertex.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
