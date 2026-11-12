---
title: "Get Build Numbers Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Build_Numbers_Example_VB.htm"
---

# Get Build Numbers Example (VBA)

This example shows how to get the build, major revision, and hot fix numbers of the SOLIDWORKS Design application.

```vb
'------------------------------------------------------------
 ' Preconditions: Open SOLIDWORKS Design.
 '
 ' Postconditions: Inspect the Immediate window for build,
 ' major revision, and hot fix numbers.
 '-----------------------------------------------------------
```

```
Dim swApp As SldWorks.SldWorks
Dim BaseVersion As String
Dim CurrentVersion As String
Dim HotFixes As String
```

```
Option Explicit
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    swApp.GetBuildNumbers2 BaseVersion, CurrentVersion, HotFixes
    Debug.Print "SOLIDWORKS major revision number: " & BaseVersion
    Debug.Print "SOLIDWORKS build number: " & CurrentVersion
    Debug.Print "SOLIDWORKS hot fix numbers: " & HotFixes
```

```
End Sub
```
