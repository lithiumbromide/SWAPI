---
title: "IVariableFilletFeatureData2 Interface"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html"
---

# IVariableFilletFeatureData2 Interface

Allows access to a variable radius fillet feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IVariableFilletFeatureData2
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
```

### C#

```csharp
public interface IVariableFilletFeatureData2
```

### C++/CLI

```cpp
public interface class IVariableFilletFeatureData2
```

## VBA Syntax

See [VariableFilletFeatureData2](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2.html).

## Examples

[Create Variable Radius Asymmetric Elliptical Fillet (VBA)](Create_Asymmetric_Elliptic_Fillets_Example_VB.htm)
[Create Variable Radius Asymmetric Elliptical Fillet (VB.NET)](Create_Asymmetric_Elliptic_Fillets_Example_VBNET.htm)
[Create Variable Radius Asymmetric Elliptical Fillet (C#)](Create_Asymmetric_Elliptic_Fillets_Example_CSharp.htm)
[Create Curvature Continuous Variable Fillet Feature (C#)](Create_Curvature_Continuous_Variable_Fillet_Feature_Example_CSharp.htm)
[Create Curvature Continuous Variable Fillet Feature (VB.NET)](Create_Curvature_Continuous_Variable_Fillet_Feature_Example_VBNET.htm)
[Create Curvature Continuous Variable Fillet Feature (VBA)](Create_Curvature_Continuous_Variable_Fillet_Feature_Example_VB.htm)

## Remarks

To create a variable fillet feature, follow the instructions in the Remarks section of [IFeatureManager::FeatureFillet3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureFillet3.html).

To edit a variable fillet feature:

1. Call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html).
2. Call [IVariableFilletFeatureData2::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~AccessSelections.html).
3. Modify properties on this interface as needed and call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html).
4. If nothing is modified, call [IVariableFilletFeatureData2::ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ReleaseSelectionAccess.html).

For more information, read the **Variable Size Fillets** topic in the SOLIDWORKS Design user-interface help.

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html)

## Access Diagram

[VariableFilletFeatureData2](SWObjectModel.pdf#VariableFilletFeatureData2)

## See Also

[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
