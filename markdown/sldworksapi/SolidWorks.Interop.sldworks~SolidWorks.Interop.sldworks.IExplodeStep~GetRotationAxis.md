---
title: "GetRotationAxis Method (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "GetRotationAxis"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetRotationAxis.html"
---

# GetRotationAxis Method (IExplodeStep)

Gets the rotation axis (manipulator index and entity) for this regular explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRotationAxis( _
   ByRef RotAxisIndex As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IExplodeStep
Dim RotAxisIndex As System.Integer
Dim value As System.Object

value = instance.GetRotationAxis(RotAxisIndex)
```

### C#

```csharp
System.object GetRotationAxis(
   out System.int RotAxisIndex
)
```

### C++/CLI

```cpp
System.Object^ GetRotationAxis(
   [Out] System.int RotAxisIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RotAxisIndex`: Rotation manipulator index as defined in [swRotationAxisIndex_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRotationAxisIndex_e.html)

### Return Value

Rotation axis entity; Nothing or null if a rotation axis entity was not selected during creation of this explode step

## VBA Syntax

See [ExplodeStep::GetRotationAxis](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~GetRotationAxis.html).

## Remarks

This method is not valid for subassembly explode steps.

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)
[IExplodeStep::SetRotationAxis Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~SetRotationAxis.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
