---
title: "ShowHistoryFile Method (IEdmHistory4)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmHistory4"
member: "ShowHistoryFile"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory4~ShowHistoryFile.html"
---

# ShowHistoryFile Method (IEdmHistory4)

Displays a history dialog for the specified file.

## Syntax

### Visual Basic

```vb
Sub ShowHistoryFile( _
   ByVal lFileID As System.Integer, _
   ByVal lParentFolderID As System.Integer, _
   Optional ByVal lParentWnd As System.Integer _
)
```

### C#

```csharp
void ShowHistoryFile(
   System.int lFileID,
   System.int lParentFolderID,
   System.int lParentWnd
)
```

### C++/CLI

```cpp
void ShowHistoryFile(
   System.int lFileID,
   System.int lParentFolderID,
   System.int lParentWnd
)
```

### Parameters

- `lFileID`: File ID
- `lParentFolderID`: Parent folder ID
- `lParentWnd`: Parent window handle

## See Also

[IEdmHistory4 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory4.html)

[IEdmHistory4 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory4_members.html)

## Availability

SOLIDWORKS PDM Professional 2025
