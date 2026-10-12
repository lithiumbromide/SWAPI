---
title: "Commit Method (IEdmRevisionMgr)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRevisionMgr"
member: "Commit"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr~Commit.html"
---

# Commit Method (IEdmRevisionMgr)

Commits all of the changes made in this batch object.

## Syntax

### Visual Basic

```vb
Sub Commit( _
   ByVal bsComment As System.String, _
   ByRef ppoErrors As EdmRevError() _
)
```

### C#

```csharp
void Commit(
   System.string bsComment,
   out EdmRevError[] ppoErrors
)
```

### C++/CLI

```cpp
void Commit(
   System.String^ bsComment,
   [Out] array<EdmRevError> ppoErrors
)
```

### Parameters

- `bsComment`: Comment to show in the file history of revision increments
- `ppoErrors`: Array of [EdmRevError](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevError.html) structures; one structure for each error that occurred during processing

## Examples

[Set Initial Revision (VB.NET)](Set_Initial_Revision_Example_VBNET.htm)
[Set Initial Revision (C#)](Set_Initial_Revision_Example_CSharp.htm)

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmRevisionMgr Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr.html)
[IEdmRevisionMgr Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr_members.html)

## Availability

SOLIDWORKS PDM Professional 2007
