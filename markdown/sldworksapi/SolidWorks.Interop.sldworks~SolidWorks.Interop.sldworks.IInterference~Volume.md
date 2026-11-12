---
title: "Volume Property (IInterference)"
project: "SOLIDWORKS API Help"
interface: "IInterference"
member: "Volume"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~Volume.html"
---

# Volume Property (IInterference)

Gets the volume of the interference.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Volume As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IInterference
Dim value As System.Double

value = instance.Volume
```

### C#

```csharp
System.double Volume {get;}
```

### C++/CLI

```cpp
property System.double Volume {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Volume of the interference

## VBA Syntax

See [Interference::Volume](ms-its:sldworksapivb6.chm::/sldworks~Interference~Volume.html).

## Examples

[Run Interference Detection (C#)](Run_Interference_Detection_Example_CSharp.htm)
[Run Interference Detection (VB.NET)](Run_Interference_Detection_Example_VBNET.htm)
[Run Interference Detection (VBA)](Run_Interference_Detection_Example_VB.htm)

## See Also

[IInterference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference.html)
[IInterference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
