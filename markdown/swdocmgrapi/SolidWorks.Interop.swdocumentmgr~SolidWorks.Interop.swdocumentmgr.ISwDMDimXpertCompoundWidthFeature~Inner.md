---
title: "Inner Property (ISwDMDimXpertCompoundWidthFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompoundWidthFeature"
member: "Inner"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundWidthFeature~Inner.html"
---

# Inner Property (ISwDMDimXpertCompoundWidthFeature)

Gets whether this compound width is for a hole or a pin.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Inner As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompoundWidthFeature
Dim value As System.Boolean

value = instance.Inner
```

### C#

```csharp
System.bool Inner {get;}
```

### C++/CLI

```cpp
property System.bool Inner {
   System.bool get();
}
```

### Property Value

True if width is for a hole; false if for a pin

## VBA Syntax

See [SwDMDimXpertCompoundWidthFeature::Inner](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompoundWidthFeature~Inner.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompoundWidthFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundWidthFeature.html)
[ISwDMDimXpertCompoundWidthFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundWidthFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
