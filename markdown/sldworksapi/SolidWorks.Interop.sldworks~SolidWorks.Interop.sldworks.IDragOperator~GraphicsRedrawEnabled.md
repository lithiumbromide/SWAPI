---
title: "GraphicsRedrawEnabled Property (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "GraphicsRedrawEnabled"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~GraphicsRedrawEnabled.html"
---

# GraphicsRedrawEnabled Property (IDragOperator)

Gets or sets whether or not to update the graphics display after moving components.

## Syntax

### Visual Basic (Declaration)

```vb
Property GraphicsRedrawEnabled As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim value As System.Boolean

instance.GraphicsRedrawEnabled = value

value = instance.GraphicsRedrawEnabled
```

### C#

```csharp
System.bool GraphicsRedrawEnabled {get; set;}
```

### C++/CLI

```cpp
property System.bool GraphicsRedrawEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to update the graphics display after moving components, false to not

## VBA Syntax

See [DragOperator::GraphicsRedrawEnabled](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~GraphicsRedrawEnabled.html).

## Remarks

If this property is set to false, call [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) when you want to update the graphics display. This property is set to True by default.

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
