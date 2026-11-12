---
title: "Scale2 Property (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "Scale2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Scale2.html"
---

# Scale2 Property (ISketchBlockInstance)

Sets the scale for this block instance.

## Syntax

### Visual Basic (Declaration)

```vb
Property Scale2 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
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

Scale: 0.0000001 to 500000 (see **Remarks**)

## VBA Syntax

See [SketchBlockInstance::Scale2](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~Scale2.html).

## Remarks

The getter of this property is obsolete. It has been superseded by [ISketchBlockInstance::GetScale3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetScale3.html).

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)

## Availability

SOLIDWORKS 2007 SP2, Revision Number 15.2
