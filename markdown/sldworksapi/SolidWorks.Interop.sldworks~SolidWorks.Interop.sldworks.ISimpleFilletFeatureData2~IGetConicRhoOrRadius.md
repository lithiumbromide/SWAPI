---
title: "IGetConicRhoOrRadius Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "IGetConicRhoOrRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetConicRhoOrRadius.html"
---

# IGetConicRhoOrRadius Method (ISimpleFilletFeatureData2)

Gets the conic rho, conic radius, or circular radius of this fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetConicRhoOrRadius( _
   ByVal PFilletItem As System.Object _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim PFilletItem As System.Object
Dim value As System.Double

value = instance.IGetConicRhoOrRadius(PFilletItem)
```

### C#

```csharp
System.double IGetConicRhoOrRadius(
   System.object PFilletItem
)
```

### C++/CLI

```cpp
System.double IGetConicRhoOrRadius(
   System.Object^ PFilletItem
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFilletItem`: Fillet item for which to get a value (see **Remarks**)

### Return Value

Conic rho, conic radius, or circular radius

## Remarks

Before calling this method, call [ISimpleFilletFeatureData2::IGetFilletItemAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~IGetFilletItemAtIndex.html) to get the pointer with which to specify PFilletItem.

The type of value returned by this method corresponds to the [ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~ConicTypeForCrossSectionProfile.html) setting.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::GetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetConicRhoOrRadius.html)
[ISimpleFilletFeatureData2::ISetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetConicRhoOrRadius.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
