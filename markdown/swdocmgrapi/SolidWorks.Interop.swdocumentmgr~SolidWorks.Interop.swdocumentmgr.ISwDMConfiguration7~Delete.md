---
title: "Delete Property (ISwDMConfiguration7)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration7"
member: "Delete"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~Delete.html"
---

# Delete Property (ISwDMConfiguration7)

Gets or sets whether to mark this configuration as deleted.

## Syntax

### Visual Basic (Declaration)

```vb
Property Delete As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration7
Dim value As System.Boolean

instance.Delete = value

value = instance.Delete
```

### C#

```csharp
System.bool Delete {get; set;}
```

### C++/CLI

```cpp
property System.bool Delete {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True marks this configuration as deleted, false does not

## VBA Syntax

See [SwDMConfiguration7::Delete](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration7~Delete.html).

## See Also

[ISwDMConfiguration7 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7.html)
[ISwDMConfiguration7 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7_members.html)

## Availability

SOLIDWORKS Document Manager API 2007 FCS
