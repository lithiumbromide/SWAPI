---
title: "Add General Spring Connector Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Orthotropic_Spring_Connector_Example_VB.htm"
---

# Add General Spring Connector Example (VBA)

This example shows how to add a general spring connector to a static study.

'==============================================================================

'Preconditions:

'1. Copy the code below into a new VBA macro (**Tools > Macro > New**).

'2. Ensure that the specified assembly template, Simulation example parts, and sldmaterials libraries exist on your machine.

'3. Modify the Part.SaveAs3 path where to save the assembly.

'4. Select the **SOLIWORKS Simulation 2025 type librar**y in the **Tools > References** dialog.

'5. Put a breakpoint after the StudyObj.RunAnalysis line.

'6. Open the Locals window.

'

'Postconditions:

'1. Creates an assembly of two parts.

'2. Adds **Coordinate System1** to the assembly and sldmaterials to its parts.

'3. Creates a **Static 1** study.

'4. Saves the assembly to the folder specified in Preconditions step 3.

'5. Creates connector, **General Spring Connector-1**.

'6. Creates external load, **Force-1**.

'7. Creates fixture**, Fixed-1**.

'8. Meshes and runs the study.

' At the breakpoint, check the ErrorCodeObj in Locals. If the run fails to produce results due to large displacement, re-run the study from the user interface. Click **No** in the dialog box (if it appears) to run the study with small displacement.

'==============================================================================

Dim swApp As SldWorks.SldWorks

Dim Part As SldWorks.ModelDoc2

Dim selMgr As SldWorks.SelectionMgr

Dim COSMOSWORKS As CosmosWorksLib.COSMOSWORKS

Dim COSMOSObject As CosmosWorksLib.CwAddincallback

Dim boolstatus As Boolean

Dim longstatus As Long, longwarnings As Long

Option Explicit

Sub main()

Set swApp = Application.SldWorks

Set COSMOSObject = swApp.GetAddInObject("CosmosWorks.CosmosWorks")

Set COSMOSWORKS = COSMOSObject.COSMOSWORKS

Dim swSheetWidth As Double

swSheetWidth = 0

Dim swSheetHeight As Double

swSheetHeight = 0

Set Part = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2025\templates\Assembly.ASMDOT", 0, swSheetWidth, swSheetHeight)

Dim swAssembly As SldWorks.AssemblyDoc

Set swAssembly = Part

swApp.ActivateDoc2 "Assem1", False, longstatus

Set Part = swApp.ActiveDoc

Dim myModelView As SldWorks.ModelView

Set myModelView = Part.ActiveView

myModelView.FrameState = swWindowState_e.swWindowMaximized

' Insert First Component

Dim AssemblyTitle As String

AssemblyTitle = Part.GetTitle

Dim tmpObj As SldWorks.ModelDoc2

Dim errors As Long

Set tmpObj = swApp.OpenDoc6("c:\users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2025\samples\Simulation Examples\bolt.sldprt", 1, 32, "", errors, longwarnings)

Set Part = swApp.ActivateDoc3(AssemblyTitle, True, 0, errors)

Dim swInsertedComponent As SldWorks.Component2

Set swInsertedComponent = Part.**AddComponent5**("c:\users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2025\samples\Simulation Examples\bolt.sldprt", 0, "", False, "", 4.22645326243774E-03, 4.98635600606522E-03, 8.87075036716113E-03)

swApp.CloseDoc "c:\users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2025\samples\Simulation Examples\bolt.sldprt"

Dim TransformData() As Double

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

TransformData(9) = 1.10844532624377E-02

TransformData(10) = -9.97981130685272E-02

TransformData(11) = 3.12075036716114E-03

TransformData(12) = 1

TransformData(13) = 0

TransformData(14) = 0

TransformData(15) = 0

Dim TransformDataVariant As Variant

TransformDataVariant = TransformData

Dim swMathUtil As SldWorks.MathUtility

