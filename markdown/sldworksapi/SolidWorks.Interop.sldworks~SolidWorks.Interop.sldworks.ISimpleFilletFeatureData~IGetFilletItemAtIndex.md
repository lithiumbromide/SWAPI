---
title: "IGetFilletItemAtIndex Method (ISimpleFilletFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData"
member: "IGetFilletItemAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData~IGetFilletItemAtIndex.html"
---

# IGetFilletItemAtIndex Method (ISimpleFilletFeatureData)

Obsolete. Superseded by [ISimpleFilletFeatureData2::IGetFilletAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~IGetFilletItemAtIndex.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFilletItemAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData
Dim Index As System.Integer
Dim value As System.Object

value = instance.IGetFilletItemAtIndex(Index)
```

### C#

```csharp
System.object IGetFilletItemAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ IGetFilletItemAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:

## VBA Syntax

See [SimpleFilletFeatureData::IGetFilletItemAtIndex](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData~IGetFilletItemAtIndex.html).

## See Also

[ISimpleFilletFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData.html)
[ISimpleFilletFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData_members.html)
