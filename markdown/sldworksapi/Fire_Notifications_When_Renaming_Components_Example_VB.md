---
title: "Fire Notifications When Renaming Components Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notifications_When_Renaming_Components_Example_VB.htm"
---

# Fire Notifications When Renaming Components Example (VBA)

This example shows how to fire notifications when you:

- are about to rename a component.
- rename a component.

```
'---------------------------------------------------
' Preconditions:
' 1. Copy and paste Main in the main module.
' 2. Click Insert > Class module and copy and paste Class1 in the class
'    module.
' 3. Verify that these documents exist in public_documents\samples\tutorial\api:
'    * beam_boltconnection.sldasm
'    * beam with holes.sldprt
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Open public_documents\samples\tutorial\api\beam_boltconnection.sldasm.
' 2. Fires pre-notification before appending
'    123 to each assembly component's name.
' 3. Fires notification when appending 123 to
'    each assembly component's name.
' 4. Examine the FeatureManager design tree and the
'    Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do
' not save changes.
'---------------------------------------------------
'Main
Option Explicit
```

```
Sub main()

    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swConfigMgr As SldWorks.ConfigurationManager
    Dim swConfig As SldWorks.Configuration
    Dim swRootComp  As SldWorks.Component2
    Dim Children As Variant
    Dim swChild As SldWorks.Component2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSelData As SldWorks.SelectData
    Dim swAssy As SldWorks.AssemblyDoc
    Dim swAssyEvents As Class1
    Dim ChildCount As Long
    Dim oldName As String
    Dim newName As String
    Dim bOldSetting As Boolean
    Dim bRet As Boolean
    Dim i As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swAssy = swModel
```

```
    'Set up events
    Set swAssy = swModel
    Set swAssyEvents = New Class1
    Set swAssyEvents.swAssy = swApp.ActiveDoc
```

```
    Set swConfigMgr = swModel.ConfigurationManager
    Set swConfig = swConfigMgr.ActiveConfiguration
    Set swRootComp = swConfig.GetRootComponent3(True)
    bOldSetting = swApp.GetUserPreferenceToggle(swExtRefUpdateCompNames)
    swApp.SetUserPreferenceToggle swExtRefUpdateCompNames, False
    Children = swRootComp.GetChildren
    ChildCount = UBound(Children)
    Set swSelMgr = swModel.SelectionManager
    Set swSelData = swSelMgr.CreateSelectData
    For i = 0 To ChildCount
        Set swChild = Children(i)
        ' Changing component name requires component to be selected
        bRet = swChild.Select4(False, swSelData, False)
        oldName = swChild.Name2
        newName = oldName & " 123"
        swChild.Name2 = newName
    Next i
    swApp.SetUserPreferenceToggle swExtRefUpdateCompNames, bOldSetting

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
Public WithEvents swAssy As SldWorks.AssemblyDoc
```

```
Private Function swAssy_PreRenameItemNotify(ByVal EntityType As Long, ByVal oldName As String, ByVal newName As String) As Long
    Debug.Print "PRE-NOTIFICATION - about to rename component: " & oldName
End Function
```

```
Private Function swAssy_RenameItemNotify(ByVal EntityType As Long, ByVal oldName As String, ByVal newName As String) As Long
    Debug.Print "NOTIFICATION - rename component: " & newName
End Function
```

```
Back to top
```
