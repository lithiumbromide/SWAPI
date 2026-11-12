---
title: "EdmCheckRef Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmCheckRef"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCheckRef.html"
---

# EdmCheckRef Structure

Contains information about a file reference.

## Syntax

### Visual Basic

```vb
Public Structure EdmCheckRef
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmCheckRef : System.ValueType
```

### C++/CLI

```cpp
public value class EdmCheckRef : public System.ValueType
```

## Examples

struct EdmCheckRef{
integer [mlParentFileID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCheckRef~mlParentFileID.html);
integer [mlRefFileID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCheckRef~mlRefFileID.html);
string [mbsParentPath](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCheckRef~mbsParentPath.html);
string [mbsRefPath](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCheckRef~mbsRefPath.html);
integer [mlRefVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCheckRef~mlRefVersion.html);
integer [mlRefLatestVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCheckRef~mlRefLatestVersion.html);
integer [mlRefFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCheckRef~mlRefFolderID.html);
};

## Remarks

Returned by [IEdmRevisionMgr3::VerUpgrade_ReferenceCheck](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr3~VerUpgrade_ReferenceCheck.html).

## See Also

[EdmCheckRef Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCheckRef_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2009
