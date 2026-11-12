---
title: "GetRadius Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "GetRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetRadius.html"
---

# GetRadius Method (ISimpleFilletFeatureData2)

Gets the radius at the specified fillet/chamfer item.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRadius( _
   ByVal PFilletItem As System.Object _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
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

- `PFilletItem`: Item at which to get the radius

### Return Value

Radius of the symmetric fillet at PFilletItem; Distance 1 radius of the asymmetric fillet/chamfer

## VBA Syntax

See [SimpleFilletFeatureData2::GetRadius](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~GetRadius.html).

## Remarks

Before calling this method, call [ISimpleFilletFeatureData2::GetFilletItemAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~GetFilletItemAtIndex.html) to get the pointer with which to specify PFilletItem.

Call [ISimpleFilletFeatureData2::GetDistance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~GetDistance.html) to get the Distance 2 radius of the asymmetric fillet/chamfer.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::IGetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetRadius.html)
[ISimpleFilletFeatureData2::ISetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetRadius.html)
[ISimpleFilletFeatureData2::SetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetRadius.html)
[ISimpleFilletFeatureData2::DefaultRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~DefaultRadius.html)
[ISimpleFilletFeatureData2::IsMultipleRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IsMultipleRadius.html)
[ISimpleFilletFeatureData2::AsymmetricFillet Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~AsymmetricFillet.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
