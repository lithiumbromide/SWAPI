---
title: "SetRadius Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "SetRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetRadius.html"
---

# SetRadius Method (ISimpleFilletFeatureData2)

Sets the radius at the specified fillet item.

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
Dim instance As ISimpleFilletFeatureData2
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

- `PFilletItem`: Fillet item at which to set the radius
- `Radius`: Radius of the symmetric fillet at PFilletItem; Distance 1 radius of the asymmetric fillet

## VBA Syntax

See [SimpleFilletFeatureData2::SetRadius](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~SetRadius.html).

## Remarks

Before calling this method, call [ISimpleFilletFeatureData2::GetFilletItemAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~GetFilletItemAtIndex.html) to get the pointer with which to specify PFilletItem.

Call [ISimpleFilletFeatureData2::SetDistance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~SetDistance.html) to set the Distance 2 radius at PFilletItem of the asymmetric fillet.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::GetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetRadius.html)
[ISimpleFilletFeatureData2::IGetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetRadius.html)
[ISimpleFilletFeatureData2::ISetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetRadius.html)
[ISimpleFilletFeatureData2::DefaultRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~DefaultRadius.html)
[ISimpleFilletFeatureData2::IsMultipleRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IsMultipleRadius.html)
[ISimpleFilletFeatureData2::AsymmetricFillet Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~AsymmetricFillet.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
