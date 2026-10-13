---
title: "Undo Feature and Fire Undo Post-Notify Event Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Undo_Feature_and_Fire_Undo_Post-Notify_Event_Example_VB.htm"
---

# Undo Feature and Fire Undo Post-Notify Event Example (VBA)

This example shows how to fire an undo post-notification in a part.

```
'--------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\cstick.sldprt.
' 2. Copy and paste Main in the main module.
' 3. Click Insert > Class Module and copy and paste Class1 into that module.
'
' Postconditions:
' 1. Creates a cut-extrude feature on the top face of the
'    candlestick.
' 2. Undoes the cut-extrude feature and fires an undo post-notification.
' 3. Click OK to close the message box.
' 4. Deletes the cut-extrude sketch and all absorbed features.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'--------------------------------------------------------------------------
'Main
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swPart As SldWorks.PartDoc
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchManager As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swFeatureManager As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim boolstatus As Boolean
Dim swPartEvents As Class1
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    ' Event notification
    Set swPart = swModel
    Set swPartEvents = New Class1
    Set swPartEvents.swPart = swApp.ActiveDoc
```

```
    ' Create a cut-extrude feature on the
    ' top face of the candlestick
    Set swModelDocExt = swModel.Extension
    boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.00140404215739, 0.2199999999999, 0.001897848026772, False, 0, Nothing, 0)
    Set swSketchManager = swModel.SketchManager
    Set swSketchSegment = swSketchManager.CreateCircle(0#, 0#, 0#, 0.01296, -0.006347, 0#)
    swModel.ClearSelection2 True
    boolstatus = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeatureManager = swModel.FeatureManager
    Set swFeature = swFeatureManager.FeatureCut(True, False, False, 0, 0, 0.01, 0.01, False, False, False, False, 0.01745329251994, 0.01745329251994, False, False, False, False, False, True, True)
    swModel.ClearSelection2 True
```

```
    ' Undo the cut-extrude feature
    swModel.EditUndo2 1
```

```
    ' Fire undo event
```

```
    ' Select the circle and delete it
    boolstatus = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
    boolstatus = swModelDocExt.DeleteSelection2(swDelete_Absorbed)
```

```
    swModel.ForceRebuild3 True
```

```
End Sub
```

```
Back to top
```

```
'Class1
Option Explicit
```

```
Public WithEvents swPart As SldWorks.PartDoc
```

```
Private Function swPart_UndoPostNotify() As Long
    'Show message after an undo action occurs
    MsgBox "An undo post-notification event has been fired."
End Function
```

```
Back to top
```
