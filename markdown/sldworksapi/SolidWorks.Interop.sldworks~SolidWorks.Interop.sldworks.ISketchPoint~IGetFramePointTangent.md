---
title: "IGetFramePointTangent Method (ISketchPoint)"
project: "SOLIDWORKS API Help"
interface: "ISketchPoint"
member: "IGetFramePointTangent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~IGetFramePointTangent.html"
---

# IGetFramePointTangent Method (ISketchPoint)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFramePointTangent( _
   ByRef Status As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPoint
Dim Status As System.Boolean
Dim value As System.Double

value = instance.IGetFramePointTangent(Status)
```

### C#

```csharp
System.double IGetFramePointTangent(
   out System.bool Status
)
```

### C++/CLI

```cpp
System.double IGetFramePointTangent(
   [Out] System.bool Status
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Status`:

## VBA Syntax

See [SketchPoint::IGetFramePointTangent](ms-its:sldworksapivb6.chm::/sldworks~SketchPoint~IGetFramePointTangent.html).

## See Also

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.html)
