---
title: "InsertCosmeticWeldBead Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertCosmeticWeldBead"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCosmeticWeldBead.html"
---

# InsertCosmeticWeldBead Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertCosmeticWeldBead2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCosmeticWeldBead2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCosmeticWeldBead( _
   ByVal WeldSize As System.Double _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim WeldSize As System.Double
Dim value As Feature

value = instance.InsertCosmeticWeldBead(WeldSize)
```

### C#

```csharp
Feature InsertCosmeticWeldBead(
   System.double WeldSize
)
```

### C++/CLI

```cpp
Feature^ InsertCosmeticWeldBead(
   System.double WeldSize
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WeldSize`: Size of the weld bead

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertCosmeticWeldBead](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertCosmeticWeldBead.html).

## Examples

[Insert Cosmetic Weld Bead (VBA)](Insert_Cosmetic_Weld_Bead_Example_VB.htm)
[Insert Cosmetic Weld Bead (VB.NET)](Insert_Cosmetic_Weld_Bead_Example_VBNET.htm)
[Insert Cosmetic Weld Bead (C#)](Insert_Cosmetic_Weld_Bead_Example_CSharp.htm)

## Remarks

Before calling this method, select the contact faces for the weld bead.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
