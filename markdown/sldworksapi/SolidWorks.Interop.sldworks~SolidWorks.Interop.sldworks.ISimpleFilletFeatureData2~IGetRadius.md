---
title: "IGetRadius Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "IGetRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetRadius.html"
---

# IGetRadius Method (ISimpleFilletFeatureData2)

Gets the radius value for specified fillet item.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetRadius( _
   ByVal PFilletItem As System.Object _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
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

- `PFilletItem`: Fillet item whose radius you want

### Return Value

Radius value

## VBA Syntax

See [SimpleFilletFeatureData2::IGetRadius](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~IGetRadius.html).

## Remarks

To obtain a pointer to a fillet item, see [ISimpleFilletFeatureData2::GetFilletItemAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~GetFilletItemAtIndex.html) and [ISimpleFilletFeatureData2::FilletItemsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~FilletItemsCount.html). Fillets can be made from multiple edges or faces and these methods get a pointer to any of the entities that helped to create the particular fillet and pass it into the PFilletItem parameter of this method.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::IGetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetRadius.html)
[ISimpleFilletFeatureData2::ISetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetRadius.html)
[ISimpleFilletFeatureData2::SetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetRadius.html)
[ISimpleFilletFeatureData2::DefaultRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~DefaultRadius.html)
[ISimpleFilletFeatureData2::IsMultipleRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IsMultipleRadius.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
