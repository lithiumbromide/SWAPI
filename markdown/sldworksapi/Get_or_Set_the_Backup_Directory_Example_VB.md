---
title: "Get or Set the Backup Directory Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_or_Set_the_Backup_Directory_Example_VB.htm"
---

# Get or Set the Backup Directory Example (VBA)

This example shows how to set and get the backup directory.

```
'------------------------------------------------------------
' Preconditions:
' 1. Verify that c:\temp exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Sets c:\temp as the backup directory.
' 2. Gets the name of the backup directory.
' 3. Examine the Immediate window.
'-------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim backupDirectory As String
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    backupDirectory = "c:\temp"
    status = swApp.SetUserPreferenceStringValue(swUserPreferenceStringValue_e.swBackupDirectory, backupDirectory)
    backupDirectory = swApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swBackupDirectory)
    Debug.Print "Backup directory: " & backupDirectory
```

```
End Sub
```
