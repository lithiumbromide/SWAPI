---
title: "EdmRevComponent Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRevComponent"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent.html"
---

# EdmRevComponent Structure

Obsolete. Superseded by [EdmRevComponent2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent2.html).

## Syntax

### Visual Basic

```vb
Public Structure EdmRevComponent
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmRevComponent : System.ValueType
```

### C++/CLI

```cpp
public value class EdmRevComponent : public System.ValueType
```

## Examples

struct EdmRevComponent

{
integer [mlComponentID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent~mlComponentID.html);
string [mbsComponentName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent~mbsComponentName.html);
};

## Remarks

Returned by [IEdmRevisionMgr::GetRevisionNumberComponents](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr~GetRevisionNumberComponents.html), which is obsolete and superseded by [IEdmRevisionMgr2.::GetRevisionNumberComponents2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr2~GetRevisionNumberComponents2.html), which returns EdmRevComponent2.

The struct contains the component information.

## See Also

[EdmRevComponent Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2007
