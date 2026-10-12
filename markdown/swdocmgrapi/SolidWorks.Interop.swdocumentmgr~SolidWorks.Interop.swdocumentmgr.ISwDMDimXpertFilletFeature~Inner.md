---
title: "Inner Property (ISwDMDimXpertFilletFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertFilletFeature"
member: "Inner"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFilletFeature~Inner.html"
---

# Inner Property (ISwDMDimXpertFilletFeature)

Gets whether this DimXpert fillet is for a hole or a pin.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Inner As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertFilletFeature
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

True if the fillet is for a hole; false if for a pin

## VBA Syntax

See [SwDMDimXpertFilletFeature::Inner](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertFilletFeature~Inner.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertFilletFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFilletFeature.html)
[ISwDMDimXpertFilletFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFilletFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
