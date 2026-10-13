---
title: "IGetNormalVector Method (ISketchArc)"
project: "SOLIDWORKS API Help"
interface: "ISketchArc"
member: "IGetNormalVector"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~IGetNormalVector.html"
---

# IGetNormalVector Method (ISketchArc)

Gets the normal to the arc.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNormalVector() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchArc
Dim value As System.Double

value = instance.IGetNormalVector()
```

### C#

```csharp
System.double IGetNormalVector()
```

### C++/CLI

```cpp
System.double IGetNormalVector();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of 3 doubles (x,y,z), which represents the unit vector normal to the arc

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[ISketchArc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.html)
[ISketchArc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc_members.html)
[ISketchArc::GetNormalVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~GetNormalVector.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
