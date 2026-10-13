---
title: "Type Property (IEdmSWBomColumn)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSWBomColumn"
member: "Type"
kind: "property"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBomColumn~Type.html"
---

# Type Property (IEdmSWBomColumn)

Gets or sets the type of this BOM column.

## Syntax

### Visual Basic

```vb
Property Type As System.Integer
```

### C#

```csharp
System.int Type {get; set;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

0 = Zone

1 = Revision

2 = Description

3 = Date

4 = Approved

5 = User

6 = Configuration quantity

7 = Item number

8 = Part number

-1 = Type not found

## Examples

See the [IEdmBomMgr3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr3.html) examples.

## See Also

[IEdmSWBomColumn Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBomColumn.html)
[IEdmSWBomColumn Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBomColumn_members.html)

## Availability

SOLIDWORKS PDM Professional 2021 SP03
