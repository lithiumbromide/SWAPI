---
title: "GetExplodeDirection Method (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "GetExplodeDirection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetExplodeDirection.html"
---

# GetExplodeDirection Method (IExplodeStep)

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
Dim instance As IExplodeStep
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

- `ExplDirIndex`: Explode direction manipulator index as defined in [swExplodeDirectionIndex_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swExplodeDirectionIndex_e.html); valid only for regular explode steps

### Return Value

Explode direction entity; Nothing or null if an explode direction entity was not selected during creation of this explode step

## VBA Syntax

See [ExplodeStep::GetExplodeDirection](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~GetExplodeDirection.html).

## Remarks

This method is not valid for subassembly explode steps.

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)
[IExplodeStep::SetExplodeDirection Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~SetExplodeDirection.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
