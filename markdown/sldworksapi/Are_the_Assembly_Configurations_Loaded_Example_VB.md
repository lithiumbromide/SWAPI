---
title: "Are the Assembly Configurations Loaded Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Are_the_Assembly_Configurations_Loaded_Example_VB.htm"
---

# Are the Assembly Configurations Loaded Example (VBA)

This example shows how to find out if the configurations in an assembly are loaded, whether the configurations need to be updated and rebuilt, and the configuration types.

```
'------------------------------------------------------------
' Preconditions:
' 1. Verify that the assembly document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Loads al configurations.
' 2. Examine the Immediate window to see the states of the
'    configurations.
'
' NOTE: Because the assembly is used elsewhere, do not save
' changes.
'-----------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swConfiguration As SldWorks.Configuration
Dim swConfigurationMgr As SldWorks.ConfigurationManager
Dim vConfNameArr As Variant
Dim vConfName As Variant
Const sDocFilename As String = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\pdmworks\speaker.sldasm"
Dim boolstatus As Boolean
Dim nErrors As Long
Dim nWarnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    ' Open document; exit if it doesn't open
    Set swModel = swApp.OpenDoc6(sDocFilename, swDocASSEMBLY, swOpenDocOptions_Silent, "", nErrors, nWarnings)
    If swModel Is Nothing Then
        Exit Sub
    Else
        Debug.Print "File = " & swModel.GetPathName
        Debug.Print ""
    End If
```

```
    Set swConfigurationMgr = swModel.ConfigurationManager
    Set swConfiguration = swConfigurationMgr.ActiveConfiguration
    vConfNameArr = swModel.GetConfigurationNames
```

```
    Debug.Print "Traverse assembly without activating other configurations..."
    For Each vConfName In vConfNameArr
        Set swConfiguration = swModel.GetConfigurationByName(vConfName)
        Debug.Print "  Name of the configuration: " & swConfiguration.Name
        Debug.Print "    Is the configuration loaded? " & swConfiguration.IsLoaded
        Debug.Print "    Does the configuration need to be updated? " & swConfiguration.IsDirty
        Debug.Print "    Does the configuration need to be rebuilt? " & swConfiguration.NeedsRebuild
        Debug.Print "    What is the configuration type? " & swConfiguration.Type
    Next
```

```
    Debug.Print ""
```

```
    ' Traverse the assembly again, but this time activate all
    ' configurations, which loads them
    Debug.Print "Traverse assembly and activate all configurations..."
        For Each vConfName In vConfNameArr
        Set swConfiguration = swModel.GetConfigurationByName(vConfName)
        boolstatus = swModel.ShowConfiguration2(vConfName)
        Set swConfiguration = swConfigurationMgr.ActiveConfiguration
        Debug.Print "  Name of the configuration: " & swConfiguration.Name
        Debug.Print "    Is the configuration loaded? " & swConfiguration.IsLoaded
        Debug.Print "    Does the configuration need to be updated? " & swConfiguration.IsDirty
        Debug.Print "    Does the configuration need to be rebuilt? " & swConfiguration.NeedsRebuild
        Debug.Print "    What is the configuration type? " & swConfiguration.Type
    Next
```

```
End Sub
```
