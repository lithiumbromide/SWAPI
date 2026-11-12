---
title: "GetPrimaryDatumModifiers Method (ISwDMDimXpertGeometricTolerance)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertGeometricTolerance"
member: "GetPrimaryDatumModifiers"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~GetPrimaryDatumModifiers.html"
---

# GetPrimaryDatumModifiers Method (ISwDMDimXpertGeometricTolerance)

Gets all of the material condition modifiers of the primary datum in this DimXpert geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPrimaryDatumModifiers() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertGeometricTolerance
Dim value As System.Object

value = instance.GetPrimaryDatumModifiers()
```

### C#

```csharp
System.object GetPrimaryDatumModifiers()
```

### C++/CLI

```cpp
System.Object^ GetPrimaryDatumModifiers();
```

### Return Value

Array of material condition modifiers as defined in [swDmDimXpertMaterialConditionModifier_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmDimXpertMaterialConditionModifier_e.html)

## VBA Syntax

See [SwDMDimXpertGeometricTolerance::GetPrimaryDatumModifiers](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertGeometricTolerance~GetPrimaryDatumModifiers.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertGeometricTolerance Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance.html)
[ISwDMDimXpertGeometricTolerance Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance_members.html)
[ISwDMDimXpertGeometricTolerance::IGetPrimaryDatumModifiers Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~IGetPrimaryDatumModifiers.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
