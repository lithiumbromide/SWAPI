---
title: "ISetFramePointTangent Method (ISketchPoint)"
project: "SOLIDWORKS API Help"
interface: "ISketchPoint"
member: "ISetFramePointTangent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~ISetFramePointTangent.html"
---

# ISetFramePointTangent Method (ISketchPoint)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetFramePointTangent( _
   ByRef ToVector As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPoint
Dim ToVector As System.Double
Dim value As System.Boolean

value = instance.ISetFramePointTangent(ToVector)
```

### C#

```csharp
System.bool ISetFramePointTangent(
   ref System.double ToVector
)
```

### C++/CLI

```cpp
System.bool ISetFramePointTangent(
   System.double% ToVector
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ToVector`:

## VBA Syntax

See [SketchPoint::ISetFramePointTangent](ms-its:sldworksapivb6.chm::/sldworks~SketchPoint~ISetFramePointTangent.html).

## See Also

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.html)
