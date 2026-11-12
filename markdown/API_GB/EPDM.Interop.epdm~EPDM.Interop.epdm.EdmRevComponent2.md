---
title: "EdmRevComponent2 Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRevComponent2"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent2.html"
---

# EdmRevComponent2 Structure

Holds information about a single revision number component.

## Syntax

### Visual Basic

```vb
Public Structure EdmRevComponent2
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmRevComponent2 : System.ValueType
```

### C++/CLI

```cpp
public value class EdmRevComponent2 : public System.ValueType
```

## Examples

struct EdmRevComponent2{
integer [mlComponentID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent2~mlComponentID.html);
string [mbsComponentName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent2~mbsComponentName.html);
integer [mlEdmRevComponentFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent2~mlEdmRevComponentFlags.html);
string [mbsData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent2~mbsData.html);
integer [mlRecipientID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent2~mlRecipientID.html);
integer [mlInitialCounter](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent2~mlInitialCounter.html);
};

## Examples

[Find Revisions Using Component (C#)](Find_Revisions_Using_Component_Example_CSharp.htm)
[Find Revisions Using Component (VB.NET)](Find_Revisions_Using_Component_Example_VBNET.htm)
[Set Initial Revision (VB.NET)](Set_Initial_Revision_Example_VBNET.htm)
[Set Initial Revision (C#)](Set_Initial_Revision_Example_CSharp.htm)

## Remarks

You can obtain this structure by calling [IEdmRevisionMgr2::GetRevisionNumberComponents2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr2~GetRevisionNumberComponents2.html).

## See Also

[EdmRevComponent2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent2_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2007 SP03
