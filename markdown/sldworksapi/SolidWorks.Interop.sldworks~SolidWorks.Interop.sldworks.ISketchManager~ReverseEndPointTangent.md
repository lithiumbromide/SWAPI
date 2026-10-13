---
title: "ReverseEndPointTangent Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "ReverseEndPointTangent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ReverseEndPointTangent.html"
---

# ReverseEndPointTangent Method (ISketchManager)

Reverses the end point tangent direction of splines and arcs.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReverseEndPointTangent( _
   ByVal ForceDeleteConstraints As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim ForceDeleteConstraints As System.Boolean
Dim value As System.Integer

value = instance.ReverseEndPointTangent(ForceDeleteConstraints)
```

### C#

```csharp
System.int ReverseEndPointTangent(
   System.bool ForceDeleteConstraints
)
```

### C++/CLI

```cpp
System.int ReverseEndPointTangent(
   System.bool ForceDeleteConstraints
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ForceDeleteConstraints`: True to force the deletion of constraints, false to not

### Return Value

Result code as defined in [swReverseEndPointTangentResult_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swReverseEndPointTangentResult_e.html)

## VBA Syntax

See [SketchManager::ReverseEndPointTangent](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~ReverseEndPointTangent.html).

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
