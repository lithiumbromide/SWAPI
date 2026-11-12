---
title: "IEdmHistory2 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmHistory2"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory2.html"
---

# IEdmHistory2 Interface

Allows you to access the history listing of files or folders.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmHistory2
   Inherits IEdmHistory
```

### C#

```csharp
public interface IEdmHistory2 : IEdmHistory
```

### C++/CLI

```cpp
public interface class IEdmHistory2 : public IEdmHistory
```

## Remarks

This interface:

- Extends [IEdmHistory](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory.html) by adding the ability to roll back a file.
- Is extended by [IEdmHistory3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3.html).

To access this interface, call [IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html) with eType set to [EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_History.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmHistory2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory2_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
