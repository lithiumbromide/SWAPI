---
title: "Create SpeedPak for Subassemblies Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_SpeedPak_for_Subassemblies_Example_VB.htm"
---

# Create SpeedPak for Subassemblies Example (VBA)

This example shows how to:

- create SpeedPak configurations for subassemblies.
- switch between the SpeedPak configuration and the parent configuration of the SpeedPak configuration.

```
'-------------------------------------------------------------------
' Preconditions:
'  1. Verify that the specified assembly to open exists.
'  2. Open the Immediate window.
'
' Postconditions:
'  1. Opens the specified assembly.
'  2. Deletes the Coordinate System1 feature to avoid errors.
'  3. Selects the arm1 and arm2 subassemblies.
'  4. Checks to see if either component has a SpeedPak configuration.
'  5. Creates graphics-only SpeedPak for each selected component.
'  6. At Stop, examine the FeatureManager design tree to verify that the
'     icons for arm1 and arm2 indicate SpeedPak, then press F5.
'  7. Switches SpeedPak to each selected component's parent configuration.
'  8. At Stop, examine the FeatureManager design tree to verify that
'     SpeedPak switched to the parent configuration of arm1 and
'     arm2, then press F5.
'  9. Switches each component back to SpeedPak.
' 10. Examine the Immediate window and FeatureManager design tree to verify
'     that arm1 and arm2 are SpeedPak.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'--------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swAssembly As SldWorks.AssemblyDoc
Dim swSelMgr As SldWorks.SelectionMgr
Dim swComponent As SldWorks.Component2
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
Dim selComponents(1) As Object
Dim i As Long
Dim count As Long
Dim speedPakExists As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\wrench.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swAssembly = swModel
    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
```

```
    'Select and delete Coordinate System1 to avoid errors
    status = swModelDocExt.SelectByID2("Coordinate System1", "COORDSYS", 0, 0, 0, False, 0, Nothing, 0)
    swModel.EditDelete
```

```
    'Select the two subassemblies for which to create SpeedPak configurations
    status = swModelDocExt.SelectByID2("arm1-1@wrench", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    Set selComponents(0) = swSelMgr.GetSelectedObject6(1, -1)
    status = swModelDocExt.SelectByID2("arm2-1@wrench", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
    Set selComponents(1) = swSelMgr.GetSelectedObject6(2, -1)
    count = swSelMgr.GetSelectedObjectCount2(-1)
```

```
    'Get whether any of the selected components already
    'have SpeedPak configurations
     For i = 0 To count - 1
        Set swComponent = selComponents(i)
        speedPakExists = swComponent.IsSpeedPak
        If (speedPakExists) Then
             Debug.Print ("SpeedPak already exists for component(" & i & ")")
        End If
    Next
```

```
    'Create graphics-only SpeedPak for the selected components
    status = swAssembly.CreateSpeedPak(2)
    Debug.Print ("SpeedPak created for selected components? " & status)

    Stop
    'Examine the FeatureManager design tree to verify that the
    'icons for arm1 and arm2 indicate SpeedPak, then press F5
```

```
    'Switch SpeedPak to the parent configurations of each selected components
    status = swModelDocExt.SelectByID2("arm1-1@wrench", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("arm2-1@wrench", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
    status = swAssembly.SetSpeedPakToParent
    Debug.Print ("SpeedPak switched to the parent configuration of each selected component? " & status)
```

```
    Stop
    'Examine the FeatureManager design tree to verify
    'that SpeedPak switched to the parent configurations of arm1 and
    'arm2
```

```
    'Switch the selected components to SpeedPak
    status = swModelDocExt.SelectByID2("arm1-1@wrench", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("arm2-1@wrench", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
    status = swAssembly.UseSpeedPak
    Debug.Print ("Switched the selected components to SpeedPak? " & status)
```

```
End Sub
```
