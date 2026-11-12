---
title: "Add and Edit Distance Mate Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_and_Edit_Distance_Mate_Example_VB.htm"
---

# Add and Edit Distance Mate Example (VBA)

This example shows how to add and edit a cylindrical distance mate.

'----------------------------------------------------------------------------
' Preconditions:
' 1. Ensure the specified template exists.
' 2. Open `public_documents`**\samples\tutorial\api\cylinder20.sldprt.**
' 3. Open an Immediate window.
'
' Postconditions:
' 1. Creates and saves a new cylindrical part.
' 2. Adds two cylindrical entities to a new assembly.
' 3. Creates a distance mate between the cylindrical entities.
' 4. Edits the distance mate to change the distance from 0.2 to 0.3.
' 5. Inspect the Immediate window, the graphics area, and the Mates folder
' of the FeatureManager design tree.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'----------------------------------------------------------------------------

```vb
Dim swApp As SldWorks.SldWorks
 Dim swAssembly As SldWorks.AssemblyDoc
 Dim Part As SldWorks.ModelDoc2
 Dim AssemblyTitle As String
 Dim swInsertedComponent As Component2
 Dim swFeat As Feature
 Dim boolstatus As Boolean
 Dim longstatus As Long, longwarnings As Long
 Dim swSheetWidth As Double
 Dim swSheetHeight As Double
 Dim swMate As Mate2
 Dim tmpObj As ModelDoc2
 Dim errors As Long
 Dim swEnt1 As SldWorks.Entity
 Dim swEnt2 As SldWorks.Entity
 Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc

    ' Shell the active part
     boolstatus = Part.Extension.SelectByRay(-1.08900020093756E-02, 6.55319999998483E-02, -5.15652172191494E-03, -0.400036026779312, -0.515038074910024, -0.758094294050284, 1.67637314537445E-03, 2, False, 1, 0)
     Part.InsertFeatureShell 0.00254, False

    ' Save the shelled part
     longstatus = Part.SaveAs3("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cylinder20_shell.sldprt", 0, 2)

    ' Create a new assembly
     swSheetWidth = 0
     swSheetHeight = 0
     Set Part = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2018\templates\Assembly.asmdot", 0, swSheetWidth, swSheetHeight)

    ' Insert a cylinder20_shell component
     AssemblyTitle = Part.GetTitle
     Set tmpObj = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cylinder20_shell.sldprt", 1, 32, "", longstatus, longwarnings)
     Set Part = swApp.ActivateDoc3(AssemblyTitle, True, 0, longstatus)
     Set swInsertedComponent = Part.AddComponent5("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cylinder20_shell.sldprt", 0, "", False, "", 0.119562469422817, -1.02308109635487E-02, -4.74663286004215E-02)
     swApp.CloseDoc "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cylinder20_shell.sldprt"
    ' Insert another cylinder20_shell component
     Set tmpObj = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cylinder20_shell.sldprt", 1, 32, "", errors, longwarnings)
     Set Part = swApp.ActivateDoc3(AssemblyTitle, True, 0, errors)
     Set swInsertedComponent = Part.AddComponent5("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cylinder20_shell.sldprt", 0, "", False, "", -0.130620346986689, -1.01738580269739E-02, 0.084551733918488)
     swApp.CloseDoc "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cylinder20_shell.sldprt"

    ' Select two cylindrical entities
     boolstatus = Part.Extension.SelectByRay(-0.140174514310559, 2.37221117538411E-03, 2.64513806530431E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 8.6563679245283E-04, 2, False, 1, 0)
     Set swEnt1 = Part.SelectionManager.GetSelectedObject6(1, -1)
     boolstatus = Part.Extension.SelectByRay(6.79787981690652E-02, -7.25673614920197E-03, -7.58574895979791E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 6.36203082166533E-04, 2, True, 1, 0)
     Set swEnt2 = Part.SelectionManager.GetSelectedObject6(1, -1)

    swEnt1.Select4 True, Nothing
     swEnt2.Select4 True, Nothing

    ' Add a center-to-center distance mate between the selected cylindrical entities
     Set swAssembly = Part
    Set swMate = swAssembly.AddDistanceMate(2, False, 0.2, 0, 0, 1, 1, errors)
     Debug.Print "First arc condition as defined in swDistanceMateArcConditions_e: " & swMate.DistanceFirstArcCondition
     Debug.Print "Second arc condition as defined in swDistanceMateArcConditions_e: " & swMate.DistanceSecondArcCondition
     Set swFeat = swMate

    Part.EditRebuild3

    ' Edit the distance mate to change the distance from 0.2 to 0.3
     boolstatus = Part.Extension.SelectByRay(-9.36626010895907E-02, 6.78476678046991E-04, -4.54698905400619E-04, -0.400036026779312, -0.515038074910024, -0.758094294050284, 8.08436123348018E-04, 2, True, 1, 0)
     Set swEnt1 = Part.SelectionManager.GetSelectedObject6(1, -1)
     boolstatus = Part.Extension.SelectByRay(8.03986691953469E-02, -1.07796570199525E-03, -9.14337018962783E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 8.08436123348018E-04, 2, True, 2, 0)
     Set swEnt2 = Part.SelectionManager.GetSelectedObject6(2, -1)

    swEnt1.Select4 True, Nothing
     swEnt2.Select4 True, Nothing
     swFeat.Select2 True, 0

    swAssembly.EditDistanceMate 2, False, 0.3, 0, 0, 1, 1, errors

    Part.EditRebuild3
End Sub
```
