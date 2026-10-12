---
title: "GetFramePointTangent Method (ISketchPoint)"
project: "SOLIDWORKS API Help"
interface: "ISketchPoint"
member: "GetFramePointTangent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~GetFramePointTangent.html"
---

# GetFramePointTangent Method (ISketchPoint)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFramePointTangent( _
   ByRef Status As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPoint
Dim Status As System.Boolean
Dim value As System.Object

value = instance.GetFramePointTangent(Status)
```

### C#

```csharp
System.object GetFramePointTangent(
   out System.bool Status
)
```

### C++/CLI

```cpp
System.Object^ GetFramePointTangent(
   [Out] System.bool Status
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Status`:

## VBA Syntax

See [SketchPoint::GetFramePointTangent](ms-its:sldworksapivb6.chm::/sldworks~SketchPoint~GetFramePointTangent.html).

## See Also

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.html)
