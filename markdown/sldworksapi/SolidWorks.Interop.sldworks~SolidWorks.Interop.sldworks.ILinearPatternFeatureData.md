---
title: "ILinearPatternFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html"
---

# ILinearPatternFeatureData Interface

Allows access to a linear pattern feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ILinearPatternFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
```

### C#

```csharp
public interface ILinearPatternFeatureData
```

### C++/CLI

```cpp
public interface class ILinearPatternFeatureData
```

## VBA Syntax

See [LinearPatternFeatureData](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData.html).

## Examples

'VBA

'----------------------------------------------------
' Preconditions: Verify that the part exists.
'
' Postconditions:
' 1. Opens the part.
' 2. Selects the feature to pattern.
' 3. Selects the edges for Direction 1 and
' Direction 2 for the bidirectional linear
' pattern.
' 4. Creates a **LPattern1**.
' 5. Examine the FeatureManager design tree and
' graphics area.
'
' NOTE: Because the part is used elsewhere, do not save
' changes.
'------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatureManager As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim swLinearPatternFeatureData As SldWorks.LinearPatternFeatureData
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
Sub main()

Set swApp = Application.SldWorks
fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\box.sldprt"
Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
Set swModelDocExt = swModel.Extension
Set swFeatureManager = swModel.FeatureManager
'Select feature to pattern
status = swModelDocExt.SelectByID2("CBORE for #6 Binding Head Machine Screw1", "BODYFEATURE", 0, 0, 0, False, 4, Nothing, 0)

'Select edges for Direction 1 and Direction 2
status = swModelDocExt.SelectByID2("", "EDGE", -3.41223962029176E-02, 3.00321434688158E-02, 4.60303188361877E-02, True, 1, Nothing, 0)
status = swModelDocExt.SelectByID2("", "EDGE", 4.36465176948104E-02, 3.01916139486593E-02, 1.14344277122314E-02, True, 2, Nothing, 0)

'Create linear pattern
Set swLinearPatternFeatureData = swFeatureManager.**CreateDefinition**(swFmLPattern)
swLinearPatternFeatureData.**D1EndCondition** = 0
swLinearPatternFeatureData.**D1ReverseDirection** = False
swLinearPatternFeatureData.**D1Spacing** = 0.01
swLinearPatternFeatureData.**D1TotalInstances** = 4
swLinearPatternFeatureData.**D2EndCondition** = 0
swLinearPatternFeatureData.**D2PatternSeedOnly** = False
swLinearPatternFeatureData.**D2ReverseDirection** = False
swLinearPatternFeatureData.**D2Spacing** = 0.01
swLinearPatternFeatureData.**D2TotalInstances** = 4
swLinearPatternFeatureData.**GeometryPattern** = False
swLinearPatternFeatureData.**VarySketch** = False
Set swFeature = swFeatureManager.**CreateFeature**(swLinearPatternFeatureData)

End Sub

## Examples

[Get Linear Pattern Feature Data (C#)](Get_Linear_Pattern_Feature_Data_Example_CSharp.htm)
[Get Linear Pattern Feature Data (VB.NET)](Get_Linear_Pattern_Feature_Data_Example_VBNET.htm)
[Get Linear Pattern Feature Data (VBA)](Get_Linear_Pattern_Feature_Data_Example_VB.htm)
[Create Bidirectional Linear Pattern (C#)](Create_Bidir_Linear_Pattern_Example_CSharp.htm)

## Remarks

Read [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm).

Before calling [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html), you must pre-select the entities needed to create the linear pattern feature.

| If... | To select an entity, use... |
| --- | --- |
| Using IModelDocExtension::SelectByID2 to select entities to pattern | 1 to mark Direction 1 2 to mark Direction 2 4 to mark the faces or features to pattern 256 to mark the solid bodies to pattern 134217728 to mark the structure systems to pattern 2097152 to mark up-to references 8388608 to mark seed geometry references if not using centroids to measure offsets |
| Directly selecting an entity | IEntity::Select4 with ISelectData::Mark = 1 to mark Direction 1 2 to mark Direction 2 IFeature::Select2 with Mark= 4 to mark the faces or features to pattern 256 to mark the bodies to pattern 134217728 to mark the structure systems to pattern 2097152 to mark up-to references 8388608 to mark seed geometry references if not using centroids to measure offsets |

After calling IFeatureManager::CreateDefinition, you can initialize the feature data object using:

- [ILinearPatternFeatureData::D1Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1Axis.html) to specify Direction 1.
- [ILinearPatternFeatureData::BodyPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~BodyPattern.html) to specify the type of seed entities to pattern:

  - [ILinearPatternFeatureData::PatternBodyArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~PatternBodyArray.html), [PatternFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~PatternFaceArray.html), or [PatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~PatternFeatureArray.html)
- [ILinearPatternFeatureData::D1EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndCondition.html) to specify either spacing and instances or offsetting from an up-to reference:

**If explicitly setting spacing and instances, use:**

- [ILinearPatternFeatureData::D1Spacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1Spacing.html) to specify spacing between pattern instances

- [ILinearPatternFeatureData::D1TotalInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1TotalInstances.html) to specify the number of pattern instances.
- [ILinearPatternFeatureData::D1ReverseDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1ReverseDirection.html) to reverse Direction 1.

**If offsetting from an up-to reference, use:**

- - [ILinearPatternFeatureData::D1EndReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndReference.html) to specify the up-to reference.
  - [ILinearPatternFeatureData::D1EndRefOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndRefOffset.html) to specify the distance between the last pattern instance and the up-to reference.
  - [ILinearPatternFeatureData::D1EndRefReverseOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndRefReverseOffset.html) to reverse the offset.
  - [ILinearPatternFeatureData::D1EndUseSeedReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndUseSeedReference.html) to specify either to measure the offset from seed geometry or a centroid. If true:

    - Use [ILinearPatternFeatureData::D1EndSeedReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndSeedReference.html).
  - [ILinearPatternFeatureData::D1EndUseSpacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndUseSpacing.html) to specify either spacing or number of instances with the up-to reference:

    - Use ILinearPatternFeatureData::D1Spacing, if D1EndUseSpacing is true.
    - Use ILinearPatternFeatureData::D1TotalInstances, if D1EndUseSpacing is false.
- All of the ILinearPatternFeatureData::D2* properties to specify Direction 2 for a bidirectional linear pattern.
- Other properties such as [feature scope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~SetFeatureScope.html), [instances to skip](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~SkippedItemArray.html), [propagate visual properties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~PropagateVisualProperty.html), [geometry pattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GeometryPattern.html), and [vary sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~VarySketch.html).

You must call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) after initializing this feature data object in order to successfully create the linear pattern feature.

After creating the linear pattern feature, you can:

- [vary the spacing of pattern instances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~InstancesToVary.html) and dimensions by implementing [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html).

- [change the structure system to pattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~StructureSystemToPatternArray.html).

For more information, see the **Linear Patterns and the Linear Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html)

IFeatureManager::CreateDefinition

## Access Diagram

[LinearPatternFeatureData](SWObjectModel.pdf#LinearPatternFeatureData)

## See Also

[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
