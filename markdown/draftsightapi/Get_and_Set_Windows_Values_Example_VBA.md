---
title: "Get and Set Windows Values Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_and_Set_Windows_Values_Example_VBA.htm"
---

# Get and Set Windows Values Example (VBA)

This example shows how to get and set various DraftSight application and document window values.

```
'--------------------------------------------------------------
' Preconditions:
'  1. Create a VBA macro in a software product in which VBA is
'     embedded.
'  2. Copy and paste this project into the Visual Basic IDE.
'  3. Add a reference to
'     install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll
'  4. Start DraftSight.
'  5. Open the Immediate window.
'  6. Run the macro.
'
' Postconditions:
' 1. Document window is minimized.
' 2. Examine the Immediate window where
'    the application and document window handle values,
'    visibility values, window states, and frame and
'    geometry positions and sizes are printed.
' 3. Interactively maximize the Document window in DraftSight.
'----------------------------------------------------------------
 Option Explicit
```

```
    Sub main()
```

```
    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document
    Dim dsAppWindow As DraftSight.DSWindow
    Dim dsDocWindow As DraftSight.DSWindow
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
        'Get application's window handle, visibility, and state
        Debug.Print ("Application window using Application object:")
        Debug.Print ("  Window handle: " & dsApp.GetHWnd)
        Debug.Print ("  Visible:       " & dsApp.Visible)
        Debug.Print ("  State:         " & dsApp.WindowState)
```

```
        Debug.Print ("")
```

```
        'Get active document
        Set dsDoc = dsApp.GetActiveDocument
        If Not dsDoc Is Nothing Then
            ' Get application's window handle, visibility, and state
            Debug.Print ("Application window using DSWindow object:")
            Set dsAppWindow = dsApp.GetMainWindow
            Dim windowHandle As Long
            dsAppWindow.GetHWnd windowHandle
            Debug.Print ("  Window handle:     " & windowHandle)
            Debug.Print ("  Visible            " & dsAppWindow.Visible)
            Debug.Print ("  State:             " & dsAppWindow.WindowState)
            Dim x As Long
            Dim y As Long
            ' Get application's frame and geometry positions and sizes
            dsAppWindow.GetFramePosition x, y
            Debug.Print ("  Frame position:    " & x & ", " & y)
            dsAppWindow.GetFrameSize x, y
            Debug.Print ("  Frame size:        " & x & ", " & y)
            dsAppWindow.GetGeometryPosition x, y
            Debug.Print ("  Geometry position: " & x & ", " & y)
            dsAppWindow.GetGeometrySize x, y
            Debug.Print ("  Geometry size:     " & x & ", " & y)
```

```
            Debug.Print (" ")
```

```
            ' Get document's window handle, visibility, state,
            ' frame and geometry positions and sizes
            Debug.Print ("Document window using DSWindow object before minimizing window:")
            Set dsDocWindow = dsDoc.GetWindow()
            dsDocWindow.GetHWnd windowHandle
            Debug.Print ("  Window handle:     " & windowHandle)
            Debug.Print ("  Visible            " & dsDocWindow.Visible)
            Debug.Print ("  State:             " & dsDocWindow.WindowState)
            dsDocWindow.GetFramePosition x, y
            Debug.Print ("  Frame position:    " & x & ", " & y)
            dsDocWindow.GetFrameSize x, y
            Debug.Print ("  Frame size:        " & x & ", " & y)
            dsDocWindow.GetGeometryPosition x, y
            Debug.Print ("  Geometry position: " & x & ", " & y)
            dsDocWindow.GetGeometrySize x, y
            Debug.Print ("  Geometry size:     " & x & ", " & y)
```

```
            'Minimize Document window
            dsDocWindow.WindowState = 0
```

```
            Debug.Print ("")
            ' Get document's window handle, visibility, state,
            ' frame and geometry positions and sizes after minimizing
            ' window
            Debug.Print ("Document window using DSWindow object after minimizing the window:")
            Set dsDocWindow = dsDoc.GetWindow
            dsDocWindow.GetHWnd windowHandle
            Debug.Print ("  Window handle:     " & windowHandle)
            Debug.Print ("  Visible            " & dsDocWindow.Visible)
            Debug.Print ("  State:             " & dsDocWindow.WindowState)
            dsDocWindow.GetFramePosition x, y
            Debug.Print ("  Frame position:    " & x & ", " & y)
            dsDocWindow.GetFrameSize x, y
            Debug.Print ("  Frame size:        " & x & ", " & y)
            dsDocWindow.GetGeometryPosition x, y
            Debug.Print ("  Geometry position: " & x & ", " & y)
            dsDocWindow.GetGeometrySize x, y
            Debug.Print ("  Geometry size:     " & x & ", " & y)
```

```
        Else
            MsgBox ("There are no open documents in DraftSight.")
        End If
```

```
    End Sub
```
