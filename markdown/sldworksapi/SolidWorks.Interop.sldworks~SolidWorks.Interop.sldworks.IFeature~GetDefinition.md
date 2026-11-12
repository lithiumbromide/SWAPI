---
title: "GetDefinition Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetDefinition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html"
---

# GetDefinition Method (IFeature)

Gets the feature data object for a feature, such as an advanced mate, extrusion, loft, fillet, chamfer, etc., in order to access the parameters that control the definition of this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDefinition() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Object

value = instance.GetDefinition()
```

### C#

```csharp
System.object GetDefinition()
```

### C++/CLI

```cpp
System.Object^ GetDefinition();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Feature data object (see **Remarks**)

## VBA Syntax

See [Feature::GetDefinition](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetDefinition.html).

## Examples

[Change Bend Radius of Sheet Metal Part (VBA)](Change_Bend_Radius_of_Sheet_Metal_Part_Example_VB.htm)
[Create Thicken Feature (VBA)](Create_Thicken_Feature_Example_VB.htm)
[Get and Set Constraint for Dome Feature (VBA)](Get_and_Set_Constraint_for_Dome_Feature_Example_VB.htm)
[Insert Reference Points (VBA)](Insert_Reference_Points_Example_VB.htm)
[Set Custom Bend Allowance (VBA)](Set_Custom_Bend_Deduction_Example_VB.htm)
[Traverse All Cosmetic Threads (VBA)](Traverse_All_Cosmetic_Threads_Example_VB.htm)
[Insert and Change DeleteFace Feature (C#)](Insert_and_Change_DeleteFace_Feature_Example_CSharp.htm)
[Insert and Change DeleteFace Feature (VB.NET)](Insert_and_Change_DeleteFace_Feature_Example_VBNET.htm)
[Insert and Change DeleteFace Feature (VBA)](Insert_and_Change_DeleteFace_Feature_Example_VB.htm)

## Remarks

You can use this method to query the feature data object, and you can modify the feature data object using [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html). Set the feature data object to Nothing or null when it is no longer needed. Not all feature types are supported, so check to see that the returned object is valid.

To:

- get the type of feature and the name of its associated interface, use [IFeature::GetTypeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName.html) or [IFeature::GetTypeName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName2.html).
- see a complete list of interfaces for feature data objects (e.g., interfaces ending in FeatureData or FeatureData2, such as ISymmetricMateFeatureData, IExtrudeFeatureData2, ILoftFeatureData, ISimpleFilletFeatureData2, IChamferFeatureData2, etc.), see the **Features Interfaces** and **Assembly Interfaces - Mates** sections in [Functional Categories](FunctionalCategories-sldworksapi.html).
- get the object of a feature that is not a feature data object, use [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::IGetDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetDefinition.html)
[IFeature::IModifyDefinition2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.html)
