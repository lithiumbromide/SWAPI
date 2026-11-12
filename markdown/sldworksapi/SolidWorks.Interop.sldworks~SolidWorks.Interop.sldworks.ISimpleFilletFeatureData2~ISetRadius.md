---
title: "ISetRadius Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "ISetRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetRadius.html"
---

# ISetRadius Method (ISimpleFilletFeatureData2)

Sets the radius value for specified fillet item.

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
Dim instance As ISimpleFilletFeatureData2
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

- `PFilletItem`: Fillet item whose radius you want
- `Radius`: Radius value

## VBA Syntax

See [SimpleFilletFeatureData2::ISetRadius](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~ISetRadius.html).

## Remarks

To obtain a pointer to a fillet item, see [ISimpleFilletFeatureData2::GetFilletItemAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~GetFilletItemAtIndex.html) and [ISimpleFilletFeatureData2::FilletItemsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~FilletItemsCount.html). Fillets can be made from multiple edges or faces and these methods get a pointer to any of the entities that helped to create the particular fillet and pass it into the PFilletItem parameter of this method.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::GetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetRadius.html)
[ISimpleFilletFeatureData2::IGetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetRadius.html)
[ISimpleFilletFeatureData2::SetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetRadius.html)
[ISimpleFilletFeatureData2::DefaultRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~DefaultRadius.html)
[ISimpleFilletFeatureData2::IsMultipleRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IsMultipleRadius.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
