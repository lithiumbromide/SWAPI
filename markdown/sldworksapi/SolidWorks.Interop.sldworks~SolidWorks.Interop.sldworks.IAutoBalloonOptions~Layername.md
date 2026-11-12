---
title: "Layername Property (IAutoBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IAutoBalloonOptions"
member: "Layername"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~Layername.html"
---

# Layername Property (IAutoBalloonOptions)

Gets and sets the name of the layer on which to create balloons.

## Syntax

### Visual Basic (Declaration)

```vb
Property Layername As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoBalloonOptions
Dim value As System.String

instance.Layername = value

value = instance.Layername
```

### C#

```csharp
System.string Layername {get; set;}
```

### C++/CLI

```cpp
property System.String^ Layername {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Layer name

## VBA Syntax

See [AutoBalloonOptions::LayerName](ms-its:sldworksapivb6.chm::/sldworks~AutoBalloonOptions~LayerName.html).

## Examples

See [IAutoBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAutoBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about autoballoons.

## See Also

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.html)
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
