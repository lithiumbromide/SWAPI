---
title: "Create Rectangular Viewport Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Rectangular_Viewport_Example_VBNET.htm"
---

# Create Rectangular Viewport Example (VB.NET)

This example shows how to create a rectangular Viewport.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this project into the VB.NET IDE.
' 3. Add a reference to
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll
' 4. Start DraftSight.
' 5. Open the Immediate window.
' 6. Press F5.
'
' Postconditions:
' 1. A Viewport is created on Sheet2.
' 2. Examine the drawing and output printed
'    to the Immediate window.
'----------------------------------------------------------------
```

```
Imports DraftSight.Interop.dsAutomation

Module Module1

    Sub Main()

        Dim dsApp As Application
        Dim dsDoc As Document
        Dim SheetName As String
        Dim dsSheets As Object
        Dim dsSheet As Sheet
        Dim index As Integer
        Dim dsViewport As Viewport
        Dim dsMathUtility As MathUtility
        Dim startCorner As MathPoint
        Dim oppositeCorner As MathPoint
        Dim isClipped As Boolean

        'Connect to DraftSight
        dsApp = GetObject(, "DraftSight.Application")

        'Abort any command currently running in DraftSight
        'to avoid nested commands
        dsApp.AbortRunningCommand()

        'Get active document
        dsDoc = dsApp.GetActiveDocument()
        If Not dsDoc Is Nothing Then

            'Switch to Sheet space and activate Sheet2
            dsSheets = dsDoc.GetSheets
            If IsArray(dsSheets) Then
                For index = LBound(dsSheets) To UBound(dsSheets)
                    dsSheet = dsSheets(index)
                    'Get sheet name
                    SheetName = dsSheet.Name
                    'Change sheet name, if it is not a model
                    If SheetName <> "Model" Then
                        'Activate sheet
                        dsSheet.Activate()
                    End If
                Next
            End If

            ' Set the corners for the Viewport
            dsMathUtility = dsApp.GetMathUtility
            startCorner = dsMathUtility.CreatePoint(0, 0, 0)
            oppositeCorner = dsMathUtility.CreatePoint(3, 3, 0)

            'Create a rectangular Viewport
            dsViewport = dsSheet.InsertRectangularViewport(dsStandardViewports_e.dsStandardViewports_1, False, startCorner, oppositeCorner)

            ' Activate and access the rectangular Viewport
            dsViewport.Active = True
            Debug.Print(SheetName & ":")
            Debug.Print("  Viewport:")
            dsViewport.GetIsClipped(isClipped)
            Debug.Print("    Clipped by an entity?       " & isClipped)
            Debug.Print("    Height:                     " & dsViewport.Height)
            Debug.Print("    Width:                      " & dsViewport.Width)
            Debug.Print("    Locked in model workspace?  " & dsViewport.DisplayLocked)
            Debug.Print("    Displayed in graphics area? " & dsViewport.IsOn)
            Debug.Print("    Visible?                    " & dsViewport.Visible)
        Else
            Debug.Print("There are no open documents in DraftSight.")
        End If

    End Sub

End Module
```
