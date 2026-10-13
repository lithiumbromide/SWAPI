---
title: "Fire Notification After Adding a Mate Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_After_Adding_a_Mate_Example_VB.htm"
---

# Fire Notification After Adding a Mate Example (VBA)

This example shows how to fire a post-notify event when adding mates:

```
'----------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly to open exists.
' 2. Copy Main to the main module.
' 3. Click Insert > Class Module and copy Class to that
'    module.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Opens the assembly.
' 2. Interactively add a mate between two entities
'    (click Insert > Mate). For example, add a lock mate
'    between the toaster base and the cup.
' 3. Adds a mate between the selected entities.
' 4. Examine the Immediate window.
'
' NOTE: Because this assembly is used elsewhere, do not save
' changes.
'----------------------------------------------------------
'Main
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swAssemblyDoc As SldWorks.AssemblyDoc
Dim errorstatus As Long, warningstatus As Long
Dim swAssemblyDocEvents As Class1
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    swApp.OpenDoc6 "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\toaster_scene.sldasm", swDocASSEMBLY, swOpenDocOptions_Silent, "", errorstatus, warningstatus
    Set swModel = swApp.ActiveDoc
    Set swAssemblyDoc = swModel
```

```
    ' Set up event
    Set swAssemblyDocEvents = New Class1
    Set swAssemblyDocEvents.swAssemblyDoc = swApp.ActiveDoc
```

```
End Sub
```

###### 'Class

```vb
Option Explicit

Public WithEvents swAssemblyDoc As SldWorks.AssemblyDoc

 Private Function swAssemblyDoc_AddMatePostNotify2(mates As Variant) As Long
     Debug.Print "One or more mates were added to the assembly."

    Dim mate As Mate2
     Dim i As Integer
     For i = 0 To UBound(mates)
         Set mate = mates(i)
        Debug.Print "Type of mate added as defined in swMateType_e: " & mate.Type
     Next i

 End Function
```
