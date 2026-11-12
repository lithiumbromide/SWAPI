---
title: "Run SOLIDWORKS Commands and Synthesize Mouse Events Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Run_SolidWorks_Commands_and_Synthesize_Mouse_Events_Example_VBNET.htm"
---

# Run SOLIDWORKS Commands and Synthesize Mouse Events Example (VB.NET)

This example shows how to run SOLIDWORKS commands and synthesize mouse events.

```
'-----------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document to open exists.
' 2. Click Tools > Options and click to clear the Stop VSTA debugger
'    on macro exit check box, if it is selected.
' 3. In the IDE, right-click the project name in the Project Explorer,
'    click Add Reference, browse install_dir\api\redist, click
'    SolidWorks.Interop.swcommands.dll, and click OK.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Fits the model to the graphics area.
' 3. Moves the mouse.
' 4. Changes the view orientation to *Front.
' 5. Select an edge on the model.
' 6. Left-click anywhere outside the model in the graphics area.
' 7. Examine the Immediate window.
' 8. Click Stop Debugging in the IDE.
' 9. Click Tools > Options and click to select the Stop VSTA debugger
'    on macro exit check box, if it is clear.
'-----------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.swcommands
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public WithEvents msMouse As Mouse

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swModelView As ModelView
        Dim TheMouse As Mouse
        Dim i As Integer
        Dim x As Double
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer
        Dim status As Boolean

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block20.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        swModelView = swModel.GetFirstModelView
        TheMouse = swModelView.GetMouse

        'Set up events
        msMouse = TheMouse
        AttachEventHandlers()

        x = 0

        Debug.Print("Fit model to graphics area")
        swModelDocExt.RunCommand(swCommands_e.swCommands_ZoomToFit, "")

        'Move the mouse
        status = TheMouse.Move(50, 150, swMouse_e.swMouse_Absolute + swMouse_e.swMouse_MouseMove + swMouse_e.swMouse_LeftDown)
        Debug.Print("First call to Move: " & status)
        Debug.Print("Calls to Move within loop:")
        For i = 1 To 5
            status = TheMouse.Move(5, 5, swMouse_e.swMouse_MouseMove)
            Debug.Print("  Call " & i & " to Move: " & status)
        Next
        status = TheMouse.Move(0, 0, swMouse_e.swMouse_LeftUp)
        Debug.Print("Last call to Move: " & status)

        status = TheMouse.MoveXYZ(0.03720615681732, 0.0316583060694, 0.04991700841805, swMouse_e.swMouse_LeftDown)
        Debug.Print("Call to MoveXYZ: " & status)
        Debug.Print("Calls to Move within next loop:")
        For i = 1 To 5
            status = TheMouse.Move(5, 5, swMouse_e.swMouse_MouseMove)
            Debug.Print("  Call " & (i + 1).ToString & " to Move: " & status)
        Next

        status = TheMouse.Move(10, 10, swMouse_e.swMouse_LeftUp)
        Debug.Print("Last call to Move: " & status)

        Debug.Print("Change view to *Front")
        swModelDocExt.RunCommand(swCommands_e.swCommands_Front, "")

    End Sub

    Sub AttachEventHandlers()
        AttachSWEvents()
    End Sub

    Sub AttachSWEvents()

        AddHandler msMouse.MouseSelectNotify, AddressOf Me.ms_MouseSelectNotify
        AddHandler msMouse.MouseLBtnDownNotify, AddressOf Me.ms_MouseLBtnDownNotify

    End Sub

    Private Function ms_MouseSelectNotify(ByVal Ix As Integer, ByVal Iy As Integer, ByVal x As Double, ByVal y As Double, ByVal z As Double) As Integer
        Debug.Print("Selection made:")
        Debug.Print(" Mouse location:")
        Debug.Print("   Window space coordinates:")
        Debug.Print("     " & Ix)
        Debug.Print("     " & Iy)
        Debug.Print("   World space coordinates:")
        Debug.Print("     " & x)
        Debug.Print("     " & y)
        Debug.Print("     " & z)
    End Function

    Private Function ms_MouseLBtnDownNotify(ByVal x As Integer, ByVal y As Integer, ByVal WParam As Integer) As Integer
        Debug.Print("Left-mouse button pressed.")
    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
