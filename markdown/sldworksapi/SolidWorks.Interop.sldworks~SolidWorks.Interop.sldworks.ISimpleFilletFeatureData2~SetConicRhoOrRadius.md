---
title: "SetConicRhoOrRadius Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "SetConicRhoOrRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetConicRhoOrRadius.html"
---

# SetConicRhoOrRadius Method (ISimpleFilletFeatureData2)

Sets the conic rho or radius of this fillet/chamfer.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetConicRhoOrRadius( _
   ByVal PFilletItem As System.Object, _
   ByVal ConicRhoVal As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim PFilletItem As System.Object
Dim ConicRhoVal As System.Double

instance.SetConicRhoOrRadius(PFilletItem, ConicRhoVal)
```

### C#

```csharp
void SetConicRhoOrRadius(
   System.object PFilletItem,
   System.double ConicRhoVal
)
```

### C++/CLI

```cpp
void SetConicRhoOrRadius(
   System.Object^ PFilletItem,
   System.double ConicRhoVal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFilletItem`: Fillet item for which to set ConicRhoVal (see **Remarks**)
- `ConicRhoVal`: Conic rho or radius (see **Remarks**)

## VBA Syntax

See [SimpleFilletFeatureData2::SetConicRhoOrRadius](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~SetConicRhoOrRadius.html).

## Remarks

Before calling this method, call [ISimpleFilletFeatureData2::GetFilletItemAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~GetFilletItemAtIndex.html) to get the pointer with which to specify PFilletItem.

The value specified in ConicRhoVal must match the [ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~ConicTypeForCrossSectionProfile.html) setting.

If setting the conic rho value, it must be in the range [0.05, 0.95].

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::ISetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetConicRhoOrRadius.html)
[ISimpleFilletFeatureData2::GetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetConicRhoOrRadius.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
