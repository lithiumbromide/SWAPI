---
title: "Load and Activate LineStyles Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Laod_and_Activate_LineStyles_Example_VBNET.htm"
---

# Load and Activate LineStyles Example (VB.NET)

This example shows how to load and activate LineStyles.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Add references to System and System.Windows.Forms.
' 5. Start DraftSight and open a document.
' 6. Start debugging the project.
'
' Postconditions:
' 1. Gets the active document.
' 2. Gets the LineStyle Manager.
' 3. Loads the BATTING and ZIGAG LineStyles.
' 4. Activates and draws a Line for each LineStyle
'    loaded in Step 3.
'----------------------------------------------------------------

Imports DraftSight.Interop.dsAutomation
Imports System.Runtime.InteropServices
Imports System.Windows.Forms
Imports System

Module Module1

    Sub Main()

        Dim dsApp As DraftSight.Interop.dsAutomation.Application

        'Connect to DraftSight application
        dsApp = DirectCast(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)

        ' Abort any command currently running in DraftSight to avoid nested commands
        dsApp.AbortRunningCommand()

        If dsApp Is Nothing Then
            Return
        End If

        'Get active document
        Dim dsDoc As Document = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MessageBox.Show("There are no open documents in DraftSight.")
            Return
        End If

        'Get LineStyle manager
        Dim dsLineStyleMgr As LineStyleManager = dsDoc.GetLineStyleManager()

        'Load LineStyles
        Dim lineStyleFilePath As String = System.IO.Path.Combine(dsApp.GetSystemFiles().GetUserDataPath(), "Linestyles")
        Dim lineStyleFile As String = System.IO.Path.Combine(lineStyleFilePath, "MM.LIN")
        Dim dsLineStyle As LineStyle = Nothing
        dsLineStyleMgr.LoadLineStyle("BATTING", lineStyleFile, dsLineStyle)
        dsLineStyleMgr.LoadLineStyle("ZIGZAG", lineStyleFile, dsLineStyle)

        'Get Sketch manager
        Dim dsSketchMgr As SketchManager = dsDoc.GetModel().GetSketchManager()

        'Activate BATTING LineStyle and insert Line
        dsLineStyle = dsLineStyleMgr.GetLineStyle("BATTING")
        dsLineStyle.Activate()
        dsSketchMgr.InsertLine(0, 0, 0, 100, 100, 0)

        'Activate ZIGZAG LineStyle and insert Line
        dsLineStyle = dsLineStyleMgr.GetLineStyle("ZIGZAG")
        dsLineStyle.Activate()
        dsSketchMgr.InsertLine(100, 0, 0, 200, 100, 0)
    End Sub

End Module
```
