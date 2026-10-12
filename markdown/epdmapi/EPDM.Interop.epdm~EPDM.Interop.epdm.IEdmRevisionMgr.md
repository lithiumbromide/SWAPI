---
title: "IEdmRevisionMgr Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRevisionMgr"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr.html"
---

# IEdmRevisionMgr Interface

Allows you to update revision numbers on many files all at once.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmRevisionMgr
```

### C#

```csharp
public interface IEdmRevisionMgr
```

### C++/CLI

```cpp
public interface class IEdmRevisionMgr
```

## Remarks

This interface:

- inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).
- is extended by [IEdmRevisionMgr2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr2.html).
- is more efficient than calling [IEdmFile5::IncrementRevision](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~IncrementRevision.html) for each file whose revision number you want to update.

Typical usage of this interface:

1. Access this interface by calling IEdmVault7::CreateUtility, setting eType to [EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_RevisionMgr.
2. Call [IEdmRevisionMgr::SetRevisionCounters](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr~SetRevisionCounters.html) for each file whose revision counters you want to set.
3. Call [IEdmRevisionMgr::IncrementRevision](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr~IncrementRevision.html) for each file whose revision you want to increment.
4. Call [IEdmRevisionMgr::Commit](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr~Commit.html) to commit all of the changes to the database.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmRevisionMgr Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
