---
title: "IGetFilletEdgeAtIndex Method (IVariableFilletFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData"
member: "IGetFilletEdgeAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData~IGetFilletEdgeAtIndex.html"
---

# IGetFilletEdgeAtIndex Method (IVariableFilletFeatureData)

Obsolete. Superseded by [IVariableFilletFeatureData2::IGetFilletEdgeAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~IGetFilletEdgeAtIndex.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFilletEdgeAtIndex( _
   ByVal Index As System.Integer _
) As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData
Dim Index As System.Integer
Dim value As Edge

value = instance.IGetFilletEdgeAtIndex(Index)
```

### C#

```csharp
Edge IGetFilletEdgeAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
Edge^ IGetFilletEdgeAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:

## VBA Syntax

See [VariableFilletFeatureData::IGetFilletEdgeAtIndex](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData~IGetFilletEdgeAtIndex.html).

## See Also

[IVariableFilletFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData.html)
[IVariableFilletFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData_members.html)
