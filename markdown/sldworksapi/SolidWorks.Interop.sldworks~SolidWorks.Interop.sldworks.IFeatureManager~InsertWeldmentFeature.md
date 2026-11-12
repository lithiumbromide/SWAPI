---
title: "InsertWeldmentFeature Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertWeldmentFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentFeature.html"
---

# InsertWeldmentFeature Method (IFeatureManager)

Inserts a weldment feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertWeldmentFeature() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As Feature

value = instance.InsertWeldmentFeature()
```

### C#

```csharp
Feature InsertWeldmentFeature()
```

### C++/CLI

```cpp
Feature^ InsertWeldmentFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertWeldmentFeature](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertWeldmentFeature.html).

## Examples

[Insert Structural Weldment (C#)](Insert_Structural_Weldment_Example_CSharp.htm)
[Insert Structural Weldment (VB.NET)](Insert_Structural_Weldment_Example_VBNET.htm)
[Insert Structural Weldment (VBA)](Insert_Structural_Weldment_Example_VB.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
