---
title: "EdmRevNo Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRevNo"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevNo.html"
---

# EdmRevNo Structure

Holds information about a revision number and is returned from [IEdmRevisionMgr2::GetRevisionNumbers](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr2~GetRevisionNumbers.html)..

## Syntax

### Visual Basic

```vb
Public Structure EdmRevNo
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmRevNo : System.ValueType
```

### C++/CLI

```cpp
public value class EdmRevNo : public System.ValueType
```

## Examples

struct EdmRevNo{
integer [mlRevNoID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevNo~mlRevNoID.html);
string [mbsRevNoName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevNo~mbsRevNoName.html);
string [mbsData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevNo~mbsData.html);
};

## Examples

[Find Revisions Using Component (C#)](Find_Revisions_Using_Component_Example_CSharp.htm)
[Find Revisions Using Component (VB.NET)](Find_Revisions_Using_Component_Example_VBNET.htm)

## Remarks

You can get the components of a revision number by calling [IEdmRevisionMgr2::GetRevisionNumberComponents2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr2~GetRevisionNumberComponents2.html) and passing a negative value to the EdmRevNo struct's [mlRevNoID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevNo~mlRevNoID.html) field as the argument.

## See Also

[EdmRevNo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevNo_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2007 SP03
