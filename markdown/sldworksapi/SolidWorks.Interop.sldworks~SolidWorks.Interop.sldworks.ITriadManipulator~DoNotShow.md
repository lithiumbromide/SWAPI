---
title: "DoNotShow Property (ITriadManipulator)"
project: "SOLIDWORKS API Help"
interface: "ITriadManipulator"
member: "DoNotShow"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~DoNotShow.html"
---

# DoNotShow Property (ITriadManipulator)

Specifies which triad manipulator's control points to not show.

## Syntax

### Visual Basic (Declaration)

```vb
Property DoNotShow As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITriadManipulator
Dim value As System.Integer

instance.DoNotShow = value

value = instance.DoNotShow
```

### C#

```csharp
System.int DoNotShow {get; set;}
```

### C++/CLI

```cpp
property System.int DoNotShow {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Control points to not show as defined in [swTriadManipulatorDoNotShow_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTriadManipulatorDoNotShow_e.html)

## VBA Syntax

See [TriadManipulator::DoNotShow](ms-its:sldworksapivb6.chm::/sldworks~TriadManipulator~DoNotShow.html).

## See Also

[ITriadManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator.html)
[ITriadManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
