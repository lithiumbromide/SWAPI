---
title: "AddCornerReliefCorner Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "AddCornerReliefCorner"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddCornerReliefCorner.html"
---

# AddCornerReliefCorner Method (IFeatureManager)

Adds the bend corner of two selected faces of a sheet metal body to the set of corners to which to apply a corner relief.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCornerReliefCorner() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Integer

value = instance.AddCornerReliefCorner()
```

### C#

```csharp
System.int AddCornerReliefCorner()
```

### C++/CLI

```cpp
System.int AddCornerReliefCorner();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Index of corner to which to apply the corner relief; used by [IFeatureManager::AddCornerReliefType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~AddCornerReliefType.html)

## VBA Syntax

See [FeatureManager::AddCornerReliefCorner](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~AddCornerReliefCorner.html).

## Examples

[Create Corner Relief Feature (C#)](Create_Corner_Relief_Feature_Example_CSharp.htm)
[Create Corner Relief Feature (VBA)](Create_Corner_Relief_Feature_Example_VB.htm)
[Create Corner Relief Feature (VB.NET)](Create_Corner_Relief_Feature_Example_VBNET.htm)

## Remarks

To create a corner relief feature:

1. Call [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) with Mark = 0 and Append = true to select the sheet metal body in which to create a corner relief feature.
2. Call IModelDocExtension::SelectByID2 with Mark = 4 and Append = true to select two faces that form a bend corner.
3. Call this method to add the corner to the corner relief feature.
4. Call [IFeatureManager::AddCornerReliefType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~AddCornerReliefType.html) to specify the corner relief for the corner.
5. Repeat steps 2 - 4 to add another corner to the corner relief feature.
6. Call [IFeatureManager::FinishCornerRelief](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FinishCornerRelief.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
