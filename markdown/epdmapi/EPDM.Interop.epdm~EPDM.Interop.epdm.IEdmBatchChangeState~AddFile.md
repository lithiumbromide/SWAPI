---
title: "AddFile Method (IEdmBatchChangeState)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchChangeState"
member: "AddFile"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~AddFile.html"
---

# AddFile Method (IEdmBatchChangeState)

Adds a file to this batch of files whose states you want to change or whose transitions you want to revoke.

## Syntax

### Visual Basic

```vb
Sub AddFile( _
   ByVal lFileID As System.Integer, _
   ByVal lFolderID As System.Integer _
)
```

### C#

```csharp
void AddFile(
   System.int lFileID,
   System.int lFolderID
)
```

### C++/CLI

```cpp
void AddFile(
   System.int lFileID,
   System.int lFolderID
)
```

### Parameters

- `lFileID`: ID of file whose state you want to change or whose transition you want to revoke
- `lFolderID`: ID of file's folder

## Examples

See the [IEdmBatchChangeState4](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState4.html) examples.

## Remarks

After calling this method, call [IEdmBatchChangeState::ChangeState](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~ChangeState.html) to actually change the state of the file or revoke its transition.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchChangeState Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState.html)
[IEdmBatchChangeState Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
