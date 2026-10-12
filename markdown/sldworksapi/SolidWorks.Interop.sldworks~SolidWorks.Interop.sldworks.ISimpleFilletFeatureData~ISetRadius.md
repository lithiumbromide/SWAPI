---
title: "ISetRadius Method (ISimpleFilletFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData"
member: "ISetRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData~ISetRadius.html"
---

# ISetRadius Method (ISimpleFilletFeatureData)

Obsolete. Superseded by [ISimpleFilletFeatureData2::ISetRadius](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~ISetRadius.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetRadius( _
   ByVal PFilletItem As System.Object, _
   ByVal Radius As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData
Dim PFilletItem As System.Object
Dim Radius As System.Double

instance.ISetRadius(PFilletItem, Radius)
```

### C#

```csharp
void ISetRadius(
   System.object PFilletItem,
   System.double Radius
)
```

### C++/CLI

```cpp
void ISetRadius(
   System.Object^ PFilletItem,
   System.double Radius
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFilletItem`:
- `Radius`:

## VBA Syntax

See [SimpleFilletFeatureData::ISetRadius](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData~ISetRadius.html).

## See Also

[ISimpleFilletFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData.html)
[ISimpleFilletFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData_members.html)
