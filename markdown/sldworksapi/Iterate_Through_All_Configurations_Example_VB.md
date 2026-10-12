---
title: "Iterate Through All Configurations Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Iterate_Through_All_Configurations_Example_VB.htm"
---

# Iterate Through All Configurations Example (VBA)

This example shows how to iterate through all of the configurations in a document and forcibly rebuild each one.

```
'--------------------------------------
' Preconditions:
' 1. Open a part or assembly.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Iterates through all configurations.
' 2. Examine the Immediate window.
'---------------------------------------------------------
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
    Dim nStart As Single
    Dim i As Long
    Dim bShowConfig As Boolean
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
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
        nStart = Timer
        bRebuild = swModel.ForceRebuild3(False)
        Debug.Print "  Configuration = " & sConfigName
        Debug.Print "    Configuration shown? " & bShowConfig
        Debug.Print "    Configuration rebuilt? " & bRebuild
        Debug.Print "    Execution time for this configuration = " & Timer - nStart & " seconds"
    Next i
```

```
End Sub
```
