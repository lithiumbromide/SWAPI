---
title: "GetVertex Method (IExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData"
member: "GetVertex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData~GetVertex.html"
---

# GetVertex Method (IExtrudeFeatureData)

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
Dim instance As IExtrudeFeatureData
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

See [ExtrudeFeatureData::GetVertex](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData~GetVertex.html).

## See Also

[IExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData.html)
[IExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData_members.html)
