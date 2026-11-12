---
title: "IEdmItem Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmItem"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html"
---

# IEdmItem Interface

Allows you to access an item.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmItem
   Inherits IEdmObject5
```

### C#

```csharp
public interface IEdmItem : IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmItem : public IEdmObject5
```

## Examples

[Get and Set Item References (VB.NET)](Get_and_Set_Item_References_Example_VBNET.htm)
[Get and Set Item References (C#)](Get_and_Set_Item_References_Example_CSharp.htm)

## Remarks

This interface inherits from [IEdmObject5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5.html).

To access this interface, you can:

- Cast [IEdmFile`X`](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html) objects to an IEdmItem pointer.
- Call IEdmVault5::GetObject, setting eType to [EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html).EdmObject_Item.

See the [Programming Items](Items.htm) topic for more information.

## Accessors

[IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html)

## See Also

[IEdmItem Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
