---
title: "mpoFolder Field"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmFolderInfo"
member: "mpoFolder"
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderInfo~mpoFolder.html"
---

# mpoFolder Field

Interface for the folder that was added to the batch using [IEdmBatchAddFolders::AddFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders~AddFolder.html).

## Syntax

### Visual Basic

```vb
Public mpoFolder As IEdmFolder6
```

### C#

```csharp
public IEdmFolder6 mpoFolder
```

### C++/CLI

```cpp
public:
IEdmFolder6^ mpoFolder
```

## Remarks

This member is valid only if you specify [EdmBatchAddFolderFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchAddFolderFlag.html).Ebaff_GetInterface in IEdmBatchAddFolders::AddFolder.

## See Also

[EdmFolderInfo Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderInfo.html)
[EdmFolderInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderInfo_members.html)
