---
title: "EdmListFile2 Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmListFile2"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2.html"
---

# EdmListFile2 Structure

Holds information about a file returned by the [IEdmBatchListing4::GetFiles2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing4~GetFiles2.html) method.

## Syntax

### Visual Basic

```vb
Public Structure EdmListFile2
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmListFile2 : System.ValueType
```

### C++/CLI

```cpp
public value class EdmListFile2 : public System.ValueType
```

## Examples

struct EdmListFile

{
short [mbHasLockRights](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2~mbHasLockRights.html);
short [mbLocalOverwrittenVersionObsolete](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2~mbLocalOverwrittenVersionObsolete.html);
string [mbsLockComputer](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2~mbsLockComputer.html);
string [mbsLockPath](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2~mbsLockPath.html);
string [mbsLockUser](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2~mbsLockUser.html);
string [mbsLockViewID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2~mbsLockViewID.html);
string [mbsRevisionName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2~mbsRevisionName.html);
integer [mlFileID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2~mlFileID.html);
integer [mlFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2~mlFolderID.html);
integer [mlLatestVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2~mlLatestVersion.html);
integer [mlLocalVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2~mlLocalVersion.html);
integer [mlLockProjectID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2~mlLockProjectID.html);
integer [mlParam](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2~mlParam.html);
object [moColumnData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2~moColumnData.html);
struct [EdmWorkflowInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmWorkflowInfo.html) [moCurrentState](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2~moCurrentState.html);
};

## Examples

[Get File References for a File (C#)](Get_File_References_for_File_Example_CSharp.htm)
[Get File References for a File (VB.NET)](Get_File_References_for_File_Example_VBNET.htm)

## Remarks

This struct is an extended version of the [EdmListFile](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile.html) struct, which is returned by the [IEdmBatchListing::GetFiles](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~GetFiles.html) method.

## See Also

[EdmListFile2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2017
