---
title: "ExitApp Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ExitApp"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ExitApp.html"
---

# ExitApp Method (ISldWorks)

Shuts down SOLIDWORKS Design.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ExitApp()
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks

instance.ExitApp()
```

### C#

```csharp
void ExitApp()
```

### C++/CLI

```cpp
void ExitApp();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [SldWorks::ExitApp](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~ExitApp.html).

## Remarks

This method is not normally used with macros (*.swp) because it shuts down your SOLIDWORKS Design session.

For C++ and Visual Basic projects, ending your program does not guarantee that the SLDWORKS processes are closed. During development, you can determine whether processes are left running by checking the Process Viewer and looking for any SLDWORKS processes. Typically, you do not want the SLDWORKS process running after your program has ended. Calling this method ensures that no SLDWORKS processes are left running when your program ends.

However, the CreateObject ("SldWorks.Application") statement used to start up the SOLIDWORKS Design software either creates a new SOLIDWORKS Design session or it attaches to an existing SOLIDWORKS Design session. If the end-user currently has an open SOLIDWORKS Design session, then your program attaches to it. Performing this method ends that session.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
