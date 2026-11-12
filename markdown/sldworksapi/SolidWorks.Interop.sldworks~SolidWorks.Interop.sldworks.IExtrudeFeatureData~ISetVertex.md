---
title: "ISetVertex Method (IExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData"
member: "ISetVertex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData~ISetVertex.html"
---

# ISetVertex Method (IExtrudeFeatureData)

Obsolete. Superseded by [IExtrudeFeatureData2::SetEndConditionReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~SetEndConditionReference.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetVertex( _
   ByVal Forward As System.Boolean, _
   ByVal Face As Vertex _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData
Dim Forward As System.Boolean
Dim Face As Vertex

instance.ISetVertex(Forward, Face)
```

### C#

```csharp
void ISetVertex(
   System.bool Forward,
   Vertex Face
)
```

### C++/CLI

```cpp
void ISetVertex(
   System.bool Forward,
   Vertex^ Face
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`:
- `Face`:

## VBA Syntax

See [ExtrudeFeatureData::ISetVertex](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData~ISetVertex.html).

## See Also

[IExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData.html)
[IExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData_members.html)
