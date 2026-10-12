---
title: "IEdmBomMgr2 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBomMgr2"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr2.html"
---

# IEdmBomMgr2 Interface

Allows you to access the Bill of Materials (BOM) layouts installed in a vault.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmBomMgr2
   Inherits IEdmBomMgr
```

### C#

```csharp
public interface IEdmBomMgr2 : IEdmBomMgr
```

### C++/CLI

```cpp
public interface class IEdmBomMgr2 : public IEdmBomMgr
```

## Examples

[Access Bill of Materials (VB.NET)](Access_Bill_of_Materials_Example_VBNET.htm)
[Access Bill of Materials (C#)](Access_Bill_of_Materials_Example_CSharp.htm)

## Remarks

This interface:

- Extends [IEdmBomMgr](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr.html) by providing:

- Is extended by [IEdmBomMgr3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr3.html).

To view a vault's BOM layouts in the SOLIDWORKS PDM Professional Administration tool, log in to a vault and expand **Bills of Materials**.

To access this interface, call IEdmVault7::CreateUtility with eType = [EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_BomMgr.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmBomMgr2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr2_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
