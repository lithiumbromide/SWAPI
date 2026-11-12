---
title: "Create Model and Sheet Views Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Model_and_Sheet_Views_Example_VBA.htm"
---

# Create Model and Sheet Views Example (VBA)

This example shows how to create:

- model named view with a gradient background.
- model named view without a background.
- sheet named view.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Open the Immediate window.
' 4. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
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
'--------------------------------------------------------------
```

```
Option Explicit
```

```
    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document
    Dim dsModel As DraftSight.Model
    Dim dsViewMgr As DraftSight.ViewManager
    Dim dsCorner1(2) As Double
    Dim dsCorner2(2) As Double
    Dim dsCorner3(2) As Double
    Dim dsCorner4(2) As Double
    Dim dsModelNamedView As DraftSight.ModelNamedView
    Dim dsSheetNamedView As DraftSight.SheetNamedView
    Dim dsSheet As DraftSight.Sheet
    Dim dsSheets As Variant
    Dim result As dsCreateObjectResult_e
    Dim dsGradientBackground As DraftSight.GradientBackground
    'Dim dsSolidBackground As DraftSight.SolidBackground
    'Dim dsImageBackground As DraftSight.ImageBackground
    Dim imageFile As String
    Dim dsColor As DraftSight.Color
    Dim dsColor2 As DraftSight.Color
    Dim dsColor3 As DraftSight.Color
```

```
    Sub main()
        'Connect to DraftSight
        Set dsApp = GetObject(, "DraftSight.Application")
        'Abort any command currently running in DraftSight
        'to avoid nested commands
        dsApp.AbortRunningCommand
```

```
        'Get active document
        Set dsDoc = dsApp.GetActiveDocument()
        If Not dsDoc Is Nothing Then
            dsCorner1(0) = 16.12
            dsCorner1(1) = 12.23
            dsCorner1(2) = 0#
            dsCorner2(0) = 25.46
            dsCorner2(1) = 20.47
            dsCorner2(2) = 0#
            dsCorner3(0) = 5#
            dsCorner3(1) = 4.5
            dsCorner3(2) = 0#
            dsCorner4(0) = 7.36
            dsCorner4(1) = 6.38
            dsCorner4(2) = 0#
```

```
            'Get the view manager
            Set dsViewMgr = dsDoc.GetViewManager()
```

```
            'In model space, create a model named view
            Set dsModel = dsDoc.GetModel
            dsModel.Activate
            result = dsViewMgr.CreateModelNamedView("ModelView", "A", dsCorner1, dsCorner2, dsModelNamedView)
```

```
            Set dsColor = dsApp.GetNamedColor(dsNamedColor_Blue)
            Set dsColor2 = dsApp.GetNamedColor(dsNamedColor_Cyan)
            Set dsColor3 = dsApp.GetNamedColor(dsNamedColor_Green)
```

```
            'Create gradient background
            Set dsGradientBackground = dsViewMgr.CreateGradientBackground(dsColor, dsColor2, dsColor3, False, 0)
```

```
            'Create solid background
            'Set dsSolidBackground = dsViewMgr.CreateSolidBackground(dsColor)
```

```
            'Create image background
            imageFile = "image_path_file_name"
            'Set dsImageBackground = dsViewMgr.CreateImageBackground(imageFile, dsImageBackgroundPosition_Tile, 0, 0, 0, 0)
```

```
            Debug.Print ("Result (1 = Object successfully created, 2 = Object already exists, 3 = Error creating object): " & result)
            Debug.Print ("Model named view: " & dsModelNamedView.GetNamedView.GetName)
            Set dsModelNamedView = dsViewMgr.GetModelNamedView("ModelView")
            'Set background of ModelView and verify
            'by getting its background type
            dsModelNamedView.SetGradientBackground dsGradientBackground
            'dsModelNamedView.SetSolidBackground dsSolidBackground
            'dsModelNamedView.SetImageBackground dsImageBackground
            Debug.Print ("Type of background: " & dsModelNamedView.GetBackgroundType)
            result = dsViewMgr.SaveCurrentViewAsModelView("SavedModelView", "A", dsModelNamedView)
            dsViewMgr.ActivateModelView ("SavedModelView")

            Debug.Print ""
```

```
            'Switch to sheet space and create a sheet named view in Sheet1
            dsSheets = dsDoc.GetSheets
            dsSheets(1).Activate
            result = dsViewMgr.CreateSheetNamedView("SheetView", "B", dsCorner3, dsCorner4, dsSheetNamedView)
            Debug.Print ("Result (1 = Object successfully created, 2 = Object already exists, 3 = Error creating object): " & result)
            Debug.Print ("Sheet named view: " & dsSheetNamedView.GetNamedView.GetName)
            Set dsSheetNamedView = dsViewMgr.GetSheetNamedView("SheetView")
            Set dsSheet = dsSheetNamedView.GetSheet()
            result = dsViewMgr.SaveCurrentViewAsSheetView("SavedSheetView", "B", dsSheetNamedView)
            dsViewMgr.ActivateSheetView ("SheetView")
```

```
        Else
            MsgBox ("There are no open documents in DraftSight.")
        End If
```

```
    End Sub
```
