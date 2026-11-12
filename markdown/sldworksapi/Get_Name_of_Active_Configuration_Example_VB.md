---
title: "Get Name of Active Configuration Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Name_of_Active_Configuration_Example_VB.htm"
---

# Get Name of Active Configuration Example (VBA)

This example shows how to get the name of the configuration active when the the specified SOLIDWORKS Design document was last closed.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Prints to the Immediate the name of the configuration
'    active when the the part document was last closed.
' 2. Examine the Immediate window.
'-----------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Const sFileName As String = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\fillets\knob.sldprt"
    Dim swApp As SldWorks.SldWorks
```

```
    Set swApp = Application.SldWorks
    Debug.Print "File = " & sFileName
    Debug.Print "  Name of active configuration = " & swApp.GetActiveConfigurationName(sFileName)
```

```
End Sub
```
