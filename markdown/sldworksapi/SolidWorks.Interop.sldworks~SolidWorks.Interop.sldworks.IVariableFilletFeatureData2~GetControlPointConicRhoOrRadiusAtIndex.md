---
title: "GetControlPointConicRhoOrRadiusAtIndex Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "GetControlPointConicRhoOrRadiusAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointConicRhoOrRadiusAtIndex.html"
---

# GetControlPointConicRhoOrRadiusAtIndex Method (IVariableFilletFeatureData2)

Gets the conic rho or radius at the specified control point.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetControlPointConicRhoOrRadiusAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim Index As System.Integer
Dim value As System.Double

value = instance.GetControlPointConicRhoOrRadiusAtIndex(Index)
```

### C#

```csharp
System.double GetControlPointConicRhoOrRadiusAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double GetControlPointConicRhoOrRadiusAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Zero-based index of the control point (see **Remarks**)

### Return Value

Conic rho or radius

## VBA Syntax

See [VariableFilletFeatureData2::GetControlPointConicRhoOrRadiusAtIndex](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~GetControlPointConicRhoOrRadiusAtIndex.html).

## Remarks

Call [IVariableFilletFeatureData2::GetControlPointsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointsCount.html) before calling this method to determine a value for Index.

If [IVariableFilletFeatureData2::ConicTypeForCrossSectionProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ConicTypeForCrossSectionProfile.html) is set to [swFeatureFilletProfileType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletProfileType_e.html).:

- swFeatureFilletConicRadius (symmetric fillet only), then this method returns a radius.
- swFeatureFilletConicRho (symmetric or asymmetric fillet), then this method returns a conic rho value in the range [0.05, 0.95].

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::SetControlPointConicRhoOrRadiusAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointConicRhoOrRadiusAtIndex.html)
[IVariableFilletFeatureData2::GetControlPointRadiusAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointRadiusAtIndex.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
