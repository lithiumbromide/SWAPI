---
title: "CurvatureContinuous Property (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "CurvatureContinuous"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~CurvatureContinuous.html"
---

# CurvatureContinuous Property (IVariableFilletFeatureData2)

Gets or sets whether to create a smoother curvature between adjacent surfaces for this variable radius fillet feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurvatureContinuous As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim value As System.Boolean

instance.CurvatureContinuous = value

value = instance.CurvatureContinuous
```

### C#

```csharp
System.bool CurvatureContinuous {get; set;}
```

### C++/CLI

```cpp
property System.bool CurvatureContinuous {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to make curvatures continuous, false to not

## VBA Syntax

See [VariableFilletFeatureData2::CurvatureContinuous](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~CurvatureContinuous.html).

## Examples

[Create Curvature Continuous Variable Fillet Feature (C#)](Create_Curvature_Continuous_Variable_Fillet_Feature_Example_CSharp.htm)
[Create Curvature Continuous Variable Fillet Feature (VB.NET)](Create_Curvature_Continuous_Variable_Fillet_Feature_Example_VBNET.htm)
[Create Curvature Continuous Variable Fillet Feature (VBA)](Create_Curvature_Continuous_Variable_Fillet_Feature_Example_VB.htm)

## Remarks

This property supersedes any [IVariableFilletFeatureData2::ConicTypeForCrossSectionProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ConicTypeForCrossSectionProfile.html) setting. Curvature continuous fillets are smoother than standard fillets because there is no jump in curvature at the boundary.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
