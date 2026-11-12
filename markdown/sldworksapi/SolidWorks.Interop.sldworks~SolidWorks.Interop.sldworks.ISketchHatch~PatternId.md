---
title: "PatternId Property (ISketchHatch)"
project: "SOLIDWORKS API Help"
interface: "ISketchHatch"
member: "PatternId"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~PatternId.html"
---

# PatternId Property (ISketchHatch)

Gets the pattern ID for this sketch hatch.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternId As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchHatch
Dim value As System.Integer

instance.PatternId = value

value = instance.PatternId
```

### C#

```csharp
System.int PatternId {get; set;}
```

### C++/CLI

```cpp
property System.int PatternId {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pattern ID as defined in install_dir\lang\language\SLDWRKS.PTN

## VBA Syntax

See [SketchHatch::PatternId](ms-its:sldworksapivb6.chm::/sldworks~SketchHatch~PatternId.html).

## See Also

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html)
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.html)
[ISketchHatch::Pattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~Pattern.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
