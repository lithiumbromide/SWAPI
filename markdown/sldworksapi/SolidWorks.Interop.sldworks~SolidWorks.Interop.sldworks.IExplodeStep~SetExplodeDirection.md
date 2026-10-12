---
title: "SetExplodeDirection Method (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "SetExplodeDirection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~SetExplodeDirection.html"
---

# SetExplodeDirection Method (IExplodeStep)

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
Dim instance As IExplodeStep
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

- `ExplodeDirection`: Explode direction entity
- `ExplDirIndex`: Explode direction manipulator index as defined in [swExplodeDirectionIndex_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swExplodeDirectionIndex_e.html); valid only for regular explode steps

## VBA Syntax

See [ExplodeStep::SetExplodeDirection](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~SetExplodeDirection.html).

## Examples

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html) examples.

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)
[IExplodeStep::GetExplodeDirection Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetExplodeDirection.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
