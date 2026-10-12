---
title: "IEdmBatchUpdate Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchUpdate"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate.html"
---

# IEdmBatchUpdate Interface

Allows you to set the values of several file and folder card variables all at once.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmBatchUpdate
```

### C#

```csharp
public interface IEdmBatchUpdate
```

### C++/CLI

```cpp
public interface class IEdmBatchUpdate
```

## Remarks

This interface:

- inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).
- is superseded by [IEdmBatchUpdate2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2.html), which can also update folder variables.

To set the values of file card variables:

1. Access this interface by calling [IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html), passing in [EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_BatchUpdate.
2. Call [IEdmBatchUpdate::SetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate~SetVar.html) once for each variable you want to update.
3. Call [IEdmBatchUpdate::Commit](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate~Commit.html) to commit all variable changes.

Before SOLIDWORKS PDM Professional 6.2, the only way to set the values of variables used in file data cards was to use the [IEdmEnumeratorVariable](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable9.html) interface which processed the variables one file and one variable at a time. This still works, but when setting the values of many variables, it is more efficient to use the IEdmBatchUpdate interface which accumulates all variables to set and then commits them all in a single operation.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmBatchUpdate Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
