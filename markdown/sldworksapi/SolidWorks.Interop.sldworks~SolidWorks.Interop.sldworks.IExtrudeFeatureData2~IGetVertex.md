---
title: "IGetVertex Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "IGetVertex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IGetVertex.html"
---

# IGetVertex Method (IExtrudeFeatureData2)

Obsolete. Superseded by [IExtrudeFeatureData2::GetEndConditionReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~GetEndConditionReference.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetVertex( _
   ByVal Forward As System.Boolean _
) As Vertex
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim Forward As System.Boolean
Dim value As Vertex

value = instance.IGetVertex(Forward)
```

### C#

```csharp
Vertex IGetVertex(
   System.bool Forward
)
```

### C++/CLI

```cpp
Vertex^ IGetVertex(
   System.bool Forward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`:

## VBA Syntax

See [ExtrudeFeatureData2::IGetVertex](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~IGetVertex.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
