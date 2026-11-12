---
title: "GetSetbackVerticesCount Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "GetSetbackVerticesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVerticesCount.html"
---

# GetSetbackVerticesCount Method (IVariableFilletFeatureData2)

Gets the number of setback vertices for this variable fillet feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSetbackVerticesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim value As System.Integer

value = instance.GetSetbackVerticesCount()
```

### C#

```csharp
System.int GetSetbackVerticesCount()
```

### C++/CLI

```cpp
System.int GetSetbackVerticesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of setback vertices

## VBA Syntax

See [VariableFilletFeatureData2::GetSetbackVerticesCount](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~GetSetbackVerticesCount.html).

## Remarks

Call this method before calling [IVariableFilletFeatureData2::IGetSetbackVertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~IGetSetbackVertices.html).

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::GetSetbackDistanceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackDistanceCount.html)
[IVariableFilletFeatureData2::GetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVertexDistance.html)
[IVariableFilletFeatureData2::GetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVertices.html)
[IVariableFilletFeatureData2::IGetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetSetbackVertexDistance.html)
[IVariableFilletFeatureData2::IGetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetSetbackVertices.html)
[IVariableFilletFeatureData2::ISetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetSetbackVertexDistance.html)
[IVariableFilletFeatureData2::ISetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetSetbackVertices.html)
[IVariableFilletFeatureData2::SetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetSetbackVertexDistance.html)
[IVariableFilletFeatureData2::IGetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetSetbackVertices.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
