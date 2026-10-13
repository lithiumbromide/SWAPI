---
title: "SetDistance Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "SetDistance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetDistance.html"
---

# SetDistance Method (ISimpleFilletFeatureData2)

Sets the Distance 2 radius at the specified item of this asymmetric fillet/chamfer.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDistance( _
   ByVal PFilletItem As System.Object, _
   ByVal Dist2 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim PFilletItem As System.Object
Dim Dist2 As System.Double

instance.SetDistance(PFilletItem, Dist2)
```

### C#

```csharp
void SetDistance(
   System.object PFilletItem,
   System.double Dist2
)
```

### C++/CLI

```cpp
void SetDistance(
   System.Object^ PFilletItem,
   System.double Dist2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFilletItem`: Item at which to set the Distance 2 radius
- `Dist2`: Distance 2 radius of the asymmetric fillet/chamfer at PFilletItem

## VBA Syntax

See [SimpleFilletFeatureData2::SetDistance](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~SetDistance.html).

## Remarks

Call [ISimpleFilletFeatureData2::SetRadius](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~SetRadius.html) to set the Distance 1 radius.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::GetDistance Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetDistance.html)
[ISimpleFilletFeatureData2::AsymmetricFillet Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~AsymmetricFillet.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
