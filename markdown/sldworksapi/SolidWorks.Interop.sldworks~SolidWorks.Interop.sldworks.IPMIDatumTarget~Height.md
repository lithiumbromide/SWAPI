---
title: "Height Property (IPMIDatumTarget)"
project: "SOLIDWORKS API Help"
interface: "IPMIDatumTarget"
member: "Height"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget~Height.html"
---

# Height Property (IPMIDatumTarget)

Gets the PMI datum target height.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Height As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDatumTarget
Dim value As System.Double

instance.Height = value

value = instance.Height
```

### C#

```csharp
System.double Height {get; set;}
```

### C++/CLI

```cpp
property System.double Height {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Datum target height

## VBA Syntax

See [PMIDatumTarget::Height](ms-its:sldworksapivb6.chm::/sldworks~PMIDatumTarget~Height.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## Remarks

This property is valid only if [IPMIDatumTarget::AreaStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget~AreaStyle.html) is set to [swPMIDatumTargetAreaStyle_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMIDatumTargetAreaStyle_e.html).swPMIDatumTargetAreaStyle_Rectangular.

## See Also

[IPMIDatumTarget Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget.html)
[IPMIDatumTarget Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget_members.html)
[IPMIDatumTarget::Unit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget~Unit.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
