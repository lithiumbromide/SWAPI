---
title: "Pattern Property (ISketchHatch)"
project: "SOLIDWORKS API Help"
interface: "ISketchHatch"
member: "Pattern"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~Pattern.html"
---

# Pattern Property (ISketchHatch)

Gets or sets the hatch pattern (also called type or name) of the sketch hatch (for example, "Stars" or "Honeycomb"), which is a string from the **sldwks.ptn** file.

## Syntax

### Visual Basic (Declaration)

```vb
Property Pattern As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchHatch
Dim value As System.String

instance.Pattern = value

value = instance.Pattern
```

### C#

```csharp
System.string Pattern {get; set;}
```

### C++/CLI

```cpp
property System.String^ Pattern {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the hatch pattern

## VBA Syntax

See [SketchHatch::Pattern](ms-its:sldworksapivb6.chm::/sldworks~SketchHatch~Pattern.html).

## Examples

See the [ISketchHatch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html) examples.

## See Also

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html)
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.html)
[ISketchHatch::PatternId Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~PatternId.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
