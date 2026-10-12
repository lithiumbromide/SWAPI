---
title: "ISetRadius Method (IVariableFilletFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData"
member: "ISetRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData~ISetRadius.html"
---

# ISetRadius Method (IVariableFilletFeatureData)

Obsolete. Superseded by [IVariableFilletFeatureData2::ISetRadius](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~ISetRadius.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetRadius( _
   ByVal PFilletItem As Vertex, _
   ByVal Radius As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData
Dim PFilletItem As Vertex
Dim Radius As System.Double

instance.ISetRadius(PFilletItem, Radius)
```

### C#

```csharp
void ISetRadius(
   Vertex PFilletItem,
   System.double Radius
)
```

### C++/CLI

```cpp
void ISetRadius(
   Vertex^ PFilletItem,
   System.double Radius
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFilletItem`:
- `Radius`:

## VBA Syntax

See [VariableFilletFeatureData::ISetRadius](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData~ISetRadius.html).

## See Also

[IVariableFilletFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData.html)
[IVariableFilletFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData_members.html)
