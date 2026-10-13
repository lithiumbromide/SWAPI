---
title: "Extract Configuration-specific Parameters Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Extract_Configuration-Specific_Parameters_Example_VB.htm"
---

# Extract Configuration-specific Parameters Example (VBA)

This example shows how to extract and list all configuration-specific parameters from a model.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open a part or assembly.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets configuration properties for each of the configurations
'    in the part or assembly.
' 2. Examine the Immediate window.
'
' NOTE: All parameters and their values are returned as strings.
' It is up to the application to interpret the meaning of
' each parameter and perform the appropriate conversion.
'-----------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swConfigMgr As SldWorks.ConfigurationManager
    Dim vConfName As Variant
    Dim vConfParam As Variant
    Dim vConfValue As Variant
    Dim i As Long
    Dim j As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swConfigMgr = swModel.ConfigurationManager
    Debug.Print "File = " + swModel.GetPathName
```

```
    vConfName = swModel.GetConfigurationNames
    For i = 0 To UBound(vConfName)
        bRet = swConfigMgr.GetConfigurationParams(vConfName(i), vConfParam, vConfValue)
        Debug.Assert bRet
        Debug.Print "  Configuration = " & vConfName(i)
        If Not IsEmpty(vConfParam) Then
            For j = 0 To UBound(vConfParam)
                Debug.Print "    " & vConfParam(j) & " = " & vConfValue(j)
            Next j
        End If
    Next i
```

```
End Sub
```
