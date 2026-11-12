---
title: "IEdmCardControl6 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCardControl6"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl6.html"
---

# IEdmCardControl6 Interface

Allows you to access a control in a file or folder data card.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmCardControl6
   Inherits IEdmCardControl5, IEdmObject5
```

### C#

```csharp
public interface IEdmCardControl6 : IEdmCardControl5, IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmCardControl6 : public IEdmCardControl5, IEdmObject5
```

## Examples

[Get Card Control Information (VB.NET)](Get_Card_Control_Info_Example_VBNET.htm)
[Get Card Control Information (C#)](Get_Card_Control_Info_Example_CSharp.htm)

## Remarks

This interface:

- extends [IEdmCardControl5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5.html) by providing the option to update all configurations in edit box controls.
- is extended by [IEdmCardControl7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl7.html).

To access this interface, call [IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html) with eType = [EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html).EdmObject_CardControl.

## See Also

[IEdmCardControl6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl6_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
