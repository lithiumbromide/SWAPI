---
title: "InsertSubWeldFolder2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertSubWeldFolder2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSubWeldFolder2.html"
---

# InsertSubWeldFolder2 Method (IFeatureManager)

Creates a sub weld folder feature containing the specified weldment bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSubWeldFolder2( _
   ByVal BodyArray As System.Object _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim BodyArray As System.Object
Dim value As Feature

value = instance.InsertSubWeldFolder2(BodyArray)
```

### C#

```csharp
Feature InsertSubWeldFolder2(
   System.object BodyArray
)
```

### C++/CLI

```cpp
Feature^ InsertSubWeldFolder2(
   System.Object^ BodyArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyArray`: Array of [Body2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) objects

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertSubWeldFolder2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertSubWeldFolder2.html).

## Examples

[Insert Weldment Features (VBA)](Insert_Weldment_Features_Example_VB.htm)
[Insert Weldment Features (VB.NET)](Insert_Weldment_Features_Example_VBNET.htm)
[Insert Weldment Features (C#)](Insert_Weldment_Features_Example_CSharp.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::InsertSubWeldFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSubWeldFolder.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
