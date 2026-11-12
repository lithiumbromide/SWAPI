---
title: "EdmListFile Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmListFile"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile.html"
---

# EdmListFile Structure

Holds information about a file returned by the [IEdmBatchListing::GetFiles](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~GetFiles.html) method.

## Syntax

### Visual Basic

```vb
Public Structure EdmListFile
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmListFile : System.ValueType
```

### C++/CLI

```cpp
public value class EdmListFile : public System.ValueType
```

## Examples

struct EdmListFile

{
integer [mlFileID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile~mlFileID.html);
integer [mlFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile~mlFolderID.html);
integer [mlParam](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile~mlParam.html);
integer [mlLatestVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile~mlLatestVersion.html);
integer [mlLocalVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile~mlLocalVersion.html);
string [mbsLockUser](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile~mbsLockUser.html);
string [mbsLockComputer](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile~mbsLockComputer.html);
string [mbsLockPath](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile~mbsLockPath.html);
string [mbsRevisionName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile~mbsRevisionName.html);
struct [EdmWorkflowInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmWorkflowInfo.html) [moCurrentState](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile~moCurrentState.html);
object [moColumnData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile~moColumnData.html);
};

## Remarks

This struct is extended by [EdmListFile2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2.html), which is returned by the [IEdmBatchListing4::GetFiles2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing4~GetFiles2.html) method.

## See Also

[EdmListFile Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
