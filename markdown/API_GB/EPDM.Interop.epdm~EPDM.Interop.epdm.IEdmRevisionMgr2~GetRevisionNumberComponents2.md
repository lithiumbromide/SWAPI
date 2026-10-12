---
title: "GetRevisionNumberComponents2 Method (IEdmRevisionMgr2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRevisionMgr2"
member: "GetRevisionNumberComponents2"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr2~GetRevisionNumberComponents2.html"
---

# GetRevisionNumberComponents2 Method (IEdmRevisionMgr2)

Gets the specified revision number components in the vault.

## Syntax

### Visual Basic

```vb
Sub GetRevisionNumberComponents2( _
   ByVal oNameIDorEmpty As System.Object, _
   ByRef ppoRetData As EdmRevComponent2() _
)
```

### C#

```csharp
void GetRevisionNumberComponents2(
   System.object oNameIDorEmpty,
   out EdmRevComponent2[] ppoRetData
)
```

### C++/CLI

```cpp
void GetRevisionNumberComponents2(
   System.Object^ oNameIDorEmpty,
   [Out] array<EdmRevComponent2> ppoRetData
)
```

### Parameters

- `oNameIDorEmpty`: Name or ID of revision number component to retrieve, null to retrieve all components (see **Remarks**)
- `ppoRetData`: Array of [EdmRevComponent2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent2.html) structures; one structure for each revision number component

## Examples

[Find Revisions Using Component (C#)](Find_Revisions_Using_Component_Example_CSharp.htm)
[Find Revisions Using Component (VB.NET)](Find_Revisions_Using_Component_Example_VBNET.htm)

## Remarks

If oNameIDorEmpty is a positive integer, it is interpreted as the ID of the component to retrieve. If it is a negative integer, it is interpreted as a revision number, and all components with that revision number are returned.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmRevisionMgr2 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr2.html)
[IEdmRevisionMgr2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr2_members.html)

## Availability

SOLIDWORKS PDM Professional 2007 SP03
