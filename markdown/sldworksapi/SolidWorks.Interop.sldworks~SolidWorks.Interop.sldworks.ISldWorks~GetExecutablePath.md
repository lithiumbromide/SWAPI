---
title: "GetExecutablePath Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetExecutablePath"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetExecutablePath.html"
---

# GetExecutablePath Method (ISldWorks)

Gets the path to the SOLIDWORKS Design executable, sldworks.exe.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExecutablePath() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.String

value = instance.GetExecutablePath()
```

### C#

```csharp
System.string GetExecutablePath()
```

### C++/CLI

```cpp
System.String^ GetExecutablePath();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Path for **sldworks.exe**

## VBA Syntax

See [SldWorks::GetExecutablePath](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetExecutablePath.html).

## Examples

This subroutine illustrates how to use this method:

```vb
'---------------------------------------------
Option Explicit

Sub main()
    Dim swApp As SldWorks.SldWorks

    Set swApp = Application.SldWorks

    ' Gives directory name without trailing backslash
    Debug.Print "SldWorks Design executable = " & swApp.GetExecutablePath
End Sub
'---------------------------------------------
```

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetCurrentMacroPathFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathFolder.html)
[ISldWorks::GetCurrentWorkingDirectory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentWorkingDirectory.html)
[ISldWorks::GetDataFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDataFolder.html)

## Availability

SOLIDWORKS 2003 SP3, Revision Number 11.3
