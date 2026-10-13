---
title: "type Property (ISwDMDimXpertBlockTolerances)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertBlockTolerances"
member: "type"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertBlockTolerances~type.html"
---

# type Property (ISwDMDimXpertBlockTolerances)

Gets the type of this DimXpert block tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property type As swDmDimXpertBlockToleranceType_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertBlockTolerances
Dim value As swDmDimXpertBlockToleranceType_e

value = instance.type
```

### C#

```csharp
swDmDimXpertBlockToleranceType_e type {get;}
```

### C++/CLI

```cpp
property swDmDimXpertBlockToleranceType_e type {
   swDmDimXpertBlockToleranceType_e get();
}
```

### Property Value

Type of block tolerance as defined in [swDmDimXpertBlockToleranceType_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmDimXpertBlockToleranceType_e.html)

## VBA Syntax

See [SwDMDimXpertBlockTolerances::type](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertBlockTolerances~type.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertBlockTolerances Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertBlockTolerances.html)
[ISwDMDimXpertBlockTolerances Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertBlockTolerances_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
