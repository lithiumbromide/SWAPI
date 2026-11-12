---
title: "InsertCombineFeature Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertCombineFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCombineFeature.html"
---

# InsertCombineFeature Method (IFeatureManager)

Combines the specified bodies in the multibody part to create a combine feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCombineFeature( _
   ByVal OperationType As System.Integer, _
   ByVal MainBody As Body2, _
   ByVal ToolVar As System.Object _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim OperationType As System.Integer
Dim MainBody As Body2
Dim ToolVar As System.Object
Dim value As Feature

value = instance.InsertCombineFeature(OperationType, MainBody, ToolVar)
```

### C#

```csharp
Feature InsertCombineFeature(
   System.int OperationType,
   Body2 MainBody,
   System.object ToolVar
)
```

### C++/CLI

```cpp
Feature^ InsertCombineFeature(
   System.int OperationType,
   Body2^ MainBody,
   System.Object^ ToolVar
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OperationType`: Operation as defined in [swBodyOperationType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyOperationType_e.html)
- `MainBody`:

  | If OperationType is ... | Then set MainBody to ... |
  | --- | --- |
  | swBodyOperationType_e.SWBODYADD | Nothing or null |
  | swBodyOperationType_e.SWBODYCUT | Target body |
  | swBodyOperationType_e.SWBODYINTERSECT | Nothing or null |

  (See **Remarks**)
- `ToolVar`: Array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) to combine (see **Remarks**)

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertCombineFeature](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertCombineFeature.html).

## Examples

[Combine Bodies (C#)](Combine_Bodies_Example_CSharp.htm)
[Combine Bodies (VB.NET)](Combine_Bodies_Example_VBNET.htm)
[Combine Bodies (VBA)](Combine_Bodies_Example_VB.htm)

## Remarks

You can either call this method, directly passing in the bodies with MainBody and ToolVar, or you can:

1. Select the bodies using [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) as follows:

  | To select... | Use Mark... |
  | --- | --- |
  | MainBody | 1 |
  | ToolVar bodies | 2 |
2. Call this method, setting MainBody to Nothing or null and ToolVar to an empty array.

See the SOLIDWORKS Help for more information about the combine feature.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::IInsertCombineFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertCombineFeature.html)
[ICombineBodiesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
