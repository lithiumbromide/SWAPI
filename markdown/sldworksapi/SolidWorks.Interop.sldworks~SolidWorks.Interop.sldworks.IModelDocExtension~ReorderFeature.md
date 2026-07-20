---
title: "ReorderFeature Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "ReorderFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReorderFeature.html"
---

# ReorderFeature Method (IModelDocExtension)

Obsolete. Superseded by

[IModelDocExtension::ReorderFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReorderFeature2.html)

.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReorderFeature( _
   ByVal FeatureToMove As System.String, _
   ByVal TargetFeature As System.String, _
   ByVal MoveLocation As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim FeatureToMove As System.String
Dim TargetFeature As System.String
Dim MoveLocation As System.Integer
Dim value As System.Boolean

value = instance.ReorderFeature(FeatureToMove, TargetFeature, MoveLocation)
```

### C#

```csharp
System.bool ReorderFeature(
   System.string FeatureToMove,
   System.string TargetFeature,
   System.int MoveLocation
)
```

### C++/CLI

```cpp
System.bool ReorderFeature(
   System.String^ FeatureToMove,
   System.String^ TargetFeature,
   System.int MoveLocation
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `FeatureToMove`: Name of feature to move
- `TargetFeature`: Name of feature before or after which to move FeatureToMove; valid only if MoveLocation is[swMoveLocation_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveLocation_e.html).swMoveAfter

- or -

Name of folder; valid only if MoveLocation is swMoveLocation_e.swMoveToFolder
- `MoveLocation`: Move type as defined by

[swMoveLocation_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveLocation_e.html)

### Return Value

True if feature moved successfully, false if not

## VBA Syntax

See

[ModelDocExtension::ReorderFeature](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~ReorderFeature.html)

.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)

[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

[IPartDoc::ReorderFeature Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ReorderFeature.html)

[IAssemblyDoc::ReorderComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorderComponents.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
