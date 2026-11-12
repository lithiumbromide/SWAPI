---
title: "MovableStyle Property (IPMIDatumTarget)"
project: "SOLIDWORKS API Help"
interface: "IPMIDatumTarget"
member: "MovableStyle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget~MovableStyle.html"
---

# MovableStyle Property (IPMIDatumTarget)

Gets the movable style of this PMI datum target.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property MovableStyle As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDatumTarget
Dim value As System.Integer

instance.MovableStyle = value

value = instance.MovableStyle
```

### C#

```csharp
System.int MovableStyle {get; set;}
```

### C++/CLI

```cpp
property System.int MovableStyle {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Movable style as defined in [swPMIDatumTargetMovableStyle_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMIDatumTargetMovableStyle_e.html)

## VBA Syntax

See [PMIDatumTarget::MovableStyle](ms-its:sldworksapivb6.chm::/sldworks~PMIDatumTarget~MovableStyle.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIDatumTarget Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget.html)
[IPMIDatumTarget Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
