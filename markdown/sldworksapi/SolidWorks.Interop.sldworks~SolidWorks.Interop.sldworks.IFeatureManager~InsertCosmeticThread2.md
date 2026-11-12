---
title: "InsertCosmeticThread2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertCosmeticThread2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCosmeticThread2.html"
---

# InsertCosmeticThread2 Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertCosmeticThread3.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCosmeticThread3.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCosmeticThread2( _
   ByVal Type As System.Short, _
   ByVal Depth As System.Double, _
   ByVal Length As System.Double, _
   ByVal Note As System.String _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Type As System.Short
Dim Depth As System.Double
Dim Length As System.Double
Dim Note As System.String
Dim value As Feature

value = instance.InsertCosmeticThread2(Type, Depth, Length, Note)
```

### C#

```csharp
Feature InsertCosmeticThread2(
   System.short Type,
   System.double Depth,
   System.double Length,
   System.string Note
)
```

### C++/CLI

```cpp
Feature^ InsertCosmeticThread2(
   System.short Type,
   System.double Depth,
   System.double Length,
   System.String^ Note
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type as defined in [swCosmeticThreadType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCosmeticThreadType_e.html)
- `Depth`: Diameter of the cosmetic thread
- `Length`: Length of the cosmetic thread
- `Note`: Callout text to display in the drawing document

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertCosmeticThread2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertCosmeticThread2.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
