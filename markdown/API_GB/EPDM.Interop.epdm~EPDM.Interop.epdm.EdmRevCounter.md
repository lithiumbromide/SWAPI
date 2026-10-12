---
title: "EdmRevCounter Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRevCounter"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevCounter.html"
---

# EdmRevCounter Structure

Used in calls to [IEdmRevisionMgr::SetRevisionCounters](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr~SetRevisionCounters.html), this structure holds information about a single counter.

## Syntax

### Visual Basic

```vb
Public Structure EdmRevCounter
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmRevCounter : System.ValueType
```

### C++/CLI

```cpp
public value class EdmRevCounter : public System.ValueType
```

## Examples

struct EdmRevCounter{
string [mbsComponentName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevCounter~mbsComponentName.html);
integer [mlCounter](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevCounter~mlCounter.html);
};

## Examples

[Set Initial Revision (VB.NET)](Set_Initial_Revision_Example_VBNET.htm)
[Set Initial Revision (C#)](Set_Initial_Revision_Example_CSharp.htm)

## See Also

[EdmRevCounter Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevCounter_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2007
