---
title: "Status Property (ISketchPoint)"
project: "SOLIDWORKS API Help"
interface: "ISketchPoint"
member: "Status"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Status.html"
---

# Status Property (ISketchPoint)

Gets or sets the status of the associated relation for this sketch point.

## Syntax

### Visual Basic (Declaration)

```vb
Property Status As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPoint
Dim value As System.Integer

instance.Status = value

value = instance.Status
```

### C#

```csharp
System.int Status {get; set;}
```

### C++/CLI

```cpp
property System.int Status {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Sketch point relation status as defined in [swConstrainedStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstrainedStatus_e.html)

## VBA Syntax

See [SketchPoint::Status](ms-its:sldworksapivb6.chm::/sldworks~SketchPoint~Status.html).

## See Also

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
