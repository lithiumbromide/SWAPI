---
title: "ScaleHatchPattern Property (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "ScaleHatchPattern"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ScaleHatchPattern.html"
---

# ScaleHatchPattern Property (IDrSection)

Gets or sets whether to scale the hatch pattern to the section view.

## Syntax

### Visual Basic (Declaration)

```vb
Property ScaleHatchPattern As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.Boolean

instance.ScaleHatchPattern = value

value = instance.ScaleHatchPattern
```

### C#

```csharp
System.bool ScaleHatchPattern {get; set;}
```

### C++/CLI

```cpp
property System.bool ScaleHatchPattern {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to scale the hatch pattern to the section view, false to not

## VBA Syntax

See [DrSection::ScaleHatchPattern](ms-its:sldworksapivb6.chm::/sldworks~DrSection~ScaleHatchPattern.html).

## Examples

[Scale Hatch Pattern to Section View (C#)](Scale_Hatch_Pattern_With_Section_View_Example_CSharp.htm)
[Scale Hatch Pattern to Section View (VB.NET)](Scale_Hatch_Pattern_With_Section_View_Example_VBNET.htm)
[Scale Hatch Pattern to Section View (VBA)](Scale_Hatch_Pattern_With_Section_View_Example_VB.htm)

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::GetAutoHatch Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetAutoHatch.html)
[IDrSection::SetAutoHatch Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetAutoHatch.html)
[IDrSection::RandomizeScale Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~RandomizeScale.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
