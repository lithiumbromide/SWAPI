---
title: "GetRevisionNumbers Method (IEdmRevisionMgr2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRevisionMgr2"
member: "GetRevisionNumbers"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr2~GetRevisionNumbers.html"
---

# GetRevisionNumbers Method (IEdmRevisionMgr2)

Gets the specified revision number in the vault.

## Syntax

### Visual Basic

```vb
Sub GetRevisionNumbers( _
   ByVal oIDorEmpty As System.Object, _
   ByRef ppoRetData As EdmRevNo() _
)
```

### C#

```csharp
void GetRevisionNumbers(
   System.object oIDorEmpty,
   out EdmRevNo[] ppoRetData
)
```

### C++/CLI

```cpp
void GetRevisionNumbers(
   System.Object^ oIDorEmpty,
   [Out] array<EdmRevNo> ppoRetData
)
```

### Parameters

- `oIDorEmpty`: ID of revision number to get or null to get all revision numbers in the vault
- `ppoRetData`: Array of [EdmRevNo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevNo.html) structures; one structure for each revision number

## Examples

[Find Revisions Using Component (C#)](Find_Revisions_Using_Component_Example_CSharp.htm)
[Find Revisions Using Component (VB.NET)](Find_Revisions_Using_Component_Example_VBNET.htm)

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmRevisionMgr2 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr2.html)
[IEdmRevisionMgr2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr2_members.html)

## Availability

SOLIDWORKS PDM Professional 2007 SP03
