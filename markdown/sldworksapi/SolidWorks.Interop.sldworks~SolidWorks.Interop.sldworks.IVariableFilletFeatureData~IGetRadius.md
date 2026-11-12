---
title: "IGetRadius Method (IVariableFilletFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData"
member: "IGetRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData~IGetRadius.html"
---

# IGetRadius Method (IVariableFilletFeatureData)

Obsolete. Superseded by [IVariableFilletFeatureData2::GetRadius2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~GetRadius2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetRadius( _
   ByVal PFilletItem As Vertex _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData
Dim PFilletItem As Vertex
Dim value As System.Double

value = instance.IGetRadius(PFilletItem)
```

### C#

```csharp
System.double IGetRadius(
   Vertex PFilletItem
)
```

### C++/CLI

```cpp
System.double IGetRadius(
   Vertex^ PFilletItem
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFilletItem`:

## VBA Syntax

See [VariableFilletFeatureData::IGetRadius](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData~IGetRadius.html).

## See Also

[IVariableFilletFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData.html)
[IVariableFilletFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData_members.html)
