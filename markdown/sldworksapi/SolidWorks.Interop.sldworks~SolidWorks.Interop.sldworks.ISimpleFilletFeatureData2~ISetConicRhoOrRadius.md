---
title: "ISetConicRhoOrRadius Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "ISetConicRhoOrRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetConicRhoOrRadius.html"
---

# ISetConicRhoOrRadius Method (ISimpleFilletFeatureData2)

Sets the conic rho, conic radius, or circular radius of this fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetConicRhoOrRadius( _
   ByVal PFilletItem As System.Object, _
   ByVal ConicRhoVal As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim PFilletItem As System.Object
Dim ConicRhoVal As System.Double

instance.ISetConicRhoOrRadius(PFilletItem, ConicRhoVal)
```

### C#

```csharp
void ISetConicRhoOrRadius(
   System.object PFilletItem,
   System.double ConicRhoVal
)
```

### C++/CLI

```cpp
void ISetConicRhoOrRadius(
   System.Object^ PFilletItem,
   System.double ConicRhoVal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFilletItem`: Fillet item for which to set ConicRhoVal (see **Remarks**)
- `ConicRhoVal`: Conic rho, conic radius, or circular radius (see **Remarks**)

## Remarks

Before calling this method, call [ISimpleFilletFeatureData2::IGetFilletItemAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~IGetFilletItemAtIndex.html) to get the pointer with which to specify PFilletItem.

The value specified in ConicRhoVal must match the [ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~ConicTypeForCrossSectionProfile.html) setting.

If setting the conic rho value, it must be in the range [0.05, 0.95].

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::SetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetConicRhoOrRadius.html)
[ISimpleFilletFeatureData2::IGetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetConicRhoOrRadius.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
