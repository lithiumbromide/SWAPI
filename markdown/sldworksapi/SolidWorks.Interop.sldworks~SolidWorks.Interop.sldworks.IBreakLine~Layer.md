---
title: "Layer Property (IBreakLine)"
project: "SOLIDWORKS API Help"
interface: "IBreakLine"
member: "Layer"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~Layer.html"
---

# Layer Property (IBreakLine)

Gets or sets the layer for this break line in the drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Property Layer As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBreakLine
Dim value As System.String

instance.Layer = value

value = instance.Layer
```

### C#

```csharp
System.string Layer {get; set;}
```

### C++/CLI

```cpp
property System.String^ Layer {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the layer

## VBA Syntax

See [BreakLine::Layer](ms-its:sldworksapivb6.chm::/sldworks~BreakLine~Layer.html).

## Remarks

An empty string indicates no layer. If you set the layer to a layer name that does not exist, nothing happens.

## See Also

[IBreakLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine.html)
[IBreakLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
