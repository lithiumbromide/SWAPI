---
title: "InsertWeldmentCutList2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertWeldmentCutList2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentCutList2.html"
---

# InsertWeldmentCutList2 Method (IFeatureManager)

Inserts a cut-list-item folder feature containing the specified weldment bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertWeldmentCutList2( _
   ByVal Bodies As System.Object _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Bodies As System.Object
Dim value As Feature

value = instance.InsertWeldmentCutList2(Bodies)
```

### C#

```csharp
Feature InsertWeldmentCutList2(
   System.object Bodies
)
```

### C++/CLI

```cpp
Feature^ InsertWeldmentCutList2(
   System.Object^ Bodies
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Bodies`: Array of [Body2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) objects

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertWeldmentCutList2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertWeldmentCutList2.html).

## Examples

[Insert Weldment Cut List Example #2 (VBA)](Insert_Weldment_Cut_List2_Example_VB.htm)
[Insert Weldment Cut List Example #2 (VB.NET)](Insert_Weldment_Cut_List2_Example_VBNET.htm)
[Insert Weldment Cut List Example #2 (C#)](Insert_Weldment_Cut_List2_Example_CSharp.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IWeldmentCutListFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.html)
[IFeatureManager::InsertWeldmentCutList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentCutList.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
