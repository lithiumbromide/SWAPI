---
title: "Reorganize Components Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Reorganize_Components_Example_VB.htm"
---

# Reorganize Components Example (VBA)

This example shows how to reorder components in an assembly.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Copy and paste this code in the main module.
' 2. Click Insert > Class module and copy and paste this code in that module.
' 3. Open public_documents\samples\tutorial\assemblyvisualize\food_processor.sldasm.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Run the macro.
' 2. Interactively select both shaft washer components in the FeatureManager design tree.
' 3. Press F5.
' 4. Interactively select the blade shaft subassembly in the FeatureManager design tree.
' 5. Press F5.
' 6. Expand and examine the blade shaft subassembly in the FeatureManager design tree to verify
'    that both shaft washer components moved to the subassembly.
' 7. Examine the Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
' ----------------------------------------------------------------------------
```

```
'Module
Option Explicit
```

```
Dim myClass As Class1
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim myModel As SldWorks.ModelDoc2
    Dim myAssem As SldWorks.AssemblyDoc
    Dim selMgr As SldWorks.SelectionMgr
    Dim selCount As Long, selType As Long
    Dim selObj As Object
    Dim selSource() As SldWorks.Component2
    Dim vSource As Variant
    Dim selTarget As SldWorks.Component2
    Dim boolstatus As Boolean
```

```
    Set swApp = Application.SldWorks
    Set myModel = swApp.ActiveDoc
    Set myAssem = myModel
```

```
    Set myClass = New Class1
    Set myClass.msrcAssemblyDoc = myAssem
```

```
    ' Interactively select components to move
    ' The selected components must be from the
    ' same level of an assembly
    ' Press F5
    Stop
```

```
    Set selMgr = myModel.SelectionManager
    selCount = selMgr.GetSelectedObjectCount2(0)
    If (selCount = 0) Then
        Exit Sub
    End If
```

```
    ReDim selSource(0 To selCount - 1)
    Dim i As Long
    For i = 1 To selCount
        selType = selMgr.GetSelectedObjectType3(i, 0)
        If (selType = SwConst.swSelCOMPONENTS) Then
            Set selObj = selMgr.GetSelectedObject6(i, 0)
            Set selSource(i - 1) = selObj
        End If
    Next i
```

```
    vSource = selSource
```

```
    myModel.ClearSelection2 True
```

```
    ' Interactively select a top-level assembly or
    ' sub-assembly where to move the
    ' previously selected components
    ' Press F5
    Stop
```

```
    selCount = selMgr.GetSelectedObjectCount2(0)
    If (selCount > 0) Then
        selType = selMgr.GetSelectedObjectType3(1, 0)
        If selType = SwConst.swSelCOMPONENTS Then
            Set selObj = selMgr.GetSelectedObject6(1, 0)
            If Not selObj Is Nothing Then
                Set selTarget = selObj
            Else
                Set selTarget = myAssem.GetEditTargetComponent
            End If
        End If
    End If
```

```
    myModel.ClearSelection2 True
```

```
    If Not (selTarget Is Nothing) Then
        boolstatus = myAssem.ReorganizeComponents((vSource), selTarget)
        ' AssemblyDoc ComponentReorganizeNotify event is fired
        If boolstatus = False Then
            Debug.Print "Reordering components failed."
        Else
            Debug.Print "Reordering components succeeded."
        End If
    End If
```

```
End Sub
```

[Back to top](#top)

'Class1
Option Explicit

```
Public WithEvents msrcAssemblyDoc   As SldWorks.AssemblyDoc
Public Function msrcAssemblyDoc_ComponentReorganizeNotify(ByVal sourceName As String, ByVal targetName As String) As Long
    Debug.Print "IAssemblyDocEvent ComponentReorganizeNotify"
    Debug.Print "  Source component is: " & sourceName
    Debug.Print "  Target component is: " & targetName
    msrcAssemblyDoc_ComponentReorganizeNotify = 1
End Function
```

[Back to top](#top)
