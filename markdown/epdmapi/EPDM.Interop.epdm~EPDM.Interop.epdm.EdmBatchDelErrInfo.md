---
title: "EdmBatchDelErrInfo Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBatchDelErrInfo"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchDelErrInfo.html"
---

# EdmBatchDelErrInfo Structure

Contains information about an error that occurred during execution of [IEdmBatchDelete::CommitDelete](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~CommitDelete.html).

## Syntax

### Visual Basic

```vb
Public Structure EdmBatchDelErrInfo
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmBatchDelErrInfo : System.ValueType
```

### C++/CLI

```cpp
public value class EdmBatchDelErrInfo : public System.ValueType
```

## Examples

struct EdmBatchDelErrInfo{
integer [mlDocID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchDelErrInfo~mlDocID.html);
integer [mlProjID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchDelErrInfo~mlProjID.html);
string [mbsPathName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchDelErrInfo~mbsPathName.html);
integer [mlErrorCode](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchDelErrInfo~mlErrorCode.html);
};

## Examples

[Destroy Deleted Files in Vault (C#)](Destroy_Deleted_Files_in_Vault_Example_CSharp.htm)
[Destroy Deleted Files in Vault (VB.NET)](Destroy_Deleted_Files_in_Vault_Example_VBNET.htm)

## Remarks

Returned by [IEdmBatchDelete3::GetCommitErrors](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete3~GetCommitErrors.html).

## See Also

[EdmBatchDelErrInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchDelErrInfo_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

Version 12.0 of SOLIDWORKS PDM Professional
