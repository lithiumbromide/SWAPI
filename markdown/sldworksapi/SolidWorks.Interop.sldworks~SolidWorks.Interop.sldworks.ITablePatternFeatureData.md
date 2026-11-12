---
title: "ITablePatternFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html"
---

# ITablePatternFeatureData Interface

Allows access to a table-driven pattern feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ITablePatternFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
```

### C#

```csharp
public interface ITablePatternFeatureData
```

### C++/CLI

```cpp
public interface class ITablePatternFeatureData
```

## VBA Syntax

See [TablePatternFeatureData](ms-its:sldworksapivb6.chm::/sldworks~TablePatternFeatureData.html).

## Examples

'VBA

' ******************************************************************************
' 1. Open `public_documents`**\samples\tutorial\api\tablepattern.sldprt**.
' 2. Delete **TPattern1**.
' 3. Run the macro.
' 4. Creates a new **TPattern1**.
' 5. Inspect the FeatureManager design tree and the graphics area.
' ******************************************************************************
Dim swApp As SldWorks.SldWorks
Dim swFeatData As TablePatternFeatureData
Dim Part As SldWorks.ModelDoc2
Dim swFeat As Feature
Dim swFeatMgr As FeatureManager
Dim boolstatus As Boolean

Option Explicit
Sub main()

Set swApp = Application.SldWorks
Set Part = swApp.ActiveDoc

boolstatus = Part.Extension.SelectByID2("Coordinate System1", "COORDSYS", 0, 0, 0, True, 16, Nothing, 0)
boolstatus = Part.Extension.SelectByID2("Cut-Extrude1", "BODYFEATURE", 0, 0, 0, True, 4, Nothing, 0)
Part.ActivateSelectedFeature
Dim swPointArray() As Double
ReDim swPointArray(0 To 5) As Double
swPointArray(0) = 0.04
swPointArray(1) = 0
swPointArray(2) = 0
swPointArray(3) = -0.025
swPointArray(4) = 0
swPointArray(5) = 0

Set swFeatMgr = Part.FeatureManager

Set swFeatData = swFeatMgr.**CreateDefinition**(swFmTablePattern)
swFeatData.**GeometryPattern** = False
swFeatData.**PointArray** = swPointArray
swFeatData.**PropagateVisualProperty** = True
swFeatData.**UseCentroid** = True
Set swFeat = swFeatMgr.**CreateFeature**(swFeatData)

End Sub

## Examples

[Get Points of Repeating Elements in Table-driven Pattern (C#)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_CSharp.htm)
[Get Points of Repeating Elements in Table-driven Pattern (VB.NET)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VBNET.htm)
[Get Points of Repeating Elements in Table-driven Pattern (VBA)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VB.htm)
[Create Table Pattern (C#)](Create_Table_Pattern_Example_CSharp.htm)

## Remarks

Read [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm).

Before calling IFeatureManager::CreateDefinition, you must pre-select the entities needed to create the table-driven pattern feature.

| To select ... | Use mark... |
| --- | --- |
| Seed feature | 4 |
| Coordinate system | 16 |
| Reference point | 32 |
| Seed face | 128 |
| Seed body | 256 |

You must call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) after initializing this feature data object in order to successfully create the table-driven pattern.

See the **Table Driven Patterns** topic in the SOLIDWORKS Design user-interface help for more information about table-driven patterns.

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html)

[IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html)

## Access Diagram

[TablePatternFeatureData](SWObjectModel.pdf#TablePatternFeatureData)

## See Also

[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
