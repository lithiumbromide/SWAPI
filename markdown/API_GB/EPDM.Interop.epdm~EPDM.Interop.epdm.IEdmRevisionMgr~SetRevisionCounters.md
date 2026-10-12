---
title: "SetRevisionCounters Method (IEdmRevisionMgr)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRevisionMgr"
member: "SetRevisionCounters"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr~SetRevisionCounters.html"
---

# SetRevisionCounters Method (IEdmRevisionMgr)

Sets the revision number component counters to specified values.

## Syntax

### Visual Basic

```vb
Sub SetRevisionCounters( _
   ByVal lFileID As System.Integer, _
   ByVal poCounters() As EdmRevCounter _
)
```

### C#

```csharp
void SetRevisionCounters(
   System.int lFileID,
   EdmRevCounter[] poCounters
)
```

### C++/CLI

```cpp
void SetRevisionCounters(
   System.int lFileID,
   array<EdmRevCounter>^ poCounters
)
```

### Parameters

- `lFileID`: ID of file in which to set counters
- `poCounters`: Array of [EdmRevCounter](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevCounter.html) structures; one structure for each revision component

## Examples

[Set Initial Revision (VB.NET)](Set_Initial_Revision_Example_VBNET.htm)
[Set Initial Revision (C#)](Set_Initial_Revision_Example_CSharp.htm)

## Remarks

This method only adds the new counters to this batch. After calling this method, you must call [IEdmRevisionMgr::Commit](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr~Commit.html) to commit the changes to the database.

This method only sets the revision component counters. It does not generate new revision numbers using any of the revision number generators that may be using the components. To create a new revision number for the file, you must also call [IEdmRevisionMgr::IncrementRevision](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr~IncrementRevision.html).

The order of calls to this method and IEdmRevisionMgr::IncrementRevision does not matter. Calls to IRevisionMgr::IncrementRevision are always processed after calls to this method.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmRevisionMgr Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr.html)
[IEdmRevisionMgr Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr_members.html)

## Availability

SOLIDWORKS PDM Professional 2007
