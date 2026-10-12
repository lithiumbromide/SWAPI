---
title: "GetRadius Method (ISimpleFilletFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData"
member: "GetRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData~GetRadius.html"
---

# GetRadius Method (ISimpleFilletFeatureData)

Obsolete. Superseded by [ISimpleFilletFeatureData2::GetRadius](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~GetRadius.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRadius( _
   ByVal PFilletItem As System.Object _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData
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

See [SimpleFilletFeatureData::GetRadius](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData~GetRadius.html).

## See Also

[ISimpleFilletFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData.html)
[ISimpleFilletFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData_members.html)
