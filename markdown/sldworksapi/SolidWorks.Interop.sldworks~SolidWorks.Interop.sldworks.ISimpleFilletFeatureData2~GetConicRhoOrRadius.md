---
title: "GetConicRhoOrRadius Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "GetConicRhoOrRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetConicRhoOrRadius.html"
---

# GetConicRhoOrRadius Method (ISimpleFilletFeatureData2)

Gets the conic rho or radius of this fillet/chamfer.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConicRhoOrRadius( _
   ByVal PFilletItem As System.Object _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim PFilletItem As System.Object
Dim value As System.Double

value = instance.GetConicRhoOrRadius(PFilletItem)
```

### C#

```csharp
System.double GetConicRhoOrRadius(
   System.object PFilletItem
)
```

### C++/CLI

```cpp
System.double GetConicRhoOrRadius(
   System.Object^ PFilletItem
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFilletItem`: Item for which to get a value (see **Remarks**)

### Return Value

Conic rho or conic radius

## VBA Syntax

See [SimpleFilletFeatureData2::GetConicRhoOrRadius](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~GetConicRhoOrRadius.html).

## Remarks

Before calling this method, call [ISimpleFilletFeatureData2::GetFilletItemAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~GetFilletItemAtIndex.html) to get the pointer with which to specify PFilletItem.

The type of value returned by this method corresponds to the [ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~ConicTypeForCrossSectionProfile.html) setting.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::IGetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetConicRhoOrRadius.html)
[ISimpleFilletFeatureData2::SetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetConicRhoOrRadius.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
