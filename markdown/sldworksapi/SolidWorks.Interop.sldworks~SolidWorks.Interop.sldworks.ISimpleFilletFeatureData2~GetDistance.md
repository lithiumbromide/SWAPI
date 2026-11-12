---
title: "GetDistance Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "GetDistance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetDistance.html"
---

# GetDistance Method (ISimpleFilletFeatureData2)

Gets the Distance 2 radius at the specified item of this asymmetric fillet/chamfer.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDistance( _
   ByVal PFilletItem As System.Object _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim PFilletItem As System.Object
Dim value As System.Double

value = instance.GetDistance(PFilletItem)
```

### C#

```csharp
System.double GetDistance(
   System.object PFilletItem
)
```

### C++/CLI

```cpp
System.double GetDistance(
   System.Object^ PFilletItem
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFilletItem`: Item at which to get the Distance 2radius

### Return Value

Distance 2 radius at PFilletItem for this asymmetric fillet/chamfer

## VBA Syntax

See [SimpleFilletFeatureData2::GetDistance](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~GetDistance.html).

## Remarks

Call [ISimpleFilletFeatureData2::GetRadius](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~GetRadius.html) to get the Distance 1 radius at PFilletItem for this asymmetric fillet/chamfer.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::SetDistance Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetDistance.html)
[ISimpleFilletFeatureData2::AsymmetricFillet Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~AsymmetricFillet.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
