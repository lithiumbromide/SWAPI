---
title: "EdmTransitionPermission Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmTransitionPermission"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTransitionPermission.html"
---

# EdmTransitionPermission Structure

Contains transition permission information.

## Syntax

### Visual Basic

```vb
Public Structure EdmTransitionPermission
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmTransitionPermission : System.ValueType
```

### C++/CLI

```cpp
public value class EdmTransitionPermission : public System.ValueType
```

## Examples

struct EdmTransitionPermission
{
[enum EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html) [meOwnerType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTransitionPermission~meOwnerType.html);
integer [mlOwnerID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTransitionPermission~mlOwnerID.html);
integer [mlTransitionID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTransitionPermission~mlTransitionID.html);
integer [mlEdmRightFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTransitionPermission~mlEdmRightFlag.html);

};

## Remarks

Used by [IEdmUserMgr9::GetTransitionPermissions](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9~GetTransitionPermissions.html) and [IEdmUserMgr9::SetTransitionPermissions](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9~SetTransitionPermissions.html).

## See Also

[EdmTransitionPermission Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTransitionPermission_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2017
