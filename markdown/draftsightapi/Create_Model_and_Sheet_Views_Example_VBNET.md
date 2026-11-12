---
title: "Create Model and Sheet Views Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Model_and_Sheet_Views_Example_VBNET.htm"
---

# Create Model and Sheet Views Example (VB.NET)

This example shows how to create:

- model named view with a gradient background.
- model named view without a background.
- sheet named view.

```
'--------------------------------------------------------------
'Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this project into the VB.NET IDE.
' 3. Open the Immediate window.
' 4. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 5. Start DraftSight and open
'    disk:\ProgramData\Dassault Systemes\DraftSight\Examples\pump housing.dwg.
' 6. Press F5.
'
'Postconditions:
' 1. A model named view, ModelView, is created with a gradient background
'    and is classified in the A category.
' 2. A model named view, SavedModelView, is created without a background.
' 3. A sheet named view, SheetView, is created and
'    classified in the B category.
' 4. Click View > Named Views and examine both the model and sheet.
' 5. Examine the Immediate window.
'
' NOTE: To change the background to:
' 1. Solid from gradient:
'    a. Uncomment these lines of code:
'       'Dim dsSolidBackground As SolidBackground
'       'dsSolidBackground = dsViewMgr.CreateSolidBackground(dsColor)
'       'dsModelNamedView.SetSolidBackground(dsSolidBackground)
'    b. Comment out these lines of code:
'       Dim dsGradientBackground As GradientBackground
'       dsGradientBackground = dsViewMgr.CreateGradientBackground(dsColor, dsColor2, dsColor3, False, 0)
'       dsModelNamedView.SetGradientBackground(dsGradientBackground)
' 2. Image from gradient:
'    a. Uncomment these lines of code:
'       'Dim dsImageBackground As ImageBackground
'       'dsImageBackground = dsViewMgr.CreateImageBackground(imageFile, dsImageBackgroundPosition_e.dsImageBackgroundPosition_Tile, 0, 0, 0, 0)
'       'dsModelNamedView.SetImageBackground(dsImageBackground)
'    b. Perform step 1b.
'    c. Substitute the path and file name of your image for
'       image_path_file_name.
'----------------------------------------------------------------

Imports System.IO
Imports DraftSight.Interop.dsAutomation

Module Module1

    Dim dsApp As Application
    Dim dsDoc As Document
    Dim dsViewMgr As ViewManager
    Dim dsCorner1 As Double() = New Double() {16.12, 12.23, 0.0}
    Dim dsCorner2 As Double() = New Double() {25.46, 20.47, 0.0}
    Dim dsCorner3 As Double() = New Double() {5.0, 4.5, 0.0}
    Dim dsCorner4 As Double() = New Double() {7.36, 6.38, 0.0}
    Dim dsModelNamedView As ModelNamedView
    Dim dsSheetNamedView As SheetNamedView
    Dim dsSheet As Sheet
    Dim dsSheets As Sheet()
    Dim dsSheetArray As Object
    Dim dsGradientBackground As GradientBackground
    'Dim dsSolidBackground As SolidBackground
    'Dim dsImageBackground As ImageBackground
    Dim imageFile As String
    Dim dsColor As Color
    Dim dsColor2 As Color
    Dim dsColor3 As Color
    Dim result As dsCreateObjectResult_e

    Sub Main()
        'Connect to DraftSight
        dsApp = GetObject(, "DraftSight.Application")

        'Get active document
        dsDoc = dsApp.GetActiveDocument()
        If Not dsDoc Is Nothing Then

            'Get the view manager
            dsViewMgr = dsDoc.GetViewManager()

            'In the model space, create a model named view
            result = dsViewMgr.CreateModelNamedView("ModelView", "A", dsCorner1, dsCorner2, dsModelNamedView)

            dsColor = dsApp.GetNamedColor(dsNamedColor_e.dsNamedColor_Blue)
            dsColor2 = dsApp.GetNamedColor(dsNamedColor_e.dsNamedColor_Cyan)
            dsColor3 = dsApp.GetNamedColor(dsNamedColor_e.dsNamedColor_Green)

            'Create gradient background
            dsGradientBackground = dsViewMgr.CreateGradientBackground(dsColor, dsColor2, dsColor3, False, 0)

            'Create solid background
            'dsSolidBackground = dsViewMgr.CreateSolidBackground(dsColor)

            'Create image background
            imageFile = "image_path_file_name"
            'dsImageBackground = dsViewMgr.CreateImageBackground(imageFile, dsImageBackgroundPosition_e.dsImageBackgroundPosition_Tile, 0, 0, 0, 0)

            Debug.Print("Result: " & result.ToString)
            Debug.Print("Model named view: " & dsModelNamedView.GetNamedView.GetName)
            dsModelNamedView = dsViewMgr.GetModelNamedView("ModelView")

            'Set background of ModelView and verify
            'by getting its background type
            dsModelNamedView.SetGradientBackground(dsGradientBackground)
            'dsModelNamedView.SetSolidBackground(dsSolidBackground)
            'dsModelNamedView.SetImageBackground(dsImageBackground)
            Debug.Print("Type of background: " & dsModelNamedView.GetBackgroundType())
            dsViewMgr.SaveCurrentViewAsModelView("SavedModelView", "A", dsModelNamedView)
            dsViewMgr.ActivateModelView("SavedModelView")
```

```
            Debug.Print("")

            'Switch to sheet space and create a sheet named view in Sheet1
            dsSheetArray = dsDoc.GetSheets
            ' First sheet is actually a model named view,
            ' so assign next element in array to dsSheet
            dsSheet = dsSheetArray(1)
            dsSheet.Activate()
            result = dsViewMgr.CreateSheetNamedView("SheetView", "B", dsCorner3, dsCorner4, dsSheetNamedView)
            Debug.Print("Result: " & result.ToString)
            Debug.Print("Sheet named view: " & dsSheetNamedView.GetNamedView.GetName)
            dsSheetNamedView = dsViewMgr.GetSheetNamedView("SheetView")
            dsSheet = dsSheetNamedView.GetSheet()
            dsViewMgr.SaveCurrentViewAsSheetView("SavedSheetView", "B", dsSheetNamedView)
            dsViewMgr.ActivateSheetView("SheetView")

        Else
            MsgBox("There are no open documents in DraftSight.")
        End If

    End Sub

End Module
```
