---
title: "Add and Edit Misaligned Symmetric Concentric Mate Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_and_Edit_Misaligned_Symmetric_Concentric_Mate_Example_VB.htm"
---

# Add and Edit Misaligned Symmetric Concentric Mate Example (VBA)

This example shows how to add and edit a misaligned symmetric concentric mate between components.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Verify that the parts to open and assembly template exist.
' 2. Open a new session of SOLIDWORKS Design to ensure that the assembly
'    document's title is Assem1.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Opens wheel_hub.sldprt.
' 2. Opens a new assembly document titled Assem1 and adds
'    wheel_hub.sldprt as a component.
' 3. Opens and adds beam with holes.sldprt as another component.
' 4. Adds a concentric mate between the components.
' 5. Adds a misaligned symmetric concentric mate
'    between the components.
' 6. Edits the misaligned symmetric concentric mate.
' 7. Examine the Immediate window, graphics area, and the mates
'    in the Mates folder in the FeatureManager design tree.
'
' NOTE: Because the parts are used elsewhere, do not save changes.
'-----------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swAssembly As SldWorks.AssemblyDoc
Dim swInsertedComponent As SldWorks.Component2
Dim swMathUtil As SldWorks.MathUtility
Dim swTransform As SldWorks.MathTransform
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swMate As SldWorks.Mate2
Dim swLinkedMate As SldWorks.Mate2
Dim swComp As SldWorks.Component2
Dim swSelectionManager As SldWorks.SelectionMgr
Dim swFeature as SldWorks.Feature
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
Dim swSheetWidth As Double
Dim swSheetHeight As Double
Dim AssemblyTitle As String
Dim TransformData() As Double
Dim TransformDataVariant As Variant
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open the part
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\wheel_hub.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    swApp.ActivateDoc2 "wheel_hub.sldprt", False, errors
```

```
    'Create an assembly
    swSheetWidth = 0
    swSheetHeight = 0
    Set swAssembly = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2018\templates\Assembly.asmdot", 0, swSheetWidth, swSheetHeight)
    AssemblyTitle = swAssembly.GetTitle
