---
title: "IFeatureFillet2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "IFeatureFillet2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IFeatureFillet2.html"
---

# IFeatureFillet2 Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::FeatureFillet3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureFillet3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IFeatureFillet2( _
   ByVal Options As System.Integer, _
   ByVal R1 As System.Double, _
   ByVal Rho As System.Double, _
   ByVal Ftyp As System.Integer, _
   ByVal OverflowType As System.Integer, _
   ByVal ConicRhoType As System.Integer, _
   ByVal NRadii As System.Integer, _
   ByRef Radii As System.Double, _
   ByRef RhoArr As System.Double, _
   ByVal SetbackDistCount As System.Integer, _
   ByRef SetBackDistances As System.Double, _
   ByVal PointCount As System.Integer, _
   ByRef PointRadiusArray As System.Double, _
   ByRef PointRhoArray As System.Double _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Options As System.Integer
Dim R1 As System.Double
Dim Rho As System.Double
Dim Ftyp As System.Integer
Dim OverflowType As System.Integer
Dim ConicRhoType As System.Integer
Dim NRadii As System.Integer
Dim Radii As System.Double
Dim RhoArr As System.Double
Dim SetbackDistCount As System.Integer
Dim SetBackDistances As System.Double
Dim PointCount As System.Integer
Dim PointRadiusArray As System.Double
Dim PointRhoArray As System.Double
Dim value As Feature

value = instance.IFeatureFillet2(Options, R1, Rho, Ftyp, OverflowType, ConicRhoType, NRadii, Radii, RhoArr, SetbackDistCount, SetBackDistances, PointCount, PointRadiusArray, PointRhoArray)
```

### C#

```csharp
Feature IFeatureFillet2(
   System.int Options,
   System.double R1,
   System.double Rho,
   System.int Ftyp,
   System.int OverflowType,
   System.int ConicRhoType,
   System.int NRadii,
   ref System.double Radii,
   ref System.double RhoArr,
   System.int SetbackDistCount,
   ref System.double SetBackDistances,
   System.int PointCount,
   ref System.double PointRadiusArray,
   ref System.double PointRhoArray
)
```

### C++/CLI

```cpp
Feature^ IFeatureFillet2(
   System.int Options,
   System.double R1,
   System.double Rho,
   System.int Ftyp,
   System.int OverflowType,
   System.int ConicRhoType,
   System.int NRadii,
   System.double% Radii,
   System.double% RhoArr,
   System.int SetbackDistCount,
   System.double% SetBackDistances,
   System.int PointCount,
   System.double% PointRadiusArray,
   System.double% PointRhoArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Options`: Feature fillet options as defined in [swFeatureFilletOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html)
- `R1`: Unifiorm radius of the fillet; valid only if:

  - Ftyp != [swFeatureFilletType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html).swFeatureFilletType_VariableRadius
  - Options include [swFeatureFilletOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html).swFeatureFilletUniformRadius
- `Rho`: Value that determines the conic shape of the fillet:

  - Conic rho value, if ConicRhoType = [swFeatureFilletProfileType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletProfileType_e.html).swFeatureFilletConicRho
  - Conic radius value, if ConicRhoType = swFeatureFilletProfileType_e.swFeatureFilletConicRadius
  - Circular radius value, if ConicRhoType = swFeatureFilletProfileType_e.swFeatureFilletCircular
- `Ftyp`: Type of fillet as defined in [swFeatureFilletType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html) (see **Remarks**)
- `OverflowType`: Control of fillet overflowing onto adjacent surfaces as defined in [swFilletOverFlowType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFilletOverFlowType_e.html)
- `ConicRhoType`: Conic fillet profile type as defined in [swFeatureFilletProfileType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletProfileType_e.html)
- `NRadii`: Number of elements in the Radii array
- `Radii`: - In-process, unmanaged C++: Pointer to an array containing the radii for the variable radius fillet; valid only if:

    - Ftyp = [swFeatureFilletType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html).swFeatureFilletType_VariableRadius
    - Options include [swFeatureFilletOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html).swFeatureFilletVarRadiusType

    - Options do not include [swFeatureFilletOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html).swFeatureFilletUniformRadius
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `RhoArr`: - In-process, unmanaged C++: Pointer to an array of conic shape values for the specified ConicRhoType for the variable radius fillet; valid only if:

    - Ftyp = [swFeatureFilletType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html).swFeatureFilletType_VariableRadius
    - Options include [swFeatureFilletOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html).swFeatureFilletVarRadiusType
    - Options do not include [swFeatureFilletOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html).swFeatureFilletUniformRadius
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `SetbackDistCount`: Number of elements in the SetBackDistances array
- `SetBackDistances`: - In-process, unmanaged C++: Pointer to an array containing setback distances along the fillet edge
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `PointCount`: Number of elements in the PointRadiusArray and PointRhoArray arrays
- `PointRadiusArray`: - In-process, unmanaged C++: Pointer to an array containing radii at various control points along the length of the edge; valid only if Ftyp = [swFeatureFilletType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html).swFeatureFilletType_VariableRadius
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `PointRhoArray`: - In-process, unmanaged C++: Pointer to an array containing conic shape values for the specified ConicRhoType at various control points along the length of the edge; valid only if Ftyp = [swFeatureFilletType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html).swFeatureFilletType_VariableRadius
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) pointer

## Remarks

See the [IFeatureManager::FeatureFillet2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureFillet2.html) Remarks.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::FeatureFillet2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureFillet2.html)
[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IFeatureManager::FilletXpertChange Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertChange.html)
[IFeatureManager::FilletXpertMakeCorner Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertMakeCorner.html)
[IFeatureManager::FilletXpertRemove Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertRemove.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
