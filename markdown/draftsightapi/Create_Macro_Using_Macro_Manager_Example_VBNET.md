---
title: "Create Macro Using Macro Manager Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Macro_Using_Macro_Manager_Example_VBNET.htm"
---

# Create Macro Using Macro Manager Example (VB.NET)

This example shows how to create a C++COM macro using the macro manager and VB.NET.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Add a reference to System.Windows.Forms.
' 5. Create C:\temp\macros, if this folder does not exist.
' 6. Start DraftSight.
' 7. Press F5.
'
' Postconditions:
' 1. Connects to DraftSight.
' 2. Gets the active document.
' 3. Gets the macro manager.
' 4. Sets the macro language, level of detail, and path
'    where to save the macro.
' 5. Starts macro recording.
' 6. Creates a Visual Studio 2008 C++ COM project containing the
'    macro at c:\temp\macros\CircleMacroCPPCOM and inserts
'    a Circle and Arc in the drawing.
' 7. Stops macro recording.
' 8. Open a new drawing in DraftSight.
' 9. Open C:\temp\macros\CircleMacroSharp\CircleMacroCPPCOM.csproj in
'    Visual Studio 2008.
'    a. Expand CircleMacroCPPCOM, if necessary.
'    b. Expand DSAPIMacros, if necessary.
'    c. Double-click CircleMacroCPPCOM located below DSAPIMacros, which opens
'       CircleMacroCPPCOM.cs.
'    d. Click Start Debugging.
'    e. Creates a Circle and Arc in the drawing.
'    f. Click File > Save All and save the solution.
'    g. Click File > Close Solution.
'----------------------------------------------

Imports System
Imports DraftSight.Interop.dsAutomation
Imports System.Runtime.InteropServices
Imports System.Windows.Forms

Module Module1

    Sub Main()

        Dim dsApp As DraftSight.Interop.dsAutomation.Application

        'Connect to DraftSight application
        dsApp = GetObject(, "DraftSight.Application")

        If dsApp Is Nothing Then
            Return
        End If

        'Abort any command currently running in DraftSight
        'to avoid nested commands
        dsApp.AbortRunningCommand()

        'Get active document
        Dim dsDoc As Document = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MessageBox.Show("There are no open documents in DraftSight.")
            Return
        End If

        'Get macro manager
        Dim dsMacroManager As MacroManager = dsApp.GetMacroManager()

        'Set macro language
        dsMacroManager.Language = dsMacroLanguage_e.dsMacroLanguage_CSharp

        'Set macro level of detail
        dsMacroManager.LevelOfDetail = dsMacroLevelOfDetail_e.dsMacroLevelOfDetail_Low

        'Set save file path
        dsMacroManager.SavePath = "C:\temp\macros\"

        'Start macro recording
        dsMacroManager.StartMacroRecording()

        'Get Sketch Manager
        Dim dsSketchMgr As SketchManager = dsDoc.GetModel().GetSketchManager()

        'Insert Circle and Arc
        Dim dsCircle As Circle = dsSketchMgr.InsertCircle(2.0, 2.0, 0.0, 4.0)

        Dim dsCircleArc As CircleArc = dsSketchMgr.InsertArc(3.0, 3.0, 0.0, 4.0, 1.0, 2.0)

        'Stop macro recoding
        dsMacroManager.StopMacroRecording("CircleMacroCPPCOM")
    End Sub

End Module
```
