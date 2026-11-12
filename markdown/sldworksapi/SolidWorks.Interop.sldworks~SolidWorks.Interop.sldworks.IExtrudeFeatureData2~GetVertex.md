---
title: "GetVertex Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "GetVertex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetVertex.html"
---

# GetVertex Method (IExtrudeFeatureData2)

Obsolete. Superseded by [IExtrudeFeatureData2::GetEndConditionReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~GetEndConditionReference.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVertex( _
   ByVal Forward As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim Forward As System.Boolean
Dim value As System.Object

value = instance.GetVertex(Forward)
```

### C#

```csharp
System.object GetVertex(
   System.bool Forward
)
```

### C++/CLI

```cpp
System.Object^ GetVertex(
   System.bool Forward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`:

## VBA Syntax

See [ExtrudeFeatureData2::GetVertex](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~GetVertex.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
