---
title: "SolidFill Property (ISketchHatch)"
project: "SOLIDWORKS API Help"
interface: "ISketchHatch"
member: "SolidFill"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~SolidFill.html"
---

# SolidFill Property (ISketchHatch)

Gets or sets whether to enable solid fill for the sketch hatch.

## Syntax

### Visual Basic (Declaration)

```vb
Property SolidFill As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchHatch
Dim value As System.Boolean

instance.SolidFill = value

value = instance.SolidFill
```

### C#

```csharp
System.bool SolidFill {get; set;}
```

### C++/CLI

```cpp
property System.bool SolidFill {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable solid fill, false to not

## VBA Syntax

See [SketchHatch::SolidFill](ms-its:sldworksapivb6.chm::/sldworks~SketchHatch~SolidFill.html).

## Examples

See the [ISketchHatch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html) examples.

## See Also

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html)
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
