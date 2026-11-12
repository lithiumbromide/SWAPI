---
title: "IEdmRefItem2 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRefItem2"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem2.html"
---

# IEdmRefItem2 Interface

Allows you to access an item in an [IEdmRefItemContainer](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItemContainer.html). **NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmRefItem2
   Inherits IEdmRefItem
```

### C#

```csharp
public interface IEdmRefItem2 : IEdmRefItem
```

### C++/CLI

```cpp
public interface class IEdmRefItem2 : public IEdmRefItem
```

## Remarks

This interface extends [IEdmRefItem](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem.html) by providing the ability to get the old and new paths of references that have been moved or renamed by another client.

## Accessors

[IEdmRefItemContainer::GetItems](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItemContainer~GetItems.html)

## See Also

[IEdmRefItem2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem2_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
