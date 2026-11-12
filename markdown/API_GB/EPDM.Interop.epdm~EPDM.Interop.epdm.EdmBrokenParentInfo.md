---
title: "EdmBrokenParentInfo Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBrokenParentInfo"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBrokenParentInfo.html"
---

# EdmBrokenParentInfo Structure

Contains broken parent information.

## Syntax

### Visual Basic

```vb
Public Structure EdmBrokenParentInfo
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmBrokenParentInfo : System.ValueType
```

### C++/CLI

```cpp
public value class EdmBrokenParentInfo : public System.ValueType
```

## Examples

struct EdmBrokenParentInfo{
integer [mlParentFileID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBrokenParentInfo~mlParentFileID.html);
integer [mlParentFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBrokenParentInfo~mlParentFolderID.html);
string [mbsParentName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBrokenParentInfo~mbsParentName.html);
integer [mlChildFileID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBrokenParentInfo~mlChildFileID.html);
integer [mlChildFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBrokenParentInfo~mlChildFolderID.html);
string [mbsChildName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBrokenParentInfo~mbsChildName.html);
};

## See Also

[EdmBrokenParentInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBrokenParentInfo_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2013
