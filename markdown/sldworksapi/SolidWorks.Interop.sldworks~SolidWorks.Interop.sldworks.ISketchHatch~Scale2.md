---
title: "Scale2 Property (ISketchHatch)"
project: "SOLIDWORKS API Help"
interface: "ISketchHatch"
member: "Scale2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~Scale2.html"
---

# Scale2 Property (ISketchHatch)

Gets or sets the hatch pattern scale.

## Syntax

### Visual Basic (Declaration)

```vb
Property Scale2 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchHatch
Dim value As System.Double

instance.Scale2 = value

value = instance.Scale2
```

### C#

```csharp
System.double Scale2 {get; set;}
```

### C++/CLI

```cpp
property System.double Scale2 {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Hatch pattern scale

## VBA Syntax

See [SketchHatch::Scale2](ms-its:sldworksapivb6.chm::/sldworks~SketchHatch~Scale2.html).

## Examples

See the [ISketchHatch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html) examples.

## See Also

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html)
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
