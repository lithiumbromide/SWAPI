---
title: "IGearMateFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IGearMateFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData.html"
---

# IGearMateFeatureData Interface

Allows access to gear mate features.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IGearMateFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IGearMateFeatureData
```

### C#

```csharp
public interface IGearMateFeatureData
```

### C++/CLI

```cpp
public interface class IGearMateFeatureData
```

## VBA Syntax

See [GearMateFeatureData](ms-its:sldworksapivb6.chm::/sldworks~GearMateFeatureData.html).

## Examples

'VBA
' ******************************************************************************
' 1. Open `public_documents`**\samples\tutorial\api\MechanicalMates\spurgear.sldasm**.
' 2. Delete **GearMate1** from the Mates folder of the FeatureManager design tree.
' 3. Run the macro.
' 4. Inspect the Mates folder in the FeatureManager design tree.
' ******************************************************************************
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim boolstatus As Boolean

Option Explicit
Sub main()

Set swApp = Application.SldWorks

Set Part = swApp.ActiveDoc

boolstatus = Part.Extension.SelectByRay(-5.60801689982782E-03, -3.24062886681986E-03, -2.52602902980925E-03, -0.577381545199981, -0.577287712085548, -0.577381545199979, 5.93757005519753E-04, 2, True, 1, 0)
boolstatus = Part.Extension.SelectByRay(3.67362652137331E-02, -6.55599730123413E-04, -2.90761848191323E-03, -0.577381545199981, -0.577287712085548, -0.577381545199979, 5.93757005519753E-04, 2, True, 1, 0)

' Create GearMateFeatureData
Dim MateData As SldWorks.GearMateFeatureData
Set MateData = Part.**CreateMateData**(10)

' Set the entities To mate
Dim EntitiesToMate(1) As Object
Set EntitiesToMate(0) = Part.SelectionManager.GetSelectedObject6(1, -1)
Set EntitiesToMate(1) = Part.SelectionManager.GetSelectedObject6(2, -1)
Dim EntitiesToMateVar As Variant
EntitiesToMateVar = EntitiesToMate
MateData.**EntitiesToMate** = (EntitiesToMateVar)

' Set the gear ratio numerator
MateData.**GearRatioNumerator** = 0.012954

' Set the gear ratio denominator
MateData.**GearRatioDenominator** = 0.012954

' Set the mate orientation direction
MateData.**Reverse** = False

' Create the mate
Dim MateFeature As SldWorks.Feature
Set MateFeature = Part.**CreateMate**(MateData)
Part.ClearSelection2 True
Part.EditRebuild3

End Sub

## Examples

[Create Gear Mate (C#)](Create_Gear_Mate_Example_CSharp.htm)

## Remarks

SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html

A gear mate forces two components to rotate relative to one another about selected axes.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html) is the parent of this mate interface.

To create a gear mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html) Remarks.
2. Specify [IGearMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData~EntitiesToMate.html) or use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities using Mark = 1.
3. Specify other properties of the GearMateFeatureData object.

To edit a gear mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a GearMateFeatureData object.
3. Modify the GearMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html).

To delete a gear mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.html).

## Access Diagram

[GearMateFeatureData](SWObjectModel.pdf#GearMateFeatureData)

## See Also

[IGearMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
