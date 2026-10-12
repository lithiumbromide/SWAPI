---
title: "GetRadius Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "GetRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetRadius.html"
---

# GetRadius Method (IVariableFilletFeatureData2)

Obsolete. Superseded by [IVariableFilletFeatureData2::GetRadius2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~GetRadius2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRadius( _
   ByVal PFilletItem As System.Object _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim PFilletItem As System.Object
Dim value As System.Double

value = instance.GetRadius(PFilletItem)
```

### C#

```csharp
System.double GetRadius(
   System.object PFilletItem
)
```

### C++/CLI

```cpp
System.double GetRadius(
   System.Object^ PFilletItem
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFilletItem`:

## VBA Syntax

See [VariableFilletFeatureData2::GetRadius](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~GetRadius.html).

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
