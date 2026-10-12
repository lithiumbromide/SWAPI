---
title: "SetSetbackVertexDistance Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "SetSetbackVertexDistance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetSetbackVertexDistance.html"
---

# SetSetbackVertexDistance Method (IVariableFilletFeatureData2)

Sets the setback distances on fillet edges from the specified fillet corner vertex on this variable fillet feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSetbackVertexDistance( _
   ByVal Vtx As System.Object, _
   ByVal EdgeVar As System.Object, _
   ByVal DistVar As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim Vtx As System.Object
Dim EdgeVar As System.Object
Dim DistVar As System.Object
Dim value As System.Boolean

value = instance.SetSetbackVertexDistance(Vtx, EdgeVar, DistVar)
```

### C#

```csharp
System.bool SetSetbackVertexDistance(
   System.object Vtx,
   System.object EdgeVar,
   System.object DistVar
)
```

### C++/CLI

```cpp
System.bool SetSetbackVertexDistance(
   System.Object^ Vtx,
   System.Object^ EdgeVar,
   System.Object^ DistVar
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Vtx`: [Vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) for which to set the setback distance
- `EdgeVar`: Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) for this vertex
- `DistVar`: Array of distances

### Return Value

True if setback distances are set, false if not

## VBA Syntax

See [VariableFilletFeatureData2::SetSetbackVertexDistance](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~SetSetbackVertexDistance.html).

## Remarks

There is a one-to-one correspondence between the arrays specified by EdgeVar and DistVar.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::ISetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetSetbackVertexDistance.html)
[IVariableFilletFeatureData2::SetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetSetbackVertices.html)
[IVariableFilletFeatureData2::ISetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetSetbackVertices.html)
[IVariableFilletFeatureData2::GetSetbackDistanceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackDistanceCount.html)
[IVariableFilletFeatureData2::GetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVertexDistance.html)
[IVariableFilletFeatureData2::GetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVertices.html)
[IVariableFilletFeatureData2::GetSetbackVerticesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVerticesCount.html)
[IVariableFilletFeatureData2::IGetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetSetbackVertexDistance.html)
[IVariableFilletFeatureData2::IGetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetSetbackVertices.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
