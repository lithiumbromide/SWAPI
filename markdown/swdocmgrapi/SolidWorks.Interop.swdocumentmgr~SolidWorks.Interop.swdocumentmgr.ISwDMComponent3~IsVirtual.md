---
title: "IsVirtual Property (ISwDMComponent3)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMComponent3"
member: "IsVirtual"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent3~IsVirtual.html"
---

# IsVirtual Property (ISwDMComponent3)

Gets whether this component is a virtual component.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property IsVirtual As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMComponent3
Dim value As System.Boolean

instance.IsVirtual = value

value = instance.IsVirtual
```

### C#

```csharp
System.bool IsVirtual {get; set;}
```

### C++/CLI

```cpp
property System.bool IsVirtual {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if this component is virtual, false if not

## VBA Syntax

See [SwDMComponent3::IsVirtual](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMComponent3~IsVirtual.html).

## Remarks

This property is only valid for assemblies saved in SOLIDWORKS 2008 and later. See the SOLIDWORKS Help for information about virtual components.

## See Also

[ISwDMComponent3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent3.html)
[ISwDMComponent3 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent3_members.html)

## Availability

SOLIDWORKS Document Manager API 2008 FCS