Set swMathUtil = swApp.GetMathUtility()

Dim swTransform As SldWorks.MathTransform

Set swTransform = swMathUtil.CreateTransform((TransformDataVariant))

boolstatus = swInsertedComponent.SetTransformAndSolve2(swTransform)

' Insert Second Component

AssemblyTitle = Part.GetTitle

Set tmpObj = swApp.OpenDoc6("c:\users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2025\samples\Simulation Examples\bolthole.sldprt", 1, 32, "", errors, longwarnings)

Set Part = swApp.ActivateDoc3(AssemblyTitle, True, 0, errors)

Set swInsertedComponent = Part.**AddComponent5**("c:\users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2025\samples\Simulation Examples\bolthole.sldprt", 0, "", False, "", -8.07494873879477E-03, -1.23151410953142E-02, 1.35381399886683E-02)

swApp.CloseDoc "c:\users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2025\samples\Simulation Examples\bolthole.sldprt"

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

TransformData(9) = -1.69649487387948E-02

TransformData(10) = -2.12051410953142E-02

TransformData(11) = 2.30631399886683E-02

TransformData(12) = 1

TransformData(13) = 0

TransformData(14) = 0

TransformData(15) = 0

TransformDataVariant = TransformData

Set swMathUtil = swApp.GetMathUtility()

Set swTransform = swMathUtil.CreateTransform((TransformDataVariant))

boolstatus = swInsertedComponent.SetTransformAndSolve2(swTransform)

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 7.54977811998253E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 4.64601730460463E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 2.32300865230232E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 2.32300865230232E-02, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.74225648922674E-02, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.74225648922674E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RollBy 0

boolstatus = Part.Extension.SelectByRay(-1.00698393235064E-02, -3.42514109536296E-03, 1.97180158292554E-02, -0.162363244633107, -0.636158591157886, -0.754281395560187, 1.2339878152205E-03, 2, False, 0, 0)

boolstatus = Part.Extension.SelectByID2("", "FACE", -1.00698393235064E-02, -3.42514109536296E-03, 1.97180158292554E-02, False, 0, Nothing, 0)

Part.ClearSelection2 True

