---
title: "SetCurrentWorkingDirectory Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "SetCurrentWorkingDirectory"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetCurrentWorkingDirectory.html"
---

# SetCurrentWorkingDirectory Method (ISldWorks)

Sets the current working directory to be used by SOLIDWORKS.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCurrentWorkingDirectory( _
   ByVal CurrentWorkingDirectory As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim CurrentWorkingDirectory As System.String
Dim value As System.Boolean

value = instance.SetCurrentWorkingDirectory(CurrentWorkingDirectory)
```

### C#

```csharp
System.bool SetCurrentWorkingDirectory(
   System.string CurrentWorkingDirectory
)
```

### C++/CLI

```cpp
System.bool SetCurrentWorkingDirectory(
   System.String^ CurrentWorkingDirectory
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CurrentWorkingDirectory`: Directory to set as the current working directory

### Return Value

True if specified direction is set as the current working directory, false if not

## VBA Syntax

See [SldWorks::SetCurrentWorkingDirectory](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~SetCurrentWorkingDirectory.html).

## Examples

[Open Document (VBA)](Open_Document_Example_VB.htm)
[Open Document (VB.NET)](Open_Document_Example_VBNET.htm)
[Open Document (C#)](Open_Document_Example_CSharp.htm)

## Remarks

The current working directory is used when opening documents containing references. If explicit search folders are not set (see [ISldWorks::SetSearchFolders](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetSearchFolders.html)), then SOLIDWORKS will initially try to locate file references (for example, assembly component parts) in the current working directory. Interactively, the current working directory is used by the File Open dialog and is set when you choose the Open dialog button.

The [ISldWorks::OpenDoc6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc6.html) method does not set the current working directory. Therefore, you may want to set the current working directory using ISldWorks::SetCurrentWorkingDirectory before opening a file that contains references. By doing so, you will get the same behavior as if the file was opened interactively using the File Open dialog.

For more information on the search criteria used by SOLIDWORKS when loading file references, see SOLIDWORKS Help.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetCurrentWorkingDirectory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentWorkingDirectory.html)
[ISldWorks::GetCurrentMacroPathFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathFolder.html)
[ISldWorks::GetCurrentMacroPathName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathName.html)
[ISldWorks::GetExecutablePath Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetExecutablePath.html)

## Availability

SOLIDWORKS 98Plus, datecode 1999087
