---
title: "SetControlPointConicRhoOrRadiusAtIndex Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "SetControlPointConicRhoOrRadiusAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointConicRhoOrRadiusAtIndex.html"
---

# SetControlPointConicRhoOrRadiusAtIndex Method (IVariableFilletFeatureData2)

Sets the conic rho or radius at the specified control point.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetControlPointConicRhoOrRadiusAtIndex( _
   ByVal Index As System.Integer, _
   ByVal ConicRhoVal As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim Index As System.Integer
Dim ConicRhoVal As System.Double

instance.SetControlPointConicRhoOrRadiusAtIndex(Index, ConicRhoVal)
```

### C#

```csharp
void SetControlPointConicRhoOrRadiusAtIndex(
   System.int Index,
   System.double ConicRhoVal
)
```

### C++/CLI

```cpp
void SetControlPointConicRhoOrRadiusAtIndex(
   System.int Index,
   System.double ConicRhoVal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Zero-based index of the control point for which to set ConicRhoVal (see **Remarks**)
- `ConicRhoVal`: Conic rho or radius (see **Remarks**)

## VBA Syntax

See [VariableFilletFeatureData2::SetControlPointConicRhoOrRadiusAtIndex](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~SetControlPointConicRhoOrRadiusAtIndex.html).

## Remarks

Call [IVariableFilletFeatureData2::GetControlPointsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointsCount.html) before calling this method to determine a value for Index.

If [IVariableFilletFeatureData2::ConicTypeForCrossSectionProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ConicTypeForCrossSectionProfile.html) is set to [swFeatureFilletProfileType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletProfileType_e.html).:

- swFeatureFilletConicRadius (symmetric fillet only), then specify ConicRhoVal with a radius.
- swFeatureFilletConicRho (symmetric or asymmetric fillet), then specify ConicRhoVal with the conic rho value in the range [0.05, 0.95].

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::GetControlPointConicRhoOrRadiusAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointConicRhoOrRadiusAtIndex.html)
[IVariableFilletFeatureData2::SetControlPointRadiusAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointRadiusAtIndex.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
