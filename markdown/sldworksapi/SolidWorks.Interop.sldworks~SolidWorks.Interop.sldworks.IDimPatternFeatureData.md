---
title: "IDimPatternFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IDimPatternFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html"
---

# IDimPatternFeatureData Interface

Allows access to a variable pattern feature, which uses a table to store the dimensions and values of the pattern instances.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IDimPatternFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IDimPatternFeatureData
```

### C#

```csharp
public interface IDimPatternFeatureData
```

### C++/CLI

```cpp
public interface class IDimPatternFeatureData
```

## VBA Syntax

See [DimPatternFeatureData](ms-its:sldworksapivb6.chm::/sldworks~DimPatternFeatureData.html).

## Examples

[Insert Variable Pattern Feature (C#)](Insert_Advanced_Variable_Pattern_Feature_Example_CSharp.htm)
[Insert Variable Pattern Feature (VB.NET)](Insert_Advanced_Variable_Pattern_Feature_Example_VBNET.htm)
[Insert Variable Pattern Feature (VBA)](Insert_Advanced_Variable_Pattern_Feature_Example_VB.htm)
[Delete Instances and Dimensions in Variable Pattern Feature (C#)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_CSharp.htm)
[Delete Instances and Dimensions in Variable Pattern Feature (VB.NET)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_VBNET.htm)
[Delete Instances and Dimensions in Variable Pattern Feature (VBA)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_VB.htm)
[Delete and Insert Instances in Variable Pattern Feature (C#)](Delete_and_Insert_Instances_in_Variable_Pattern_Feature_Example_CSharp.htm)
[Delete and Insert Instances in Variable Pattern Feature (VB.NET)](Delete_and_Insert_Instances_in_Variable_Pattern_Feature_Example_VBNET.htm)
[Delete and Insert Instances in Variable Pattern Feature (VBA)](Delete_and_Insert_Instances_in_Variable_Pattern_Feature_Example_VB.htm)

## Remarks

Read [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm).

The variable pattern feature uses a table to store the dimensions and values of pattern instances.

You can [import tables](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~ImportFromExcel.html) and [export tables](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~ExportToExcel.html) using this interface.

Before calling IFeatureManager::CreateDefinition, you must pre-select the entities needed to create the derived pattern feature. Use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select the reference geometry to drive the seed fature and the feature to pattern in any order using Marks:

- reference geometry to drive seed feature = 1048576
- feature to pattern = 4

You must call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) after initializing this feature data object in order to successfully create the derived pattern feature.

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html)

[IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html)

## Access Diagram

[DimPatternFeatureData](SWObjectModel.pdf#DimPatternFeatureData)

## See Also

[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::FeatureAdvancedTableDrivenPattern Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureAdvancedTableDrivenPattern.html)
