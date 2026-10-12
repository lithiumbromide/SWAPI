---
title: "IGetPrimaryDatumModifiers Method (ISwDMDimXpertGeometricTolerance)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertGeometricTolerance"
member: "IGetPrimaryDatumModifiers"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~IGetPrimaryDatumModifiers.html"
---

# IGetPrimaryDatumModifiers Method (ISwDMDimXpertGeometricTolerance)

Gets all of the material condition modifiers of the primary datum in this DimXpert geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPrimaryDatumModifiers( _
   ByVal Count As System.Integer _
) As swDmDimXpertMaterialConditionModifier_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertGeometricTolerance
Dim Count As System.Integer
Dim value As swDmDimXpertMaterialConditionModifier_e

value = instance.IGetPrimaryDatumModifiers(Count)
```

### C#

```csharp
swDmDimXpertMaterialConditionModifier_e IGetPrimaryDatumModifiers(
   System.int Count
)
```

### C++/CLI

```cpp
swDmDimXpertMaterialConditionModifier_e IGetPrimaryDatumModifiers(
   System.int Count
)
```

### Parameters

- `Count`: Number of primary datum modifiers

### Return Value

in-process, unmanaged C++: Pointer to an array of [SwDMDimXpertMaterialConditionModifier_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDMDimXpertMaterialConditionModifier_e.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Use [ISwDMDimXpertGeometricTolerance::GetPrimaryDatumCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~GetPrimaryDatumCount.html) to populate the Count argument.

## See Also

[ISwDMDimXpertGeometricTolerance Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance.html)
[ISwDMDimXpertGeometricTolerance Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance_members.html)
[ISwDMDimXpertGeometricTolerance::GetPrimaryDatumModifiers Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~GetPrimaryDatumModifiers.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
