---
title: "ReorderFeature Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "ReorderFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ReorderFeature.html"
---

# ReorderFeature Method (IPartDoc)

Reorders features and their operations.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReorderFeature( _
   ByVal FeatureToMove As System.String, _
   ByVal MoveAfterFeature As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim FeatureToMove As System.String
Dim MoveAfterFeature As System.String
Dim value As System.Boolean

value = instance.ReorderFeature(FeatureToMove, MoveAfterFeature)
```

### C#

```csharp
System.bool ReorderFeature(
   System.string FeatureToMove,
   System.string MoveAfterFeature
)
```

### C++/CLI

```cpp
System.bool ReorderFeature(
   System.String^ FeatureToMove,
   System.String^ MoveAfterFeature
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FeatureToMove`: Name of the feature to move
- `MoveAfterFeature`: Name of the feature that now precedes the feature in the FeatureManager design tree

### Return Value

True if successful, false if not

## VBA Syntax

See [PartDoc::ReorderFeature](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~ReorderFeature.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FirstFeature.html)
[IAssemblyDoc::ReorderComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorderComponents.html)
[IModelDocExtension::ReorderFeature Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReorderFeature.html)
