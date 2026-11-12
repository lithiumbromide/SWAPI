---
title: "ISlotMateFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "ISlotMateFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData.html"
---

# ISlotMateFeatureData Interface

Allows access to a slot mate feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISlotMateFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As ISlotMateFeatureData
```

### C#

```csharp
public interface ISlotMateFeatureData
```

### C++/CLI

```cpp
public interface class ISlotMateFeatureData
```

## VBA Syntax

See [SlotMateFeatureData](ms-its:sldworksapivb6.chm::/sldworks~SlotMateFeatureData.html).

## Examples

'VBA
' ******************************************************************************
' 1. Open `public_documents`**\samples\tutorial\api\MechanicalMates\slot_slot.sldasm**.
' 2. Run the macro.
' 3. Inspect the Mates folder of the FeatureManager design tree.
' ******************************************************************************
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim boolstatus As Boolean
Option Explicit

Sub main()

Set swApp = Application.SldWorks

Set Part = swApp.ActiveDoc
boolstatus = Part.Extension.SelectByRay(0.12649032355856, 0.133857958976421, 8.79467058769023E-03, 3.53905007657348E-02, 0.579257713320296, 0.814375843216443, 2.14371287556113E-03, 2, True, 1, 0)
boolstatus = Part.Extension.SelectByRay(9.59257342875013E-02, 9.99222046038994E-02, -2.51429018803719E-02, 3.53905007657348E-02, 0.579257713320296, 0.814375843216443, 2.14371287556113E-03, 2, True, 1, 0)

' Create SlotMateFeatureData
Dim MateData As SldWorks.SlotMateFeatureData
Set MateData = Part.**CreateMateData**(21)

' Set the entities to mate
Dim EntitiesToMate(1) As Object
Set EntitiesToMate(0) = Part.SelectionManager.GetSelectedObject6(1, -1)
Set EntitiesToMate(1) = Part.SelectionManager.GetSelectedObject6(2, -1)
Dim EntitiesToMateVar As Variant
EntitiesToMateVar = EntitiesToMate
MateData.**EntitiesToMate** = (EntitiesToMateVar)

' Set the mate alignment
MateData.**MateAlignment** = 0

' Set the mate constraint
MateData.**Constraint** = 0

' Create the mate
Dim MateFeature As SldWorks.Feature
Set MateFeature = Part.**CreateMate**(MateData)
Part.ClearSelection2 True
Part.EditRebuild3

End Sub

## Examples

[Create Slot Mate (C#)](Create_Slot_Mate_Example_CSharp.htm)

## Remarks

A slot mate is a mate between:

- A bolt and either a straight slot or an arced slot.
- Two slots, straight or arced

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html) is the parent of this mate interface.

To create a slot mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html) Remarks.
2. Specify [ISlotMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~EntitiesToMate.html) or use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities using Mark = 1.
3. Specify other properties of the SlotMateFeatureData object. as required.

To edit a slot mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a SlotMateFeatureData object.
3. Modify the SlotMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html).

To delete this slot mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.html).

## Access Diagram

[SlotMateFeatureData](SWObjectModel.pdf#SlotMateFeatureData)

## See Also

[ISlotMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
