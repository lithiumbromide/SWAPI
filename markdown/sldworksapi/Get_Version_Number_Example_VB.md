---
title: "Get Version Number Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Version_Number_Example_VB.htm"
---

# Get Version Number Example (VBA)

This example shows how to get the version number of SOLIDWORKS Design.

```
'-----------------------------------
' Preconditions: Open the Immediate window.
'
' Postconditions: Examine the Immediate
' window.
'------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim BaseVersion As String
Dim CurrentVersion As String
Dim HotFixes As String
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
Debug.Print "Version = " & swApp.RevisionNumber
swApp.GetBuildNumbers2 BaseVersion, CurrentVersion, HotFixes
Debug.Print "Major revision number: " & BaseVersion
Debug.Print "Build number: " & CurrentVersion
Debug.Print "Hot fix numbers: " & HotFixes
```

```
End Sub
```
