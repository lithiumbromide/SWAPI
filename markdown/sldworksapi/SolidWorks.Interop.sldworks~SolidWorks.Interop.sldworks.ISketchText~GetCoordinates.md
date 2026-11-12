---
title: "GetCoordinates Method (ISketchText)"
project: "SOLIDWORKS API Help"
interface: "ISketchText"
member: "GetCoordinates"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetCoordinates.html"
---

# GetCoordinates Method (ISketchText)

Gets the position of this sketch text.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCoordinates() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchText
Dim value As System.Object

value = instance.GetCoordinates()
```

### C#

```csharp
System.object GetCoordinates()
```

### C++/CLI

```cpp
System.Object^ GetCoordinates();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of 3 double values, the x,y,z coordinate of the sketch text

## VBA Syntax

See [SketchText::GetCoordinates](ms-its:sldworksapivb6.chm::/sldworks~SketchText~GetCoordinates.html).

## Examples

See the [ISketchText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.html) examples.

## Remarks

To set the position of this sketch text, use [ISketchText::SetCoordinates](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchText~IGetCoordinates.html).

## See Also

[ISketchText Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.html)
[ISketchText Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText_members.html)
[ISketchText::IGetCoordinates Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~IGetCoordinates.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
