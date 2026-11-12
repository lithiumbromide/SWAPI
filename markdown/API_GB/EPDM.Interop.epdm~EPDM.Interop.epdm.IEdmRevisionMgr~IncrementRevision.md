---
title: "IncrementRevision Method (IEdmRevisionMgr)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRevisionMgr"
member: "IncrementRevision"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr~IncrementRevision.html"
---

# IncrementRevision Method (IEdmRevisionMgr)

Increments the revision of the specified file.

## Syntax

### Visual Basic

```vb
Sub IncrementRevision( _
   ByVal lFileID As System.Integer _
)
```

### C#

```csharp
void IncrementRevision(
   System.int lFileID
)
```

### C++/CLI

```cpp
void IncrementRevision(
   System.int lFileID
)
```

### Parameters

- `lFileID`: ID of file on which to increment the revision

## Examples

[Set Initial Revision (VB.NET)](Set_Initial_Revision_Example_VBNET.htm)
[Set Initial Revision (C#)](Set_Initial_Revision_Example_CSharp.htm)

## Remarks

If you call [IEdmRevisionMgr::SetRevisionCounters](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr~SetRevisionCounters.html) before calling this method, the new revision number that gets generated uses the counters that are specified in the call to IEdmRevisionMgr::SetRevisionCounters. If counters have not been explicitly set, the component counters are incremented by one.

The order of calls to IEdmRevisionMgr::SetRevisionCounters and this method does not matter. Calls to this method are always processed after calls to IEdmRevisionMgr::SetRevisionCounters.

After calling this method, call [IEdmRevisionMgr::Commit](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr~Commit.html) to commit the revision increment to the database.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmRevisionMgr Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr.html)
[IEdmRevisionMgr Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr_members.html)

## Availability

SOLIDWORKS PDM Professional 2007
