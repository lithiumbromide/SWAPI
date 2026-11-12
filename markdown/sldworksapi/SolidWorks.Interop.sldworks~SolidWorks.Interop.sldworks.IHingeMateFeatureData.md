---
title: "IHingeMateFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IHingeMateFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData.html"
---

# IHingeMateFeatureData Interface

Allows access to a hinge mate feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IHingeMateFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IHingeMateFeatureData
```

### C#

```csharp
public interface IHingeMateFeatureData
```

### C++/CLI

```cpp
public interface class IHingeMateFeatureData
```

## VBA Syntax

See [HingeMateFeatureData](ms-its:sldworksapivb6.chm::/sldworks~HingeMateFeatureData.html).

## Examples

'VBA
' ******************************************************************************
' 1. Open `public_documents`**\samples\tutorial\api\MechanicalMates\Hinge-Assy.sldasm**.
' 2. Run the macro.
' 3. Inspect the Mates folder in the FeatureManager design tree.
' ******************************************************************************
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim boolstatus As Boolean

Option Explicit
Sub main()

Set swApp = Application.SldWorks

Set Part = swApp.ActiveDoc

boolstatus = Part.Extension.SelectByRay(3.43240086878041E-02, 9.99999999998522E-02, -5.12270896450673E-03, -0.577381545199981, -0.577287712085548, -0.577381545199979, 7.97167289842004E-04, 2, True, 32768, 0)
boolstatus = Part.Extension.SelectByRay(8.24118572918451E-02, 0.10000000000008, -4.68924659023173E-02, -0.577381545199981, -0.577287712085548, -0.577381545199979, 7.97167289842004E-04, 2, True, 32768, 0)
boolstatus = Part.Extension.SelectByRay(1.82257333177063E-02, 4.19666144006783E-02, 0, -0.577381545199981, -0.577287712085548, -0.577381545199979, 7.97167289842004E-04, 2, True, 65536, 0)
boolstatus = Part.Extension.SelectByRay(7.79243258261317E-02, 4.97185607756023E-02, -3.84484600391488E-02, -0.577381545199981, -0.577287712085548, -0.577381545199979, 7.97167289842004E-04, 2, True, 65536, 0)
boolstatus = Part.Extension.SelectByRay(5.33819856866558E-02, 9.21914939762019E-02, -1.31731445623018E-03, -0.577381545199981, -0.577287712085548, -0.577381545199979, 7.97167289842004E-04, 2, True, 1, 0)
boolstatus = Part.Extension.SelectByRay(5.80246157638271E-02, 7.00560308736158E-02, -1.92219802344198E-02, -0.577381545199981, -0.577287712085548, -0.577381545199979, 7.97167289842004E-04, 2, True, 1, 0)

' Create HingeMateFeatureData
Dim MateData As SldWorks.HingeMateFeatureData
Set MateData = Part.**CreateMateData**(22)

' Set the concentric entities to mate
Dim ConcentricEntitiesToMate(1) As Object
Set ConcentricEntitiesToMate(0) = Part.SelectionManager.GetSelectedObject6(5, -1)
Set ConcentricEntitiesToMate(1) = Part.SelectionManager.GetSelectedObject6(6, -1)
Dim ConcentricEntitiesToMateVar As Variant
ConcentricEntitiesToMateVar = ConcentricEntitiesToMate
MateData.**EntitiesToMate**(0) = ConcentricEntitiesToMateVar

' Set the coincident entities to mate
Dim CoincidentEntitiesToMate(1) As Object
Set CoincidentEntitiesToMate(0) = Part.SelectionManager.GetSelectedObject6(1, -1)
Set CoincidentEntitiesToMate(1) = Part.SelectionManager.GetSelectedObject6(2, -1)
Dim CoincidentEntitiesToMateVar As Variant
CoincidentEntitiesToMateVar = CoincidentEntitiesToMate
MateData.**EntitiesToMate**(1) = CoincidentEntitiesToMateVar

' Set the mate angle selection
MateData.**AngleSelection** = True

' Set the angle entities to mate
Dim AngleEntitiesToMate(1) As Object
Set AngleEntitiesToMate(0) = Part.SelectionManager.GetSelectedObject6(3, -1)
Set AngleEntitiesToMate(1) = Part.SelectionManager.GetSelectedObject6(4, -1)
Dim AngleEntitiesToMateVar As Variant
AngleEntitiesToMateVar = AngleEntitiesToMate
MateData.**EntitiesToMate**(2) = AngleEntitiesToMateVar

' Set the mate angle value
MateData.**Angle** = 0.5235987755983

' Set the mate angle minimum value
MateData.**MinVal** = 0.5235987755983

' Set the mate angle maximum value
MateData.**MaxVal** = 0.5235987755983

' Set the mate alignment
MateData.**MateAlignment** = 0

' Create the mate
Dim MateFeature As SldWorks.Feature
Set MateFeature = Part.**CreateMate**(MateData)
Part.ClearSelection2 True
Part.EditRebuild3

End Sub

## Examples

[Create Hinge Mate (C#)](Create_Hinge_Mate_Example_CSharp.htm)

## Remarks

A hinge mate:

- Limits the movement between two components to one rotational degree of freedom.
- Can also limit the angular movement between two components.
- Acts like a concentric mate and a coincident mate.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html) is the parent of this mate interface.

To create a hinge mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html) Remarks.
2. Specify [IHingeMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~EntitiesToMate.html) for each EntityType or use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities using Mark = 1 for the concentric entities, Mark = 32768 for the coincident entities, and Mark = 65536 for the angle entities.
3. Specify other properties of the HingeMateFeatureData object as required.

To edit a hinge mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a HingeMateFeatureData object.
3. Modify the HingeMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html).

To delete a hinge mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.html).

## Access Diagram

[HingeMateFeatureData](SWObjectModel.pdf#HingeMateFeatureData)

## See Also

[IHingeMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
