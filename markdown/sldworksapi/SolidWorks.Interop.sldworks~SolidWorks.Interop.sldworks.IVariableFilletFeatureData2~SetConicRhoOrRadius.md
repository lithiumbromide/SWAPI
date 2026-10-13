---
title: "SetConicRhoOrRadius Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "SetConicRhoOrRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetConicRhoOrRadius.html"
---

# SetConicRhoOrRadius Method (IVariableFilletFeatureData2)

Sets the conic rho or radius for the specified fillet item.

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
Dim instance As IVariableFilletFeatureData2
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

See [VariableFilletFeatureData2::SetConicRhoOrRadius](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~SetConicRhoOrRadius.html).

## Remarks

Before calling this method, call [IVariableFilletFeatureData2::GetFilletEdgeAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~GetFilletEdgeAtIndex.html) to specify PFilletItem.

If [IVariableFilletFeatureData2::ConicTypeForCrossSectionProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ConicTypeForCrossSectionProfile.html) is set to [swFeatureFilletProfileType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletProfileType_e.html).:

- swFeatureFilletConicRadius (symmetric fillet only), then specify ConicRhoVal with a radius.
- swFeatureFilletConicRho (symmetric or asymmetric fillet), then specify ConicRhoVal with the conic rho value in the range [0.05, 0.95].

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::GetConicRhoOrRadius2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetConicRhoOrRadius2.html)
[IVariableFilletFeatureData2::ISetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetConicRhoOrRadius.html)
[IVariableFilletFeatureData2::SetRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetRadius.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
