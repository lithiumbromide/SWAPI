---
title: "Layername Property (IBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IBalloonOptions"
member: "Layername"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions~Layername.html"
---

# Layername Property (IBalloonOptions)

Gets and sets the name of the layer on which to create the balloon.

## Syntax

### Visual Basic (Declaration)

```vb
Property Layername As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonOptions
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

See [BalloonOptions::LayerName](ms-its:sldworksapivb6.chm::/sldworks~BalloonOptions~LayerName.html).

## Remarks

See the SOLIDWORKS Help for additional details about balloons.

## See Also

[IBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.html)
[IBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
