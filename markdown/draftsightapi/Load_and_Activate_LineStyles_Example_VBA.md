---
title: "Load and Activate LineStyles Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Load_and_Activate_LineStyles_Example_VBA.htm"
---

# Load and Activate LineStyles Example (VBA)

This example shows how to load and activate LineStyles.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight and open a document.
' 5. Start debugging the project.
'
' Postconditions:
' 1. Gets the active document.
' 2. Gets the LineStyle Manager.
' 3. Loads the BATTING and ZIGAG LineStyles.
' 4. Activates and draws a Line for each LineStyle
'    loaded in Step 3.
'----------------------------------------------------------------
Option Explicit
```

```
   Sub main()
```

```
        Dim dsApp As DraftSight.Application
```

```
        'Connect to DraftSight application
        Set dsApp = GetObject(, "DraftSight.Application")
```

```
        'Abort any command currently running in DraftSight
        'to avoid nested commands
        dsApp.AbortRunningCommand
```

```
        If dsApp Is Nothing Then
            Return
        End If
```

```
        'Get active document
        Dim dsDoc As DraftSight.Document
        Set dsDoc = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MsgBox ("There are no open documents in DraftSight.")
            Return
        End If
```

```
        'Get LineStyle manager
        Dim dsLineStyleMgr As DraftSight.LineStyleManager
        Set dsLineStyleMgr = dsDoc.GetLineStyleManager()
```

```
        'Load LineStyles
        Dim lineStyleFile As String
        lineStyleFile = "c:\Program Files\Dassault Systemes\DraftSight\Default Files\Linestyles\MM.LIN"
        Dim dsLineStyle As DraftSight.LineStyle
        dsLineStyleMgr.LoadLineStyle "BATTING", lineStyleFile, dsLineStyle
        dsLineStyleMgr.LoadLineStyle "ZIGZAG", lineStyleFile, dsLineStyle
```

```
        'Get Sketch manager
        Dim dsSketchMgr As DraftSight.SketchManager
        Set dsSketchMgr = dsDoc.GetModel().GetSketchManager()
```

```
        'Activate BATTING LineStyle and insert Line
        Set dsLineStyle = dsLineStyleMgr.GetLineStyle("BATTING")
        dsLineStyle.Activate
        dsSketchMgr.InsertLine 0, 0, 0, 100, 100, 0
```

```
        'Activate ZIGZAG LineStyle and insert Line
        Set dsLineStyle = dsLineStyleMgr.GetLineStyle("ZIGZAG")
        dsLineStyle.Activate
        dsSketchMgr.InsertLine 100, 0, 0, 200, 100, 0
```

```
   End Sub
```
