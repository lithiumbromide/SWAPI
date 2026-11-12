---
title: "IsDerived Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "IsDerived"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IsDerived.html"
---

# IsDerived Method (ISketch)

Gets whether a sketch is derived.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsDerived() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Boolean

value = instance.IsDerived()
```

### C#

```csharp
System.bool IsDerived()
```

### C++/CLI

```cpp
System.bool IsDerived();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the sketch is derived, false if not

## VBA Syntax

See [Sketch::IsDerived](ms-its:sldworksapivb6.chm::/sldworks~Sketch~IsDerived.html).

## Examples

[Create Derived or Underived Sketch (VB.NET)](Create_Derived_or_Underived_Sketch_Example_VBNET.htm)
[Create Derived or Underived Sketch (VBA)](Create_Derived_or_Underived_Sketch_Example_VB.htm)
[Create Derived or Underived Sketch (C#)](Create_Derived_or_Underived_Sketch_Example_CSharp.htm)

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[IModelDoc2::DeriveSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeriveSketch.html)
[IModelDoc2::UnderiveSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~UnderiveSketch.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
