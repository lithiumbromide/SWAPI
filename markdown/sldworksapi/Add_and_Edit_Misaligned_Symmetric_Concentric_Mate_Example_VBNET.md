---
title: "Add and Edit Misaligned Symmetric Concentric Mate Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_and_Edit_Misaligned_Symmetric_Concentric_Mate_Example_VBNET.htm"
---

# Add and Edit Misaligned Symmetric Concentric Mate Example (VB.NET)

This example shows how to add and edit a misaligned symmetric concentric mate between components.

```vb
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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Public Sub main()

         Dim swModel As ModelDoc2
         Dim swAssembly As AssemblyDoc
         Dim swInsertedComponent As Component2
         Dim swMathUtil As MathUtility
         Dim swTransform As MathTransform
         Dim swModelDocExt As ModelDocExtension
         Dim swMate As Mate2
 Dim swLinkedMate As Mate2
         Dim swComp As Component2
         Dim swSelectionManager As SelectionMgr
         Dim swFeature As Feature
         Dim status As Boolean
         Dim errors As Integer
         Dim warnings As Integer
         Dim fileName As String
         Dim swSheetWidth As Double
         Dim swSheetHeight As Double
         Dim AssemblyTitle As String
         Dim TransformData(15) As Double
         Dim TransformDataObj As Object

         'Open the part
         fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\wheel_hub.sldprt"
         swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
         swApp.ActivateDoc2("wheel_hub.sldprt", False, errors)

         'Create an assembly
         swSheetWidth = 0
         swSheetHeight = 0
         swAssembly = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2018\templates\Assembly.asmdot", 0, swSheetWidth, swSheetHeight)
         AssemblyTitle = swAssembly.GetTitle

         'Add the part to the assembly
         swInsertedComponent = swAssembly.AddComponent5(fileName, swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", False, "", -0.000181145833835217, 0.000107469465717713, 0.0000225750183631135)
         swApp.CloseDoc(fileName)
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
         TransformDataObj = TransformData
         swMathUtil = swApp.GetMathUtility()
         swTransform = swMathUtil.CreateTransform((TransformDataObj))
         status = swInsertedComponent.SetTransformAndSolve2(swTransform)

         'Open and add another part to the assembly
         fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\beam with holes.sldprt"
         swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_AutoMissingConfig, "", errors, warnings)
         swModel = swApp.ActivateDoc3(AssemblyTitle, True, 0, errors)
         swAssembly = swModel
         swInsertedComponent = swAssembly.AddComponent5(fileName, swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", False, "", -0.0543800538871437, -0.10948954091873, 0.0944189997389913)
         swApp.CloseDoc(fileName)
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
         TransformData(10) = -0.0894895409187302
         TransformData(11) = 0.0744189997389913
         TransformData(12) = 1
         TransformData(13) = 0
         TransformData(14) = 0
         TransformData(15) = 0
         TransformDataObj = TransformData
         swMathUtil = swApp.GetMathUtility()
         swTransform = swMathUtil.CreateTransform((TransformDataObj))

         'Add a concentric mate
         swModelDocExt = swModel.Extension
         status = swModelDocExt.SelectByRay(-0.158811046822791, -0.11180606883903, 0.110029416510201, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000877710636365774, 2, True, 1, 0)
         status = swModelDocExt.SelectByRay(-0.0595820179927387, -0.0282041473137156, 0.0120989536100637, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000877710636365774, 2, True, 1, 0)
         swMate = swAssembly.AddMate5(swMateType_e.swMateCONCENTRIC, swMateAlign_e.swMateAlignALIGNED, False, 0.128546596088087, 0.0254, 0.0254, 0.0254, 0.0254, 0, 0.5235987755983, 0.5235987755983, False, False, 0, errors)
         swModel.ClearSelection2(True)
         swModel.EditRebuild3()

         'Move a component in order to add another mate
         status = swModelDocExt.SelectByID2("beam with holes-1@Assem1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
         TransformData(0) = 0.999268594246539
         TransformData(1) = -0.0382397247969312
         TransformData(2) = 0
         TransformData(3) = 0.0382397247969312
         TransformData(4) = 0.999268594246539
         TransformData(5) = 0
         TransformData(6) = 0
         TransformData(7) = 0
         TransformData(8) = 1
         TransformData(9) = -0.0817169203602251
         TransformData(10) = -0.00405863499514564
         TransformData(11) = 0.158954897029145
         TransformData(12) = 1
         TransformData(13) = 0
         TransformData(14) = 0
         TransformData(15) = 0
         TransformDataObj = TransformData
         swMathUtil = swApp.GetMathUtility()
         swTransform = swMathUtil.CreateTransform((TransformDataObj))
         swSelectionManager = swModel.SelectionManager
         swComp = swSelectionManager.GetSelectedObjectsComponent4(1, -1)
         status = swComp.SetTransformAndSolve2(swTransform)

         'Add a misaligned symmetric concentric mate
         status = swModelDocExt.SelectByRay(-0.0362917984178921, -0.0292363280984205, 0.194521666713399, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000877710636365774, 2, True, 1, 0)
         status = swModelDocExt.SelectByRay(0.054967212945769, -0.0278611795938559, 0.0112380964281442, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000877710636365774, 2, True, 1, 0)
          Debug.Print("Misaligned concentric mate:")
         swMate = swAssembly.AddConcentricMateWithTolerance(swMateAlign_e.swMateAlignALIGNED, swConcentricAlignmentType_e.swConcentricAlignSymmetric, False, 0, errors)
         If errors = 1 Then
             Debug.Print("  Added")
         Else
             Debug.Print("  Not added")
         End If

         swModel.ClearSelection2(True)

         'Edit the misaligned symmetric concentric mate
         'and change its position from symmetric to aligned
         status = swModelDocExt.SelectByRay(0.0548392523382404, -0.0277425865184, 0.00906375356890976, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.00107347349835279, 2, False, 0, 0)
         status = swModelDocExt.SelectByRay(0.00980255664001106, -0.0292099642897483, 0.193646683964346, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.00107347349835279, 2, True, 0, 0)
         status = swModelDocExt.SelectByID2("Concentric2", "MATE", 0, 0, 0, True, 0, Nothing, 0)
         swAssembly.EditConcentricMate(swMateAlign_e.swMateAlignALIGNED, swConcentricAlignmentType_e.swConcentricAlignThisMate, True, 0.095, errors)

         swModel.ClearSelection2(True)

         If errors = 1 Then
             Debug.Print("  Edited")
             status = swModelDocExt.SelectByID2("Concentric2", "MATE", 0, 0, 0, True, 0, Nothing, 0)
             swFeature = swSelectionManager.GetSelectedObject6(1, -1)
             swMate = swFeature.GetSpecificFeature2

             'Get the linked concentric mate
             swLinkedMate = swMate.GetLinkedMate
             'Get current misaligned deviation
             Debug.Print("    Current misalignment deviation: " & swLinkedMate.GetCurrentMisalignedDeviation)
             'Do not use document property value for misalignment deviation
             swMate.SetUseMisalignedDeviationDocumentProperty(False)
             Debug.Print("    Use document property? " & swMate.GetUseMisalignedDeviationDocumentProperty)
             'Change mate alignment type to symmetric
             swLinkedMate.SetConcentricAlignmentType(swConcentricAlignmentType_e.swConcentricAlignSymmetric)
             Debug.Print("    Concentric alignment type as defined in swConcentricAlignmentType_e: " & swLinkedMate.GetConcentricAlignmentType)
             'Set maximum misalignment deviation
             swMate.SetMaximumMisalignedDeviation(0.102)
             Debug.Print("    Maximum misalignment deviation: " & swMate.GetMaximumMisalignedDeviation)
         Else
             Debug.Print("  Not edited")
         End If

         swModel.ClearSelection2(True)
         swModel.EditRebuild3()

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
