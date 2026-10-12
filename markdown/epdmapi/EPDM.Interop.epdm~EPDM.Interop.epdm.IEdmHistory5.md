---
title: "IEdmHistory5 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmHistory5"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5.html"
---

# IEdmHistory5 Interface

Allows you to access the sorted history of files or folders.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmHistory5
   Inherits IEdmHistory, IEdmHistory2, IEdmHistory3, IEdmHistory4
```

### C#

```csharp
public interface IEdmHistory5 : IEdmHistory, IEdmHistory2, IEdmHistory3, IEdmHistory4
```

### C++/CLI

```cpp
public interface class IEdmHistory5 : public IEdmHistory, IEdmHistory2, IEdmHistory3, IEdmHistory4
```

## Examples

Tailor the [IEdmHistory3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3.html) examples to use this interface.

## Remarks

This interface extends IEdmHistory4 by providing the ability to retrieve comments and system generated details separately.

To access this interface, call [IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html) with eType set to [EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_History.

## Accessors

IEdmVault7::CreateUtility

## See Also

[IEdmHistory5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
