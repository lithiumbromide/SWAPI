---
title: "IGetRadius Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "IGetRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetRadius.html"
---

# IGetRadius Method (IVariableFilletFeatureData2)

Obsolete. Superseded by [IVariableFilletFeatureData2::Radius2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~GetRadius2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetRadius( _
   ByVal PFilletItem As Vertex _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
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

See [VariableFilletFeatureData2::IGetRadius](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~IGetRadius.html).

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
