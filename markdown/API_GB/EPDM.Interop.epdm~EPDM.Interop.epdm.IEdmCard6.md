---
title: "IEdmCard6 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCard6"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard6.html"
---

# IEdmCard6 Interface

Allows you to access the file or folder data card that is created with the SOLIDWORKS PDM Professional's Card Editor.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmCard6
   Inherits IEdmCard5, IEdmObject5
```

### C#

```csharp
public interface IEdmCard6 : IEdmCard5, IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmCard6 : public IEdmCard5, IEdmObject5
```

## Examples

[Get Card Control Information (VB.NET)](Get_Card_Control_Info_Example_VBNET.htm)
[Get Card Control Information (C#)](Get_Card_Control_Info_Example_CSharp.htm)

## Remarks

This interface extends [IEdmCard5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5.html) by getting the card type.

To access this interface, call [IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html) with eType = [EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html).EdmObject_Card.

## See Also

[IEdmCard6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard6_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
