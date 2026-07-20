---
title: "IEdmHistory4 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmHistory4"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory4.html"
---

# IEdmHistory4 Interface

Allows you to access the sorted history of files or folders.

NOTE:

Click the

Members

link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmHistory4
   Inherits IEdmHistory, IEdmHistory2, IEdmHistory3
```

### C#

```csharp
public interface IEdmHistory4 : IEdmHistory, IEdmHistory2, IEdmHistory3
```

### C++/CLI

```cpp
public interface class IEdmHistory4 : public IEdmHistory, IEdmHistory2, IEdmHistory3
```

## Examples

Tailor the

[IEdmHistory3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3.html)

examples to use this interface.

## Remarks

This interface extends IEdmHistory3 by providing the ability to show:

- a file's history using the same history dialog that is employed in the user interface
- a folder's history using the same history dialog that is employed in the user interface

To access this interface, call[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)with eType set to[EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_History.

## Accessors

IEdmVault7::CreateUtility

## See Also

[IEdmHistory4 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory4_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
