---
title: "ShowChildComponentsInBOM2 Property (ISwDMConfiguration15)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration15"
member: "ShowChildComponentsInBOM2"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration15~ShowChildComponentsInBOM2.html"
---

# ShowChildComponentsInBOM2 Property (ISwDMConfiguration15)

Gets whether to show child components in the bill of materials (BOM) for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowChildComponentsInBOM2 As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration15
Dim value As System.Integer

instance.ShowChildComponentsInBOM2 = value

value = instance.ShowChildComponentsInBOM2
```

### C#

```csharp
System.int ShowChildComponentsInBOM2 {get; set;}
```

### C++/CLI

```cpp
property System.int ShowChildComponentsInBOM2 {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Show child components in BOM as defined in [swDmShowChildComponentsInBOMResult](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmShowChildComponentsInBOMResult.html)

## VBA Syntax

See [SwDMConfiguration15::ShowChildComponentsInBOM2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration15~ShowChildComponentsInBOM2.html).

## Remarks

This property only supports documents saved in SOLIDWORKS 2009 and later.

## See Also

[ISwDMConfiguration15 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration15.html)
[ISwDMConfiguration15 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration15_members.html)

## Availability

SOLIDWORKS Document Manager API 2018 SP0
