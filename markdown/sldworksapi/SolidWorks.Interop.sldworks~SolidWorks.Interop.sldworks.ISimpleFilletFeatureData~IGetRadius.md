---
title: "IGetRadius Method (ISimpleFilletFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData"
member: "IGetRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData~IGetRadius.html"
---

# IGetRadius Method (ISimpleFilletFeatureData)

Obsolete. Superseded by [ISimpleFilletFeatureData2::IGetRadius](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~IGetRadius.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetRadius( _
   ByVal PFilletItem As System.Object _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData
Dim PFilletItem As System.Object
Dim value As System.Double

value = instance.IGetRadius(PFilletItem)
```

### C#

```csharp
System.double IGetRadius(
   System.object PFilletItem
)
```

### C++/CLI

```cpp
System.double IGetRadius(
   System.Object^ PFilletItem
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFilletItem`:

## VBA Syntax

See [SimpleFilletFeatureData::IGetRadius](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData~IGetRadius.html).

## See Also

[ISimpleFilletFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData.html)
[ISimpleFilletFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData_members.html)
