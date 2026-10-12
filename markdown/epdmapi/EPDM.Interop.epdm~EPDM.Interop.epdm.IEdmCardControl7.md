---
title: "IEdmCardControl7 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCardControl7"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl7.html"
---

# IEdmCardControl7 Interface

Allows you to access a control in a file or folder data card.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmCardControl7
   Inherits IEdmCardControl5, IEdmCardControl6, IEdmObject5
```

### C#

```csharp
public interface IEdmCardControl7 : IEdmCardControl5, IEdmCardControl6, IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmCardControl7 : public IEdmCardControl5, IEdmCardControl6, IEdmObject5
```

## Examples

[Get Card Control Information (C#)](Get_Card_Control_Info_Example_CSharp.htm)
[Get Card Control Information (VB.NET)](Get_Card_Control_Info_Example_VBNET.htm)

## Remarks

This interface extends [IEdmCardControl6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl6.html) by providing the ability to get the list of items in a list control on the data card.

To access this interface, call [IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html) with eType = [EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html).EdmObject_CardControl.

## See Also

[IEdmCardControl7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl7_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
