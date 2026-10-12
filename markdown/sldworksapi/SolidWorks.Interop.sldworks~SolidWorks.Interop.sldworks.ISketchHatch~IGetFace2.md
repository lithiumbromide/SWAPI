---
title: "IGetFace2 Method (ISketchHatch)"
project: "SOLIDWORKS API Help"
interface: "ISketchHatch"
member: "IGetFace2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~IGetFace2.html"
---

# IGetFace2 Method (ISketchHatch)

Gets the face associated with this sketch hatch.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFace2() As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchHatch
Dim value As Face2

value = instance.IGetFace2()
```

### C#

```csharp
Face2 IGetFace2()
```

### C++/CLI

```cpp
Face2^ IGetFace2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) associated with the sketch hatch or null if the operation fails

## VBA Syntax

See [SketchHatch::IGetFace2](ms-its:sldworksapivb6.chm::/sldworks~SketchHatch~IGetFace2.html).

## Remarks

You should not select the returned face. Only use the returned face for getting the geometry of the sketch hatch: loops, edges, equations for the edges, and so on. Do not hold onto the pointer the face after it is used as the face is transient.

## See Also

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html)
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.html)
[ISketchHatch::GetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~GetFace.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
