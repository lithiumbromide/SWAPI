---
title: "ItemDescriptiveName Property (IEdmItem)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmItem"
member: "ItemDescriptiveName"
kind: "property"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem~ItemDescriptiveName.html"
---

# ItemDescriptiveName Property (IEdmItem)

Gets the descriptive name of this item.

## Syntax

### Visual Basic

```vb
ReadOnly Property ItemDescriptiveName As System.String
```

### C#

```csharp
System.string ItemDescriptiveName {get;}
```

### C++/CLI

```cpp
property System.String^ ItemDescriptiveName {
   System.String^ get();
}
```

### Property Value

Descriptive name of this item

## Examples

See the [IEdmItem](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html) examples.

## Remarks

The descriptive name of an item is based on a variable in its data card.

An item also has an "item ID", which is its file name counterpart, accessible via the [IEdmItem::Name](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem~ItemDescriptiveName.html).

## See Also

[IEdmItem Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html)
[IEdmItem Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
