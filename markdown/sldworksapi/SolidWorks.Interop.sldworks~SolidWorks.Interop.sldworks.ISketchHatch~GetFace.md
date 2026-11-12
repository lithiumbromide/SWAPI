---
title: "GetFace Method (ISketchHatch)"
project: "SOLIDWORKS API Help"
interface: "ISketchHatch"
member: "GetFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~GetFace.html"
---

# GetFace Method (ISketchHatch)

Gets the face associated with this sketch hatch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFace() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchHatch
Dim value As System.Object

value = instance.GetFace()
```

### C#

```csharp
System.object GetFace()
```

### C++/CLI

```cpp
System.Object^ GetFace();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) associated with the sketch hatch or null if the operation fails

## VBA Syntax

See [SketchHatch::GetFace](ms-its:sldworksapivb6.chm::/sldworks~SketchHatch~GetFace.html).

## Examples

See the [ISketchHatch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html) examples.

## Remarks

This method returns the face in the space of the sketch or drawing view. You should not select the returned face. Only use the returned face for getting the geometry of the sketch hatch: loops, edges, equations for the edges, and so on. Do not hold on to the pointer to the face after it is used as the face is transient.

## See Also

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html)
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.html)
[ISketchHatch::IGetFace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~IGetFace2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
