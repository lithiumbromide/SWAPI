---
title: "GetDataFolder Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetDataFolder"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDataFolder.html"
---

# GetDataFolder Method (ISldWorks)

Gets the data directory name currently used by SOLIDWORKS Design.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDataFolder( _
   ByVal BShowErrorMsg As System.Boolean _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim BShowErrorMsg As System.Boolean
Dim value As System.String

value = instance.GetDataFolder(BShowErrorMsg)
```

### C#

```csharp
System.string GetDataFolder(
   System.bool BShowErrorMsg
)
```

### C++/CLI

```cpp
System.String^ GetDataFolder(
   System.bool BShowErrorMsg
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BShowErrorMsg`: True to show any error messages in a dialog or false to avoid these dialogs (that is, data directory could not be found messages)

### Return Value

Data directory currently used by the SOLIDWORKS Design application

## VBA Syntax

See [SldWorks::GetDataFolder](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetDataFolder.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetCurrentWorkingDirectory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentWorkingDirectory.html)
[ISldWorks::SetCurrentWorkingDirectory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetCurrentWorkingDirectory.html)
[ISldWorks::GetExecutablePath Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetExecutablePath.html)
[ISldWorks::GetSearchFolders Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSearchFolders.html)

## Availability

SOLIDWORKS 99, datecode 1999207
