---
title: "Get Mass Properties of Inactive Document Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mass_Properties_of_Inactive_Document_Example_VB.htm"
---

# Get Mass Properties of Inactive Document Example (VBA)

This example shows how to get the mass properties from a closed (i.e., inactive) assembly document.

```
'--------------------------------------------------------
' Preconditions:
' 1. Copy the files in public_documents\samples\tutorial\motionstudies
'    to c:\temp\motionstudies.
' 2. Open c:\temp\motionstudies\valve_cam.sldasm, click Tools > Options >
'    System Options > Performance > Update mass properties while saving
'    document > OK.
' 3. Click File > Save.
' 4. Click File > Close.
' 5. Open the Immediate window.
'
' Postconditions:
' 1. Gets the mass properties.
' 2. Examine the Immediate window.
'--------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Const sFileName As String = "c:\temp\motionstudies\valve_cam.sldasm"
    Const sConfigName As String = "Default"
    Dim swApp As SldWorks.SldWorks
    Dim vMassProp As Variant
```

```
    Set swApp = CreateObject("SldWorks.Application")
```

```
    vMassProp = swApp.GetMassProperties2(sFileName, sConfigName, 1)
    Debug.Print "SldWorks::GetMassProperties2(" + sFileName + " [" + sConfigName + "])"
    Debug.Print "  UpdateMassPropsDuringSave = " & swApp.GetUserPreferenceToggle(swUpdateMassPropsDuringSave)
    Debug.Print ""
    If Not IsEmpty(vMassProp) Then
        Debug.Print "  CenterOfMassX = " & vMassProp(0)
        Debug.Print "  CenterOfMassY = " & vMassProp(1)
        Debug.Print "  CenterOfMassZ = " & vMassProp(2)
        Debug.Print "  Volume = " & vMassProp(3)
        Debug.Print "  Area   = " & vMassProp(4)
        Debug.Print "  Mass   = " & vMassProp(5)
        Debug.Print "  MomXX = " & vMassProp(6)
        Debug.Print "  MomYY = " & vMassProp(7)
        Debug.Print "  MomZZ = " & vMassProp(8)
        Debug.Print "  MomXY = " & vMassProp(9)
        Debug.Print "  MomZX = " & vMassProp(10)
        Debug.Print "  MomYZ = " & vMassProp(11)
    End If
```

```
End Sub
```
