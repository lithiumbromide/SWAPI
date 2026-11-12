---
title: "GetTertiaryDatumModifiers Method (ISwDMDimXpertGeometricTolerance)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertGeometricTolerance"
member: "GetTertiaryDatumModifiers"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~GetTertiaryDatumModifiers.html"
---

# GetTertiaryDatumModifiers Method (ISwDMDimXpertGeometricTolerance)

Gets all of the material condition modifiers of the tertiary datum in this DimXpert geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTertiaryDatumModifiers() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertGeometricTolerance
Dim value As System.Object

value = instance.GetTertiaryDatumModifiers()
```

### C#

```csharp
System.object GetTertiaryDatumModifiers()
```

### C++/CLI

```cpp
System.Object^ GetTertiaryDatumModifiers();
```

### Return Value

Array of material condition modifiers as defined in [swDmDimXpertMaterialConditionModifier_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmDimXpertMaterialConditionModifier_e.html)

## VBA Syntax

See [SwDMDimXpertGeometricTolerance::GetTertiaryDatumModifiers](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertGeometricTolerance~GetTertiaryDatumModifiers.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertGeometricTolerance Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance.html)
[ISwDMDimXpertGeometricTolerance Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance_members.html)
[ISwDMDimXpertGeometricTolerance::IGetTertiaryDatumModifiers Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~IGetTertiaryDatumModifiers.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
