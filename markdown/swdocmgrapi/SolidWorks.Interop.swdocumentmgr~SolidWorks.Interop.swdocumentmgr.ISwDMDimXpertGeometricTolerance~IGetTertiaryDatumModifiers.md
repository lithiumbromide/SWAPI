---
title: "IGetTertiaryDatumModifiers Method (ISwDMDimXpertGeometricTolerance)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertGeometricTolerance"
member: "IGetTertiaryDatumModifiers"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~IGetTertiaryDatumModifiers.html"
---

# IGetTertiaryDatumModifiers Method (ISwDMDimXpertGeometricTolerance)

Gets all of the material condition modifiers of the tertiary datum in this DimXpert geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTertiaryDatumModifiers( _
   ByVal Count As System.Integer _
) As swDmDimXpertMaterialConditionModifier_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertGeometricTolerance
Dim Count As System.Integer
Dim value As swDmDimXpertMaterialConditionModifier_e

value = instance.IGetTertiaryDatumModifiers(Count)
```

### C#

```csharp
swDmDimXpertMaterialConditionModifier_e IGetTertiaryDatumModifiers(
   System.int Count
)
```

### C++/CLI

```cpp
swDmDimXpertMaterialConditionModifier_e IGetTertiaryDatumModifiers(
   System.int Count
)
```

### Parameters

- `Count`: Number of tertiary datum modifiers

### Return Value

in-process, unmanaged C++: Pointer to an array of [SwDMDimXpertMaterialConditionModifier_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDMDimXpertMaterialConditionModifier_e.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Use [ISwDMDimXpertGeometricTolerance::GetTertiaryDatumCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~GetTertiaryDatumCount.html) to populate the Count argument.

## See Also

[ISwDMDimXpertGeometricTolerance Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance.html)
[ISwDMDimXpertGeometricTolerance Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance_members.html)
[ISwDMDimxpertGeometricTolerance::GetTertiaryDatumModifiers Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~GetTertiaryDatumModifiers.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
