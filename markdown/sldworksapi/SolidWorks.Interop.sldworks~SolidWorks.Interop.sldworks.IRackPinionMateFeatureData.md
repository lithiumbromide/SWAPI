---
title: "IRackPinionMateFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IRackPinionMateFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData.html"
---

# IRackPinionMateFeatureData Interface

Allows access to a rack and pinion mate feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IRackPinionMateFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IRackPinionMateFeatureData
```

### C#

```csharp
public interface IRackPinionMateFeatureData
```

### C++/CLI

```cpp
public interface class IRackPinionMateFeatureData
```

## VBA Syntax

See [RackPinionMateFeatureData](ms-its:sldworksapivb6.chm::/sldworks~RackPinionMateFeatureData.html).

## Examples

'VBA
' ******************************************************************************
' 1. Open `public_documents`**\samples\tutorial\api\MechanicalMates\Rack And Pinion.sldasm**.
' 2. Delete **RackPinionMate1** from the Mates folder of the FeatureManager design tree.
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

boolstatus = Part.Extension.SelectByRay(-4.63518983485187E-02, 0.061012999696942, -6.42963015610576E-03, -0.398796540128449, 0.236369842894561, -0.886053393962, 7.98486578462134E-04, 1, True, 64, 0)
boolstatus = Part.Extension.SelectByRay(7.90589165686129E-03, -9.93915877270979E-03, -4.38167267822109E-03, -0.398796540128449, 0.236369842894561, -0.886053393962, 7.98486578462134E-04, 2, True, 128, 0)

' Create RackPinionMateFeatureData
Dim MateData As SldWorks.RackPinionMateFeatureData
Set MateData = Part.**CreateMateData**(13)

' Set the mate diameter type
MateData.**DiameterType** = 0

' Set the mate diameter value
MateData.**DiameterVal** = 0.0254

' Set the mate orientation direction
MateData.**Reverse** = False

' Create the mate
Dim MateFeature As SldWorks.Feature
Set MateFeature = Part.**CreateMate**(MateData)
Part.ClearSelection2 True
Part.EditRebuild3

End Sub

## Examples

[Create Rack and Pinion Mate (C#)](Rack_and_Pinion_Mate_Example_CSharp.htm)

## Remarks

A rack and pinion mate consists of two components where:

- One component (the rack) causes circular rotation in another component (the pinion) and vice versa.
- Neither component is required to have gear teeth.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html) is the parent of this mate interface.

To create a rack and pinion mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html) Remarks.
2. Use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities using Mark = 64 for the rack edge and Mark = 128 for the pinion face.
3. Specify other properties of the RackPinionMateFeatureData object as required.

To edit a rack and pinion mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a RackPinionMateFeatureData object.
3. Modify the RackPinionMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html).

To delete this rack and pinion mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.html).

## Access Diagram

[RackPinionMateFeatureData](SWObjectModel.pdf#RackPinionMateFeatureData)

## See Also

[IRackPinionMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
