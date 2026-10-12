---
title: "EdmListFolder Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmListFolder"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFolder.html"
---

# EdmListFolder Structure

Contains information about a folder returned from [IEdmBatchListing::GetFolders](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~GetFolders.html).

## Syntax

### Visual Basic

```vb
Public Structure EdmListFolder
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmListFolder : System.ValueType
```

### C++/CLI

```cpp
public value class EdmListFolder : public System.ValueType
```

## Examples

struct EdmListFolder{
integer [mlFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFolder~mlFolderID.html);
integer [mlParam](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFolder~mlParam.html);
string [mbsPath](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFolder~mbsPath.html);
object [moColumnData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFolder~moColumnData.html);
};

## See Also

[EdmListFolder Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFolder_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
