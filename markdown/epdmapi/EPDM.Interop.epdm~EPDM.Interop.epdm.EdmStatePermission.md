---
title: "EdmStatePermission Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmStatePermission"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmStatePermission.html"
---

# EdmStatePermission Structure

Contains state permission information.

## Syntax

### Visual Basic

```vb
Public Structure EdmStatePermission
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmStatePermission : System.ValueType
```

### C++/CLI

```cpp
public value class EdmStatePermission : public System.ValueType
```

## Examples

struct EdmStatePermission
{
[enum EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html) [meOwnerType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmStatePermission~meOwnerType.html);
integer [mlOwnerID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmStatePermission~mlOwnerID.html);
integer [mlStateID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmStatePermission~mlStateID.html);
integer [mlEdmRightFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmStatePermission~mlEdmRightFlag.html);

};

## Remarks

Used by [IEdmUserMgr9::GetStatePermissions](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9~GetStatePermissions.html) and [IEdmUserMgr9::SetStatePermissions](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9~SetStatePermissions.html).

## See Also

[EdmStatePermission Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmStatePermission_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2017
