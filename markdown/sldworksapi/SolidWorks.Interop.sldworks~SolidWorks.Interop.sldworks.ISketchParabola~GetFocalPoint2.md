---
title: "GetFocalPoint2 Method (ISketchParabola)"
project: "SOLIDWORKS API Help"
interface: "ISketchParabola"
member: "GetFocalPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola~GetFocalPoint2.html"
---

# GetFocalPoint2 Method (ISketchParabola)

Gets the sketch point for the focal point of the parabola.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFocalPoint2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchParabola
Dim value As System.Object

value = instance.GetFocalPoint2()
```

### C#

```csharp
System.object GetFocalPoint2()
```

### C++/CLI

```cpp
System.Object^ GetFocalPoint2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Focal [sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) or null if the operation fails

## VBA Syntax

See [SketchParabola::GetFocalPoint2](ms-its:sldworksapivb6.chm::/sldworks~SketchParabola~GetFocalPoint2.html).

## Examples

See the [ISketchParabola](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola.html) examples.

## See Also

[ISketchParabola Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola.html)
[ISketchParabola Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola_members.html)
[ISketdhParabola::IGetFocalPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola~IGetFocalPoint2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
