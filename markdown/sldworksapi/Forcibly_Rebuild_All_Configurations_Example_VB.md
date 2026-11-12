---
title: "Forcibly Rebuild All Configurations Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Forcibly_Rebuild_All_Configurations_Example_VB.htm"
---

# Forcibly Rebuild All Configurations Example (VBA)

This example shows how to forcibly rebuild all of the configurations in a SOLIDWORKS Design part or assembly document.

```
'-----------------------------------------------------
' Postconditions:
' 1. Open a part or assembly.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Rebuilds each configuration in the the part or
'    assembly.
' 2. Examine the Immediate window.
'-----------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim vConfNameArr As Variant
    Dim sConfigName As String
    Dim start As Single
    Dim i As Long
    Dim bShowConfig As Boolean
    Dim bRebuild As Boolean
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
```

```
    Debug.Print "File = " + swModel.GetPathName
```

```
    vConfNameArr = swModel.GetConfigurationNames
    For i = 0 To UBound(vConfNameArr)
        sConfigName = vConfNameArr(i)
        bShowConfig = swModel.ShowConfiguration2(sConfigName)
        start = Timer
        bRebuild = swModel.ForceRebuild3(False)
        Debug.Print "  Configuration = " & sConfigName
        Debug.Print "    ShowConfig  = " & bShowConfig
        Debug.Print "    Rebuild     = " & bRebuild
        Debug.Print "    Time        = " & Timer - start & " seconds"
    Next i
```

```
End Sub
```
