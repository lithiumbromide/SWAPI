---
title: "ILocalCircularPatternFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "ILocalCircularPatternFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html"
---

# ILocalCircularPatternFeatureData Interface

Allows access to a circular component pattern feature in an assembly.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ILocalCircularPatternFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCircularPatternFeatureData
```

### C#

```csharp
public interface ILocalCircularPatternFeatureData
```

### C++/CLI

```cpp
public interface class ILocalCircularPatternFeatureData
```

## VBA Syntax

See [LocalCircularPatternFeatureData](ms-its:sldworksapivb6.chm::/sldworks~LocalCircularPatternFeatureData.html).

## Examples

'VBA

'-------------------------------------------------------
' Preconditions: Verify that the assembly exists.
'
' Postconditions:
' 1. Opens the assembly.
' 2. Selects an edge for the direction axis.
' 3. Selects a subassembly to pattern.
' 4. Creates **LocalCirPattern1**.
' 5. Examine the FeatureManager design tree and
' graphics area.
'
' NOTE: Because the assembly is used elsewhere, do not
' save changes.
'--------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatureManager As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim swLocalCirPattFD As SldWorks.LocalCircularPatternFeatureData
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
Sub main()

Set swApp = Application.SldWorks
fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\distance linkage.sldasm"
Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
Set swModelDocExt = swModel.Extension
Set swFeatureManager = swModel.FeatureManager
status = swModelDocExt.SelectByID2("", "EDGE", 0.22639417933982, -0.194822643434378, 0.102086175644843, False, 2, Nothing, 0)
status = swModelDocExt.SelectByID2("mount base-1@distance linkage", "COMPONENT", 0, 0, 0, True, 1, Nothing, 0)
Set swLocalCirPattFD = swFeatureManager.**CreateDefinition**(swFmLocalCirPattern)
swLocalCirPattFD.**TotalInstances** = 3
swLocalCirPattFD.**EqualSpacing** = True
Set swFeature = swFeatureManager.**CreateFeature**(swLocalCirPattFD)
swModel.ClearSelection2 True

End Sub

## Examples

[Get and Set Seed Components (C#)](Get_and_Set_Seed_Components_Example_CSharp.htm)
[Get and Set Seed Components (VB.NET)](Get_and_Set_Seed_Components_Example_VBNET.htm)
[Get and Set Seed Components (VBA)](Get_and_Set_Seed_Components_Example_VB.htm)
[Create Local Circular Pattern (C#)](Create_Local_Circular_Pattern_Example_CSharp.htm)

## Remarks

Read [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm).

Before calling IFeatureManager::CreateDefinition, you must pre-select the entities needed to create the local circular pattern feature.

| If... | To select a component, use... |
| --- | --- |
| Using IModelDocExtension::SelectByID2 to select components, ordered selection of the components is required | 1 to mark the components to pattern 2 to mark the axis |
| Directly selecting a component or axis | ISelectData::Mark and Component2::Select3 1 to mark the components to pattern 2 to mark the axis |

You must call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) after initializing this feature data object in order to successfully create the local circular pattern feature.

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html)

[IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html)

## Access Diagram

[LocalCircularPatternFeatureData](SWObjectModel.pdf#LocalCircularPatternFeatureData)

## See Also

[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
