---
title: "mpoObject Field"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmFileInfo"
member: "mpoObject"
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFileInfo~mpoObject.html"
---

# mpoObject Field

Interface for the file or folder that was added to the batch using one of the [IEdmBatchAdd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd.html)::AddXxxxx methods.

## Syntax

### Visual Basic

```vb
Public mpoObject As IEdmObject5
```

### C#

```csharp
public IEdmObject5 mpoObject
```

### C++/CLI

```cpp
public:
IEdmObject5^ mpoObject
```

### Field Value

[IEdmFile6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile6.html), if a file, or [IEdmFolder6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder6.html), if a folder

## Remarks

This member is valid only if you specify [EdmBatchAddFolderFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchAddFolderFlag.html).Ebaff_GetInterface or [EdmAddFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddFlag.html).EdmAdd_GetInterface in the method that adds the file or folder to the batch.

## See Also

[EdmFileInfo Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFileInfo.html)
[EdmFileInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFileInfo_members.html)
