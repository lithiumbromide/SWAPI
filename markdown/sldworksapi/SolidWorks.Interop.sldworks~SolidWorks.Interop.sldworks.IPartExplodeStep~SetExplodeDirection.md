---
title: "SetExplodeDirection Method (IPartExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IPartExplodeStep"
member: "SetExplodeDirection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~SetExplodeDirection.html"
---

# SetExplodeDirection Method (IPartExplodeStep)

Sets the explode direction (manipulator index and entity) for this explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetExplodeDirection( _
   ByVal ExplodeDirection As System.Object, _
   ByVal ExplDirIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPartExplodeStep
Dim ExplodeDirection As System.Object
Dim ExplDirIndex As System.Integer

instance.SetExplodeDirection(ExplodeDirection, ExplDirIndex)
```

### C#

```csharp
void SetExplodeDirection(
   System.object ExplodeDirection,
   System.int ExplDirIndex
)
```

### C++/CLI

```cpp
void SetExplodeDirection(
   System.Object^ ExplodeDirection,
   System.int ExplDirIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ExplodeDirection`: Explode direction entity (e.g., [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), [IRefAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html))
- `ExplDirIndex`: Explode direction manipulator index as defined in [swExplodeDirectionIndex_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swExplodeDirectionIndex_e.html)

## VBA Syntax

See [PartExplodeStep::SetExplodeDirection](ms-its:sldworksapivb6.chm::/sldworks~PartExplodeStep~SetExplodeDirection.html).

## See Also

[IPartExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.html)
[IPartExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep_members.html)
[IPartExplodeStep::GetExplodeDirection Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~GetExplodeDirection.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
