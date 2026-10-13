---
title: "SketchExtend Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "SketchExtend"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchExtend.html"
---

# SketchExtend Method (ISketchManager)

Adds to the length of the selected sketch entity (i.e., line, centerline, or arc) to meet the nearest sketch entity.

## Syntax

### Visual Basic (Declaration)

```vb
Function SketchExtend( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean

value = instance.SketchExtend(X, Y, Z)
```

### C#

```csharp
System.bool SketchExtend(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool SketchExtend(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: Specify 0.0
- `Y`: Specify 0.0
- `Z`: Specify 0.0

### Return Value

True if the sketch entity is extended to meet the nearest sketch entity, false if not

## VBA Syntax

See [SketchManager::SketchExtend](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~SketchExtend.html).

## Examples

[Extend Sketch Entity (VBA)](Extend_Sketch_Entity_Example_VB.htm)
[Extend Sketch Entity (VB.NET)](Extend_Sketch_Entity_Example_VBNET.htm)
[Extend Sketch Entity (C#)](Extend_Sketch_Entity_Example_CSharp.htm)

## Remarks

Call this method multiple times to extend the selected line to meet successive sketch entities.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::SketchTrim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchTrim.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
