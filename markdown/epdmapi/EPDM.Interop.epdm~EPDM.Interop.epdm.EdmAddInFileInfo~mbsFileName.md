---
title: "mbsFileName Field"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmAddInFileInfo"
member: "mbsFileName"
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInFileInfo~mbsFileName.html"
---

# mbsFileName Field

Contains the add-in file name.

## Syntax

### Visual Basic

```vb
Public mbsFileName As System.String
```

### C#

```csharp
public System.string mbsFileName
```

### C++/CLI

```cpp
public:
System.String^ mbsFileName
```

### Field Value

File name, if the bsExtractPath argument to [IEdmAddInMgr8::ExtractInstalledAddIn](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr8~ExtractInstalledAddIn.html) is specified, or the complete path to the file, if an extract folder is not specified

## See Also

[EdmAddInFileInfo Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInFileInfo.html)
[EdmAddInFileInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInFileInfo_members.html)
