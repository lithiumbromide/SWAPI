---
title: "IDerivedPatternFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IDerivedPatternFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.html"
---

# IDerivedPatternFeatureData Interface

Allows access to a derived pattern feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IDerivedPatternFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPatternFeatureData
```

### C#

```csharp
public interface IDerivedPatternFeatureData
```

### C++/CLI

```cpp
public interface class IDerivedPatternFeatureData
```

## VBA Syntax

See [DerivedPatternFeatureData](ms-its:sldworksapivb6.chm::/sldworks~DerivedPatternFeatureData.html).

## Examples

[Get and Set Seed Components (C#)](Get_and_Set_Seed_Components_Example_CSharp.htm)
[Get and Set Seed Components (VB.NET)](Get_and_Set_Seed_Components_Example_VBNET.htm)
[Get and Set Seed Components (VBA)](Get_and_Set_Seed_Components_Example_VB.htm)
[Get Number of Instances Skipped in Driving Feature (C#)](Get_Number_of_Instances_Skipped_in_Driving_Feature_Example_CSharp.htm)
[Get Number of Instances Skipped in Driving Feature (VB.NET)](Get_Number_of_Instances_Skipped_in_Driving_Feature_Example_VBNET.htm)
[Get Number of Instances Skipped in Driving Feature (VBA)](Get_Number_of_Instances_Skipped_in_Driving_Feature_Example_VB.htm)
[Create Derived Pattern Feature (C#)](Create_Derived_Pattern_Feature_Example_CSharp.htm)
[Create Derived Pattern Feature (VB.NET)](Create_Derived_Pattern_Feature_Example_VBNET.htm)
[Create Derived Pattern Feature (VBA)](Create_Derived_Pattern_Feature_Example_VB.htm)

## Remarks

Read [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm).

Before calling IFeatureManager::CreateDefinition, you must pre-select the entities needed to create the derived pattern feature. Use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select the seed components and pattern feature in any order using Marks:

- seed component = 1
- pattern feature = 2

You must call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) after initializing this feature data object in order to successfully create the derived pattern feature.

**NOTE**: A derived pattern feature is also called a pattern driven pattern feature.

For more information, see the **SOLIDWORKS Design user-interface help > Assemblies > Basic Component Operations > Component Patterns > Pattern Driven Component Pattern PropertyManager** topic.

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html)

[IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html)

## Access Diagram

[DerivedPatternFeatureData](SWObjectModel.pdf#DerivedPatternFeatureData)

## See Also

[IDerivedPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
