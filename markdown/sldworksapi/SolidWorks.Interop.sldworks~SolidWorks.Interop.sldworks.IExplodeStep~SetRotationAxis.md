---
title: "SetRotationAxis Method (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "SetRotationAxis"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~SetRotationAxis.html"
---

# SetRotationAxis Method (IExplodeStep)

Sets the rotation axis (manipulator index and entity) for this regular explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetRotationAxis( _
   ByVal RotationAxis As System.Object, _
   ByVal RotAxisIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExplodeStep
Dim RotationAxis As System.Object
Dim RotAxisIndex As System.Integer

instance.SetRotationAxis(RotationAxis, RotAxisIndex)
```

### C#

```csharp
void SetRotationAxis(
   System.object RotationAxis,
   System.int RotAxisIndex
)
```

### C++/CLI

```cpp
void SetRotationAxis(
   System.Object^ RotationAxis,
   System.int RotAxisIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RotationAxis`: Rotation axis entity
- `RotAxisIndex`: Rotation manipulator index as defined in [swRotationAxisIndex_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRotationAxisIndex_e.html)

## VBA Syntax

See [ExplodeStep::SetRotationAxis](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~SetRotationAxis.html).

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)
[IExplodeStep::GetRotationAxis Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetRotationAxis.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