boolstatus = Part.Extension.SelectByID2("bolthole-1@Assem1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)

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

TransformData(9) = -1.25033045143875E-02

TransformData(10) = -3.45510800124485E-02

TransformData(11) = 3.33586698959948E-02

TransformData(12) = 1

TransformData(13) = 0

TransformData(14) = 0

TransformData(15) = 0

TransformDataVariant = TransformData

Set swMathUtil = swApp.GetMathUtility()

Set swTransform = swMathUtil.CreateTransform((TransformDataVariant))

Dim swComp As Object

Set swComp = Part.SelectionManager.GetSelectedObjectsComponent4(1, -1)

boolstatus = swComp.SetTransformAndSolve2(swTransform)

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -2.32300865230232E-02, -8.43111127480969E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -4.64601730460463E-02, -0.168622225496194

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -4.06526514152905E-02, -0.168622225496194

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, -8.43111127480969E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -2.32300865230232E-02, -0.094850001841609

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -2.32300865230232E-02, -0.115927780028633

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, -0.115927780028633

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -5.26944454675605E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -2.32300865230232E-02, -0.14754444730917

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -0.094850001841609

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -6.32333345610726E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -7.37722236545848E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -6.32333345610726E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -0.126466669122145

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -0.115927780028633

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -6.32333345610726E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RollBy 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RollBy 0

boolstatus = Part.Extension.SelectByRay(5.27669548546328E-03, -2.64416482581282E-02, 2.37760223852774E-02, -0.817668314726321, 0.257952628738527, 0.514663937360586, 1.2339878152205E-03, 2, False, 0, 0)

boolstatus = Part.Extension.SelectByID2("", "FACE", 5.27669548546328E-03, -2.64416482581282E-02, 2.37760223852774E-02, False, 0, Nothing, 0)

Part.ClearSelection2 True

boolstatus = Part.Extension.SelectByID2("bolthole-1@Assem1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)

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

TransformData(9) = 2.25142225941603E-03

TransformData(10) = -3.26691591456381E-03

TransformData(11) = 4.11203176790752E-02

TransformData(12) = 1

TransformData(13) = 0

TransformData(14) = 0

TransformData(15) = 0

TransformDataVariant = TransformData

Set swMathUtil = swApp.GetMathUtility()

Set swTransform = swMathUtil.CreateTransform((TransformDataVariant))

Set swComp = Part.SelectionManager.GetSelectedObjectsComponent4(1, -1)

boolstatus = swComp.SetTransformAndSolve2(swTransform)

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -2.32300865230232E-02, -4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -2.32300865230232E-02, -4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -4.64601730460463E-02, -0.105388890935121

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -2.32300865230232E-02, -6.32333345610726E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -0.029037608153779, -5.26944454675605E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -3.48451297845348E-02, -6.32333345610726E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -4.06526514152905E-02, -0.094850001841609

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -4.64601730460463E-02, -0.094850001841609

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, -4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -0.029037608153779, -5.26944454675605E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -2.32300865230232E-02, -4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -0.029037608153779, -6.32333345610726E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -0.029037608153779, -4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -0.029037608153779, -4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, -5.26944454675605E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -2.32300865230232E-02, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -2.32300865230232E-02, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -2.32300865230232E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -2.32300865230232E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, -4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -5.26944454675605E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, -5.26944454675605E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0.029037608153779, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 2.32300865230232E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0.029037608153779, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 2.32300865230232E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 2.32300865230232E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 3.48451297845348E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0.029037608153779, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.74225648922674E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0.029037608153779, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 2.32300865230232E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0.029037608153779, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 2.32300865230232E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 2.32300865230232E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0.029037608153779, 3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.74225648922674E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0.029037608153779, 3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.74225648922674E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 2.32300865230232E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0.029037608153779, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 3.48451297845348E-02, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.74225648922674E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 4.64601730460463E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 2.32300865230232E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 2.32300865230232E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -4.06526514152905E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -2.32300865230232E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -0.029037608153779, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -2.32300865230232E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -2.32300865230232E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -2.32300865230232E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -2.32300865230232E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -3.48451297845348E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -2.32300865230232E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -2.32300865230232E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -4.64601730460463E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -4.06526514152905E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RollBy 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 5.26944454675605E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 6.32333345610726E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 0.105388890935121

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 7.37722236545848E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 6.32333345610726E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 0.094850001841609

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 7.37722236545848E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 6.32333345610726E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 5.26944454675605E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 5.26944454675605E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, 3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, 1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RollBy 0

boolstatus = Part.Extension.SelectByRay(1.14322348396172E-02, -3.26691591453709E-03, 2.92164704875901E-02, -0.303853163367461, 0.952555354827929, -1.76508101860629E-02, 1.2339878152205E-03, 2, False, 0, 0)

boolstatus = Part.Extension.SelectByID2("", "FACE", 1.14322348396172E-02, -3.26691591453709E-03, 2.92164704875901E-02, False, 0, Nothing, 0)

Part.ClearSelection2 True

boolstatus = Part.Extension.SelectByID2("bolthole-1@Assem1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)

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

TransformData(9) = -4.64439690859365E-03

TransformData(10) = -5.44227809768578E-03

TransformData(11) = 4.24326411215984E-02

TransformData(12) = 1

TransformData(13) = 0

TransformData(14) = 0

TransformData(15) = 0

TransformDataVariant = TransformData

Set swMathUtil = swApp.GetMathUtility()

Set swTransform = swMathUtil.CreateTransform((TransformDataVariant))

Set swComp = Part.SelectionManager.GetSelectedObjectsComponent4(1, -1)

boolstatus = swComp.SetTransformAndSolve2(swTransform)

Part.ClearSelection2 True

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, -4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RollBy 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.74225648922674E-02, -7.37722236545848E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.22676946768021E-02, -0.179161114589706

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RollBy 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -4.21555563740484E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -5.26944454675605E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RollBy 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -3.16166672805363E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 2.32300865230232E-02, -5.26944454675605E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 0.029037608153779, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 2.32300865230232E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.16150432615116E-02, -2.10777781870242E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 2.32300865230232E-02, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 5.80752163075579E-03, -1.05388890935121E-02

Set myModelView = Part.ActiveView

myModelView.RollBy 0

Set myModelView = Part.ActiveView

myModelView.Scale2 = 1.14490186397397

Dim swTranslation() As Double

ReDim swTranslation(0 To 2) As Double

swTranslation(0) = 2.84690975061197E-02

swTranslation(1) = 1.69398225598544E-02

swTranslation(2) = 2.77877712619305E-02

Dim swTranslationVar As Variant

swTranslationVar = swTranslation

Set swMathUtil = swApp.GetMathUtility()

Dim swTranslationVector As MathVector

Set swTranslationVector = swMathUtil.CreateVector((swTranslationVar))

myModelView.Translation3 = swTranslationVector

' Insert reference coordinate system and add materials to components

boolstatus = Part.Extension.SelectByRay(1.32973311602882E-02, -5.68470233997687E-03, 2.69903350013578E-02, 0.740333878387101, 0.49389766893956, 0.456038201391486, 8.50094205905406E-04, 1, True, 0, 0)

Part.ClearSelection2 True

boolstatus = Part.Extension.SelectByRay(1.32973311602882E-02, -5.68470233997687E-03, 2.69903350013578E-02, 0.740333878387101, 0.49389766893956, 0.456038201391486, 8.50094205905406E-04, 1, False, 1, 0)

boolstatus = Part.**InsertCoordinateSystem**(False, False, False)

boolstatus = Part.Extension.SelectByID2("Unknown", "BROWSERITEM", 0, 0, 0, False, 0, Nothing, 0)

boolstatus = Part.Extension.SelectByID2("bolt-1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)

Set selMgr = Part.SelectionManager

Dim comp As SldWorks.Component2

Set comp = selMgr.GetSelectedObject6(1, -1)

Dim matChangingModel As SldWorks.ModelDoc2

Set matChangingModel = comp.GetModelDoc()

matChangingModel.**SetMaterialPropertyName2** "Default", "E:/Program Files/SOLIDWORKS Corp/SOLIDWORKS/lang/english/sldmaterials/SOLIDWORKS Materials.sldmat", "Cast Alloy Steel"

boolstatus = Part.Extension.SelectByID2("bolthole-1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)

boolstatus = Part.Extension.SelectByID2("Unknown", "BROWSERITEM", 0, 0, 0, False, 0, Nothing, 0)

boolstatus = Part.Extension.SelectByID2("bolthole-1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)

Set comp = selMgr.GetSelectedObject6(1, -1)

Set matChangingModel = comp.GetModelDoc()

matChangingModel.**SetMaterialPropertyName2** "Default", "E:/Program Files/SOLIDWORKS Corp/SOLIDWORKS/lang/english/sldmaterials/SOLIDWORKS Materials.sldmat", "Plain Carbon Steel"

' Create static study

Part.GraphicsRedraw2

Dim ActiveDocObj As CosmosWorksLib.CWModelDoc

Dim StudyManagerObj As CosmosWorksLib.CWStudyManager

Dim LoadsAndRestraintsManagerObj As CosmosWorksLib.CWLoadsAndRestraintsManager

Dim ErrorCodeObj As Long

Set ActiveDocObj = COSMOSWORKS.ActiveDoc()

Set StudyManagerObj = ActiveDocObj.StudyManager()

StudyManagerObj.ActiveStudy = 0

Dim NewStudyName As String

NewStudyName = "Static 1"

Dim CWNewStudy As CosmosWorksLib.CWStudy

Set CWNewStudy = StudyManagerObj.**CreateNewStudy3**(NewStudyName, 0, 0, ErrorCodeObj)

Part.ClearSelection2 True

' Save Assem.sldasm

longstatus = Part.**SaveAs3**("E:\2025\Simulation\Assem.SLDASM", 0, 0)

' Select face on bolt part

Part.GraphicsRedraw2

boolstatus = Part.Extension.SelectByRay(3.05895955085589E-03, 5.18722164261476E-03, 1.81207503671033E-02, 0.891602727513332, 0.357815266269476, -0.277511822298243, 3.74971675130397E-04, 2, True, 0, 0)

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -4.43369930950173E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 4.43369930950173E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 3.10358951665121E-02, -3.27818363852849E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 8.86739861900347E-03, -8.19545909632122E-03

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 3.54695944760139E-02, -2.45863772889637E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 4.43369930950173E-02, -2.45863772889637E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 2.66021958570104E-02, -1.63909181926424E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 4.43369930950173E-02, -2.45863772889637E-02

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.33010979285052E-02, -8.19545909632122E-03

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 2.66021958570104E-02, -8.19545909632122E-03

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 2.21684965475087E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 8.86739861900347E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 2.21684965475087E-02, -8.19545909632122E-03

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.33010979285052E-02, -8.19545909632122E-03

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 8.86739861900347E-03, -8.19545909632122E-03

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.77347972380069E-02, -8.19545909632122E-03

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.33010979285052E-02, -8.19545909632122E-03

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 8.86739861900347E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 8.86739861900347E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 8.86739861900347E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 8.86739861900347E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.33010979285052E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 4.43369930950173E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 8.86739861900347E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 8.86739861900347E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 8.86739861900347E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.77347972380069E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 4.43369930950173E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.33010979285052E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 8.86739861900347E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.77347972380069E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 8.86739861900347E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.77347972380069E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.33010979285052E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.77347972380069E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.33010979285052E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 8.86739861900347E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 2.66021958570104E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 1.77347972380069E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 4.43369930950173E-03, -8.19545909632122E-03

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 4.43369930950173E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter 4.43369930950173E-03, 0

' Select face on bolt hole part

Part.GraphicsRedraw2

boolstatus = Part.Extension.SelectByRay(3.32916435917241E-03, 2.13373748687218E-03, 0.0233826411216, 0.894580374859918, 0.275528156746822, 0.35186671873763, 3.74971675130397E-04, 2, True, 0, 0)

' Select Coordinate System1

Part.GraphicsRedraw2

boolstatus = Part.Extension.SelectByID2("Coordinate System1", "COORDSYS", 0, 0, 0, True, 0, Nothing, 0)

'Add General Spring Connector

Set ActiveDocObj = COSMOSWORKS.ActiveDoc()

Set StudyManagerObj = ActiveDocObj.StudyManager()

Dim StudyObj As CosmosWorksLib.CWStudy

Set StudyObj = StudyManagerObj.GetStudy(0)

Set LoadsAndRestraintsManagerObj = StudyObj.LoadsAndRestraintsManager()

Dim DispatchObj1 As Object

Set DispatchObj1 = Part.SelectionManager.GetSelectedObject6(1, -1)

Dim DispatchObj2 As Object

Set DispatchObj2 = Part.SelectionManager.GetSelectedObject6(2, -1)

Dim CoordSystDispatchObj As Object

Set CoordSystDispatchObj = Part.SelectionManager.GetSelectedObject6(3, -1)

Dim CWGeneralSpringConnector As CosmosWorksLib.CWGeneralSpringConnector

Set CWGeneralSpringConnector = LoadsAndRestraintsManagerObj.**AddGeneralSpringConnector**(DispatchObj1, DispatchObj2, ErrorCodeObj)

CWGeneralSpringConnector.**BeginEdit**

CWGeneralSpringConnector.**Unit** = 0

CWGeneralSpringConnector.**SetReferenceCoordinateSystem** CoordSystDispatchObj

CWGeneralSpringConnector.**TransverselyIsotropicStiffness** = False

CWGeneralSpringConnector.**AxialStiffnessValue** = 1000#

CWGeneralSpringConnector.**LateralStiffnessYValue** = 200#

CWGeneralSpringConnector.**LateralStiffnessZValue** = 300#

CWGeneralSpringConnector.**TorsionalStiffnessValue** = 40#

CWGeneralSpringConnector.**BendingStiffnessYValue** = 50#

CWGeneralSpringConnector.**BendingStiffnessZValue** = 60#

CWGeneralSpringConnector.**PreLoadForceType** = 0

CWGeneralSpringConnector.**PreLoadForceValue** = 70#

CWGeneralSpringConnector.**EndEdit**

Part.ClearSelection2 True

' Select face and add force load to it

Part.GraphicsRedraw2

boolstatus = Part.Extension.SelectByRay(4.4736627132238E-03, 4.18086227307413E-03, -3.79249632885603E-04, 0.672879319797199, -0.590972379829742, 0.444955129499178, 4.86074393687552E-04, 2, True, 0, 0)

Set LoadsAndRestraintsManagerObj = StudyObj.LoadsAndRestraintsManager()

Set DispatchObj1 = Part.SelectionManager.GetSelectedObject6(1, -1)

Dim DispArray As Variant

DispArray = Array(DispatchObj1)

Dim CWForceObj As CosmosWorksLib.CWForce

Dim DistanceValues As Variant

Dim ForceValues As Variant

Dim ComponentValues As Variant

Dim data(6) As Double

data(0) = 1

data(1) = 1

data(2) = 1

data(3) = 1

data(4) = 1

data(5) = 1

ComponentValues = data

Set CWForceObj = LoadsAndRestraintsManagerObj.**AddForce3**(1, 0, -1, 0, 0, 0, (DistanceValues), (ForceValues), 0, False, 0, 0, 0, 100, (ComponentValues), False, False, (DispArray), Nothing, False, ErrorCodeObj)

Part.ClearSelection2 True

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -0.029037608153779, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -3.48451297845348E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -0.029037608153779, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -6.38827379383137E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -6.38827379383137E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.22676946768021E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -4.06526514152905E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -0.029037608153779, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -3.48451297845348E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -0.029037608153779, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -6.96902595690695E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.74225648922674E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -4.06526514152905E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -2.32300865230232E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -2.32300865230232E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -1.16150432615116E-02, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.22676946768021E-02, 0.010623743273009

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -0.029037608153779, 0

Set myModelView = Part.ActiveView

myModelView.RotateAboutCenter -5.80752163075579E-03, 0

' Select restraint face

Part.GraphicsRedraw2

boolstatus = Part.Extension.SelectByRay(8.04901481643583E-03, 8.08711753433045E-03, 4.24326411215361E-02, 0.596978248079075, -0.660237078683955, -0.455745511498815, 4.86074393687552E-04, 2, False, 0, 0)

' Add fixed restraint

Part.GraphicsRedraw2

Set LoadsAndRestraintsManagerObj = StudyObj.LoadsAndRestraintsManager()

Set DispatchObj1 = selMgr.GetSelectedObject6(1, -1)

DispArray = Array(DispatchObj1)

Dim CWRestraintObj As CosmosWorksLib.CWRestraint

Set CWRestraintObj = LoadsAndRestraintsManagerObj.**AddRestraint**(0, (DispArray), Nothing, ErrorCodeObj)

Part.ClearSelection2 True

'Mesh and run

ErrorCodeObj = StudyObj.**CreateMesh**(2, 0.00184399, 0.00184399)

ErrorCodeObj = StudyObj.**RunAnalysis**()

'Due to large displacement, the run may fail to generate results

'Mesh and run from the user interface and select **No** in the dialog box (if it appears) to run with small displacement

End Sub
