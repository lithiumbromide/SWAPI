---
title: "Create Rectangular Viewport Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Rectangular_Viewport_Example_VBA.htm"
---

# Create Rectangular Viewport Example (VBA)

This example shows how to create a rectangular Viewport.

```
'--------------------------------------------------------------
'Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight.
' 5  Open the Immediate window.
' 6. Run the macro.
'
' Postconditions:
' 1. A Viewport is created on Sheet2.
' 2. Examine the drawing and output printed
'    to the Immediate window.
'----------------------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document
    Dim SheetName as String
    Dim dsSheets As Variant
    Dim dsSheet As DraftSight.Sheet
    Dim index As Long
    Dim dsViewport As DraftSight.Viewport
    Dim dsMathUtility As DraftSight.MathUtility
    Dim startCorner As DraftSight.MathPoint
    Dim oppositeCorner As DraftSight.MathPoint
    Dim isClipped As Boolean
```

```
    'Connect to DraftSight
    Set dsApp = GetObject(, "DraftSight.Application")
```

```
    'Abort any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand
```

```
    'Get active document
    Set dsDoc = dsApp.GetActiveDocument()
    If Not dsDoc Is Nothing Then
```

```
        'Switch to Sheet space and activate Sheet2
        dsSheets = dsDoc.GetSheets
        If IsArray(dsSheets) Then
            For index = LBound(dsSheets) To UBound(dsSheets)
                Set dsSheet = dsSheets(index)
                'Get sheet name
                SheetName = dsSheet.Name
                'Change sheet name, if it is not a model
                If SheetName <> "Model" Then
                    'Activate sheet
                    dsSheet.Activate
                End If
            Next
        End If
```

```
        ' Set the corners for the Viewport
        Set dsMathUtility = dsApp.GetMathUtility
        Set startCorner = dsMathUtility.CreatePoint(0, 0, 0)
        Set oppositeCorner = dsMathUtility.CreatePoint(3, 3, 0)
```

```
        'Create a rectangular Viewport
        Set dsViewport = dsSheet.InsertRectangularViewport(dsStandardViewports_1, False, startCorner, oppositeCorner)
```

```
        ' Activate and access the rectangular Viewport
        dsViewport.Active = True
```

```
        Debug.Print (SheetName & ":")
        Debug.Print "  Viewport:"
        dsViewport.GetIsClipped (isClipped)
        Debug.Print "    Clipped by an entity?       " & isClipped
        Debug.Print "    Height:                     " & dsViewport.Height
        Debug.Print "    Width:                      " & dsViewport.Width
        Debug.Print "    Locked in model workspace?  " & dsViewport.DisplayLocked
        Debug.Print "    Displayed in graphics area? " & dsViewport.IsOn
        Debug.Print "    Visible?                    " & dsViewport.Visible
```

```
    Else

        Debug.Print "There are no open documents in DraftSight."
```

```
    End If
End Sub
```
