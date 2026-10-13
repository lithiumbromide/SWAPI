---
title: "SetRadius Method (ISimpleFilletFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData"
member: "SetRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData~SetRadius.html"
---

# SetRadius Method (ISimpleFilletFeatureData)

Obsolete. Superseded by [ISimpleFilletFeatureData2::SetRadius](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~SetRadius.html).

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
Dim instance As ISimpleFilletFeatureData
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

See [SimpleFilletFeatureData::SetRadius](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData~SetRadius.html).

## See Also

[ISimpleFilletFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData.html)
[ISimpleFilletFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData_members.html)
