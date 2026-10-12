---
title: "IEdmBomMgr Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBomMgr"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr.html"
---

# IEdmBomMgr Interface

Allows you to access the Bill of Materials (BOM) layouts installed in a vault.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmBomMgr
```

### C#

```csharp
public interface IEdmBomMgr
```

### C++/CLI

```cpp
public interface class IEdmBomMgr
```

## Remarks

This interface:

- Inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).
- Is extended by [IEdmBomMgr2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr2.html).

To view a vault's BOM layouts in the SOLIDWORKS PDM Professional Administration tool, log in to a vault and expand **Bills of Materials**.

To access this interface, call IEdmVault7::CreateUtility with eType = [EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_BomMgr.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmBomMgr Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
