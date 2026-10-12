---
title: "IGetCoordinates Method (ISketchText)"
project: "SOLIDWORKS API Help"
interface: "ISketchText"
member: "IGetCoordinates"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~IGetCoordinates.html"
---

# IGetCoordinates Method (ISketchText)

Gets the position of this sketch text.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCoordinates() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchText
Dim value As System.Double

value = instance.IGetCoordinates()
```

### C#

```csharp
System.double IGetCoordinates()
```

### C++/CLI

```cpp
System.double IGetCoordinates();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of 3 double values, the x,y,z coordinate of the sketch text

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

To set the position of this sketch text, use [ISketchText::SetCoordinates](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchText~IGetCoordinates.html).

## See Also

[ISketchText Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.html)
[ISketchText Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText_members.html)
[ISketchText::GetCoordinates Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetCoordinates.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
