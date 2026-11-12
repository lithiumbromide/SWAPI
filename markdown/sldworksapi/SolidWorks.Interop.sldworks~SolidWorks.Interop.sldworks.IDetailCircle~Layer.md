---
title: "Layer Property (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "Layer"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~Layer.html"
---

# Layer Property (IDetailCircle)

Gets or sets the layer on which the detail circle is on.

## Syntax

### Visual Basic (Declaration)

```vb
Property Layer As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
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

Layer name

## VBA Syntax

See [DetailCircle::Layer](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~Layer.html).

## Remarks

An empty string indicates no layer. If you set the layer to a layer name that does not exist, nothing happens.

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
