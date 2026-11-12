---
title: "SetRadius Method (IVariableFilletFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData"
member: "SetRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData~SetRadius.html"
---

# SetRadius Method (IVariableFilletFeatureData)

Obsolete. Superseded by [IVariableFilletFeatureData2::SetRadius](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~SetRadius.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetRadius( _
   ByVal PFilletItem As System.Object, _
   ByVal Radius As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData
Dim PFilletItem As System.Object
Dim Radius As System.Double

instance.SetRadius(PFilletItem, Radius)
```

### C#

```csharp
void SetRadius(
   System.object PFilletItem,
   System.double Radius
)
```

### C++/CLI

```cpp
void SetRadius(
   System.Object^ PFilletItem,
   System.double Radius
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFilletItem`:
- `Radius`:

## VBA Syntax

See [VariableFilletFeatureData::SetRadius](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData~SetRadius.html).

## See Also

[IVariableFilletFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData.html)
[IVariableFilletFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData_members.html)