```

```
    'Add the part to the assembly
    Set swInsertedComponent = swAssembly.AddComponent5(fileName, swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", False, "", -1.81145833835217E-04, 1.07469465717713E-04, 2.25750183631135E-05)
    swApp.CloseDoc fileName
    ReDim TransformData(0 To 15) As Double
    TransformData(0) = 1
    TransformData(1) = 0
    TransformData(2) = 0
    TransformData(3) = 0
    TransformData(4) = 1
    TransformData(5) = 0
    TransformData(6) = 0
    TransformData(7) = 0
    TransformData(8) = 1
    TransformData(9) = 0
    TransformData(10) = 0
    TransformData(11) = 0
    TransformData(12) = 1
    TransformData(13) = 0
    TransformData(14) = 0
    TransformData(15) = 0
    TransformDataVariant = TransformData
    Set swMathUtil = swApp.GetMathUtility()
    Set swTransform = swMathUtil.CreateTransform((TransformDataVariant))
    status = swInsertedComponent.SetTransformAndSolve2(swTransform)
```

```
    'Add another part to the assembly
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\beam with holes.sldprt"
    swApp.OpenDoc6 fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_AutoMissingConfig, "", errors, warnings
    Set swModel = swApp.ActivateDoc3(AssemblyTitle, True, 0, errors)
    Set swAssembly = swModel
    Set swInsertedComponent = swAssembly.AddComponent5(fileName, swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", False, "", -5.43800538871437E-02, -0.10948954091873, 9.44189997389913E-02)
    swApp.CloseDoc fileName
    ReDim TransformData(0 To 15) As Double
    TransformData(0) = 1
    TransformData(1) = 0
    TransformData(2) = 0
    TransformData(3) = 0
    TransformData(4) = 1
    TransformData(5) = 0
    TransformData(6) = 0
    TransformData(7) = 0
    TransformData(8) = 1
    TransformData(9) = -0.179380053887144
    TransformData(10) = -8.94895409187302E-02
    TransformData(11) = 7.44189997389913E-02
    TransformData(12) = 1
    TransformData(13) = 0
    TransformData(14) = 0
    TransformData(15) = 0
    TransformDataVariant = TransformData
    Set swMathUtil = swApp.GetMathUtility()
    Set swTransform = swMathUtil.CreateTransform((TransformDataVariant))
```

```
    'Add a concentric mate
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByRay(-0.158811046822791, -0.11180606883903, 0.110029416510201, -0.400036026779312, -0.515038074910024, -0.758094294050284, 8.77710636365774E-04, 2, True, 1, 0)
    status = swModelDocExt.SelectByRay(-5.95820179927387E-02, -2.82041473137156E-02, 1.20989536100637E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 8.77710636365774E-04, 2, True, 1, 0)
    Set swMate = swAssembly.AddMate5(swMateType_e.swMateCONCENTRIC, swMateAlign_e.swMateAlignALIGNED, False, 0.128546596088087, 0.0254, 0.0254, 0.0254, 0.0254, 0, 0.5235987755983, 0.5235987755983, False, False, 0, errors)
    swModel.ClearSelection2 True
    swModel.EditRebuild3
```

```
    'Move a component in order to add another mate
    status = swModelDocExt.SelectByID2("beam with holes-1@Assem1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    ReDim TransformData(0 To 15) As Double
    TransformData(0) = 0.999268594246539
    TransformData(1) = -3.82397247969312E-02
    TransformData(2) = 0
    TransformData(3) = 3.82397247969312E-02
    TransformData(4) = 0.999268594246539
    TransformData(5) = 0
    TransformData(6) = 0
    TransformData(7) = 0
    TransformData(8) = 1
    TransformData(9) = -8.17169203602251E-02
    TransformData(10) = -4.05863499514564E-03
    TransformData(11) = 0.158954897029145
    TransformData(12) = 1
    TransformData(13) = 0
    TransformData(14) = 0
    TransformData(15) = 0
    TransformDataVariant = TransformData
    Set swMathUtil = swApp.GetMathUtility()
    Set swTransform = swMathUtil.CreateTransform((TransformDataVariant))
    Set swSelectionManager = swModel.SelectionManager
    Set swComp = swSelectionManager.GetSelectedObjectsComponent4(1, -1)
    status = swComp.SetTransformAndSolve2(swTransform)

   'Add a misaligned symmetric concentric mate
    status = swModelDocExt.SelectByRay(-3.62917984178921E-02, -2.92363280984205E-02, 0.194521666713399, -0.400036026779312, -0.515038074910024, -0.758094294050284, 8.77710636365774E-04, 2, True, 1, 0)
    status = swModelDocExt.SelectByRay(0.054967212945769, -2.78611795938559E-02, 1.12380964281442E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 8.77710636365774E-04, 2, True, 1, 0)
    Debug.Print "Misaligned concentric mate:"
    Set swMate = swAssembly.AddConcentricMateWithTolerance(swMateAlign_e.swMateAlignALIGNED, swConcentricAlignmentType_e.swConcentricAlignSymmetric, False, 0, errors)
    If errors = 1 Then
        Debug.Print "  Added"
    Else
        Debug.Print "  Not added"
    End If

    swModel.ClearSelection2 True
```

```
    'Edit the misaligned symmetric concentric mate
    'and change its position from symmetric to aligned
    status = swModelDocExt.SelectByRay(5.48392523382404E-02, -0.0277425865184, 9.06375356890976E-03, -0.400036026779312, -0.515038074910024, -0.758094294050284, 1.07347349835279E-03, 2, False, 0, 0)
    status = swModelDocExt.SelectByRay(9.80255664001106E-03, -2.92099642897483E-02, 0.193646683964346, -0.400036026779312, -0.515038074910024, -0.758094294050284, 1.07347349835279E-03, 2, True, 0, 0)
    status = swModelDocExt.SelectByID2("Concentric2", "MATE", 0, 0, 0, True, 0, Nothing, 0)
    swAssembly.EditConcentricMate swMateAlign_e.swMateAlignALIGNED, swConcentricAlignmentType_e.swConcentricAlignThisMate, True, 0.095, errors

    swModel.ClearSelection2 True

    If errors = 1 Then
        Debug.Print "  Edited"
        status = swModelDocExt.SelectByID2("Concentric2", "MATE", 0, 0, 0, True, 0, Nothing, 0)
        Set swFeature = swSelectionManager.GetSelectedObject6(1, -1)
        Set swMate = swFeature.GetSpecificFeature2
```

```vb
        'Get the linked concentric mate
         Set swLinkedMate = swMate.GetLinkedMate
        'Get current misaligned deviation
         Debug.Print "    Current misalignment deviation: " & swLinkedMate.GetCurrentMisalignedDeviation
        'Do not use document property value for misalignment deviation
         swMate.SetUseMisalignedDeviationDocumentProperty False
         Debug.Print "    Use document property? " & swMate.GetUseMisalignedDeviationDocumentProperty
        'Change mate alignment type to symmetric
         swLinkedMate.SetConcentricAlignmentType (swConcentricAlignmentType_e.swConcentricAlignSymmetric)
         Debug.Print "    Concentric alignment type as defined in swConcentricAlignmentType_e: " & swLinkedMate.GetConcentricAlignmentType
        'Set maximum misalignment deviation
         swMate.SetMaximumMisalignedDeviation 0.102
         Debug.Print "    Maximum misalignment deviation: " & swMate.GetMaximumMisalignedDeviation
     Else
         Debug.Print "  Not edited"
     End If
```

```
    swModel.ClearSelection2 True
    swModel.EditRebuild3
```

```
End Sub
```
