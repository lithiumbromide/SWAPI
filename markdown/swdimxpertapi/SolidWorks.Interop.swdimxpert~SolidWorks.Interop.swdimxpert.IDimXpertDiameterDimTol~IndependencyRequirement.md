---
title: "IndependencyRequirement Property (IDimXpertDiameterDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertDiameterDimTol"
member: "IndependencyRequirement"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDiameterDimTol~IndependencyRequirement.html"
---

# IndependencyRequirement Property (IDimXpertDiameterDimTol)

Gets whether this diameter dimension tolerance has an independency requirement.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IndependencyRequirement As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertDiameterDimTol
Dim value As System.Boolean

value = instance.IndependencyRequirement
```

### C#

```csharp
System.bool IndependencyRequirement {get;}
```

### C++/CLI

```cpp
property System.bool IndependencyRequirement {
   System.bool get();
}
```

### Property Value

True if independency requirement, false if not

## VBA Syntax

See [DimXpertDiameterDimTol::IndependencyRequirement](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertDiameterDimTol~IndependencyRequirement.html).

## Examples

[Get DimXpert Tolerance2 Example (VBA)](Get_DimXpert_Tolerance2_Example_VB.htm)
[Get DimXpert Tolerance2 Example (VB.NET)](Get_DimXpert_Tolerance2_Example_VBNET.htm)
[Get DimXpert Features and Annotations in a Model Example (C#)](Get_DimXpert_Features_and_Annotations_in_a_Model_Example_CSharp.htm)

## See Also

[IDimXpertDiameterDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDiameterDimTol.html)
[IDimXpertDiameterDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDiameterDimTol_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
