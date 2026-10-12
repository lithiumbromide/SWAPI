---
title: "ShowChildComponentsInBOM Property (ISwDMConfiguration11)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration11"
member: "ShowChildComponentsInBOM"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~ShowChildComponentsInBOM.html"
---

# ShowChildComponentsInBOM Property (ISwDMConfiguration11)

Obsolete. Superseded by [ISwDMConfiguration15::ShowChildComponentsInBOM2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration15~ShowChildComponentsInBOM2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowChildComponentsInBOM As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration11
Dim value As System.Integer

instance.ShowChildComponentsInBOM = value

value = instance.ShowChildComponentsInBOM
```

### C#

```csharp
System.int ShowChildComponentsInBOM {get; set;}
```

### C++/CLI

```cpp
property System.int ShowChildComponentsInBOM {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Show child components in BOM as defined in [swDmShowChildComponetsInBOMResult](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmShowChildComponentsInBOMResult.html)

## VBA Syntax

See [SwDMConfiguration11::ShowChildComponentsInBOM](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration11~ShowChildComponentsInBOM.html).

## Remarks

This property only supports documents saved in SOLIDWORKS 2009 and later.

## See Also

[ISwDMConfiguration11 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11.html)
[ISwDMConfiguration11 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11_members.html)
