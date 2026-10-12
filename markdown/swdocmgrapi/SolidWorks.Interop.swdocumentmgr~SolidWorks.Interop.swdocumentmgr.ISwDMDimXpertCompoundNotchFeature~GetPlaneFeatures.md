---
title: "GetPlaneFeatures Method (ISwDMDimXpertCompoundNotchFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompoundNotchFeature"
member: "GetPlaneFeatures"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature~GetPlaneFeatures.html"
---

# GetPlaneFeatures Method (ISwDMDimXpertCompoundNotchFeature)

Gets the DimXpert plane features for both sides of this DimXpert compound notch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlaneFeatures( _
   ByRef Plane1 As SwDMDimXpertPlaneFeature, _
   ByRef Plane2 As SwDMDimXpertPlaneFeature _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompoundNotchFeature
Dim Plane1 As SwDMDimXpertPlaneFeature
Dim Plane2 As SwDMDimXpertPlaneFeature
Dim value As System.Boolean

value = instance.GetPlaneFeatures(Plane1, Plane2)
```

### C#

```csharp
System.bool GetPlaneFeatures(
   out SwDMDimXpertPlaneFeature Plane1,
   out SwDMDimXpertPlaneFeature Plane2
)
```

### C++/CLI

```cpp
System.bool GetPlaneFeatures(
   [Out] SwDMDimXpertPlaneFeature^ Plane1,
   [Out] SwDMDimXpertPlaneFeature^ Plane2
)
```

### Parameters

- `Plane1`: [ISwDMDimXpertPlaneFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertPlaneFeature.html)
- `Plane2`: [ISwDMDimXpertPlaneFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertPlaneFeature.html)

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertCompoundNotchFeature::GetPlaneFeatures](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompoundNotchFeature~GetPlaneFeatures.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompoundNotchFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature.html)
[ISwDMDimXpertCompoundNotchFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
