---
title: "Get and Set Windows Values Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_and_Set_Windows_Values_Example_VBNET.htm"
---

# Get and Set Windows Values Example (VB.NET)

This example shows how to get and set various DraftSight application and document window values.

```
'--------------------------------------------------------------
' Preconditions:
'  1. Create a VB.NET Windows console project.
'  2. Copy and paste this project into the VB.NET IDE.
'  3. Add a reference to
'     install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll
'  4. Start DraftSight.
'  5. Open the Immediate window.
'  6. Press F5.
'
' Postconditions:
' 1. Document window is minimized.
' 2. Examine the Immediate window where
'    the application and document window handle values,
'    visibility values, window states, and frame and
'    geometry positions and sizes are printed.
' 3. Interactively maximize the document window in DraftSight.
'----------------------------------------------------------------

Imports System.IO
Imports DraftSight.Interop.dsAutomation

Module Module1

    Dim dsApp As Application
    Dim dsDoc As Document
    Dim dsAppWindow As DraftSight.Interop.dsAutomation.DSWindow
    Dim dsDocWindow As DraftSight.Interop.dsAutomation.DSWindow

    Sub Main()
        'Connect to DraftSight
        dsApp = GetObject(, "DraftSight.Application")

        'Abort any command currently running in DraftSight
        'to avoid nested commands
        dsApp.AbortRunningCommand()

        'Get application's window handle, visibility, and state
        Debug.Print("Application window using Application object:")
        Debug.Print("  Window handle: " & dsApp.GetHWND)
        Debug.Print("  Visible:       " & dsApp.Visible)
        Debug.Print("  State:         " & dsApp.WindowState)

        Debug.Print("")

        'Get active document
        dsDoc = dsApp.GetActiveDocument()
        If Not dsDoc Is Nothing Then
            ' Get application's window handle, visibility, and state
            Debug.Print("Application window using DSWindow object:")
            dsAppWindow = dsApp.GetMainWindow()
            Dim windowHandle As Integer
            dsAppWindow.GetHWND(windowHandle)
            Debug.Print("  Window handle:     " & windowHandle)
            Debug.Print("  Visible            " & dsAppWindow.Visible)
            Debug.Print("  State:             " & dsAppWindow.WindowState)
            Dim x As Integer
            Dim y As Integer
            ' Get application's frame and geometry positions and sizes
            dsAppWindow.GetFramePosition(x, y)
            Debug.Print("  Frame position:    " & x & ", " & y)
            dsAppWindow.GetFrameSize(x, y)
            Debug.Print("  Frame size:        " & x & ", " & y)
            dsAppWindow.GetGeometryPosition(x, y)
            Debug.Print("  Geometry position: " & x & ", " & y)
            dsAppWindow.GetGeometrySize(x, y)
            Debug.Print("  Geometry size:     " & x & ", " & y)

            Debug.Print(" ")

            ' Get document's window handle, visibility, state,
            ' frame and geometry positions and sizes
            Debug.Print("Document window using DSWindow object before minimizing window:")
            dsDocWindow = dsDoc.GetWindow()
            dsDocWindow.GetHWND(windowHandle)
            Debug.Print("  Window handle:     " & windowHandle)
            Debug.Print("  Visible            " & dsDocWindow.Visible)
            Debug.Print("  State:             " & dsDocWindow.WindowState)
            dsDocWindow.GetFramePosition(x, y)
            Debug.Print("  Frame position:    " & x & ", " & y)
            dsDocWindow.GetFrameSize(x, y)
            Debug.Print("  Frame size:        " & x & ", " & y)
            dsDocWindow.GetGeometryPosition(x, y)
            Debug.Print("  Geometry position: " & x & ", " & y)
            dsDocWindow.GetGeometrySize(x, y)
            Debug.Print("  Geometry size:     " & x & ", " & y)

            'Minimize Document window
            dsDocWindow.WindowState = 0

            Debug.Print("")
            ' Get document's window handle, visibility, state,
            ' frame and geometry positions and sizes after minimizing
            ' window
            Debug.Print("Document window using DSWindow object after minimizing the window:")
            dsDocWindow = dsDoc.GetWindow()
            dsDocWindow.GetHWND(windowHandle)
            Debug.Print("  Window handle:     " & windowHandle)
            Debug.Print("  Visible            " & dsDocWindow.Visible)
            Debug.Print("  State:             " & dsDocWindow.WindowState)
            dsDocWindow.GetFramePosition(x, y)
            Debug.Print("  Frame position:    " & x & ", " & y)
            dsDocWindow.GetFrameSize(x, y)
            Debug.Print("  Frame size:        " & x & ", " & y)
            dsDocWindow.GetGeometryPosition(x, y)
            Debug.Print("  Geometry position: " & x & ", " & y)
            dsDocWindow.GetGeometrySize(x, y)
            Debug.Print("  Geometry size:     " & x & ", " & y)

        Else
            MsgBox("There are no open documents in DraftSight.")
        End If

    End Sub

End Module
```
