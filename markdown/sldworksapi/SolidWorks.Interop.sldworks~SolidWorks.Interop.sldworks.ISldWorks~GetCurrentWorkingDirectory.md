---
title: "GetCurrentWorkingDirectory Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetCurrentWorkingDirectory"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentWorkingDirectory.html"
---

# GetCurrentWorkingDirectory Method (ISldWorks)

Gets the current working directory being used by the SOLIDWORKS Design application.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurrentWorkingDirectory() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.String

value = instance.GetCurrentWorkingDirectory()
```

### C#

```csharp
System.string GetCurrentWorkingDirectory()
```

### C++/CLI

```cpp
System.String^ GetCurrentWorkingDirectory();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Current working directory with trailing backslash

## VBA Syntax

See [SldWorks::GetCurrentWorkingDirectory](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetCurrentWorkingDirectory.html).

## Remarks

The current working directory is used when opening documents containing references. If explicit search folders are not set (see [ISldWorks::SetSearchFolders](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetSearchFolders.html)), then the SOLIDWORKS Design application initially tries to locate file references (for example, assembly component parts) in the current working directory. Interactively, the current working directory is used by the File Open dialog and is set when you choose the Open dialog button.

The most current [ISldWorks::OpenDoc6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc6.html) method does not set the current working directory. Therefore, you might want to set the current working directory programmatically (see [ISldWorks::SetCurrentWorkingDirectory](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetCurrentWorkingDirectory.html)) before opening a file containing references. By doing this, your application behaves as if the file was opened interactively using the File Open dialog.

For more information on the search criteria used by the SOLIDWORKS Design application when loading file references, see SOLIDWORKS Design user-interface help.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetCurrentMacroPathFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathFolder.html)
[ISldWorks::GetCurrentMacroPathName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathName.html)
[ISldWorks::SetCurrentWorkingDirectory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetCurrentWorkingDirectory.html)
[ISldWorks::GetExecutablePath Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetExecutablePath.html)

## Availability

SOLIDWORKS 98Plus, datecode 1999087
