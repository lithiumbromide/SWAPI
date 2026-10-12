---
title: "IEdmCardControl5 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCardControl5"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5.html"
---

# IEdmCardControl5 Interface

Allows you to access a control in a file or folder data card.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmCardControl5
   Inherits IEdmObject5
```

### C#

```csharp
public interface IEdmCardControl5 : IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmCardControl5 : public IEdmObject5
```

## Remarks

This interface:

- inherits from [IEdmObject5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5.html).
- extends [IEdmCardControl6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl6.html).

To access this interface, call [IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html) with eType = [EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html).EdmObject_CardControl.

## Accessors

[IEdmCard5::GetControl](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5~GetControl.html)

[IEdmCard5::GetNextControl](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5~GetNextControl.html)

[IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html)

## See Also

[IEdmCardControl5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
