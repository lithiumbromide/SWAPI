---
title: "GetExplodeDirection Method (IPartExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IPartExplodeStep"
member: "GetExplodeDirection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~GetExplodeDirection.html"
---

# GetExplodeDirection Method (IPartExplodeStep)

Gets the explode direction (manipulator index and entity) for this explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExplodeDirection( _
   ByRef ExplDirIndex As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartExplodeStep
Dim ExplDirIndex As System.Integer
Dim value As System.Object

value = instance.GetExplodeDirection(ExplDirIndex)
```

### C#

```csharp
System.object GetExplodeDirection(
   out System.int ExplDirIndex
)
```

### C++/CLI

```cpp
System.Object^ GetExplodeDirection(
   [Out] System.int ExplDirIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ExplDirIndex`: Explode direction manipulator index as defined in [swExplodeDirectionIndex_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swExplodeDirectionIndex_e.html)

### Return Value

Explode direction entity (e.g., [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), [IRefAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html)); Nothing or null if an explode direction entity was not selected during creation of this explode step

## VBA Syntax

See [PartExplodeStep::GetExplodeDirection](ms-its:sldworksapivb6.chm::/sldworks~PartExplodeStep~GetExplodeDirection.html).

## See Also

[IPartExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.html)
[IPartExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep_members.html)
[IPartExplodeStep::SetExplodeDirection Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~SetExplodeDirection.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
