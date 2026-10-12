---
title: "Cursor Property (ITriadManipulator)"
project: "SOLIDWORKS API Help"
interface: "ITriadManipulator"
member: "Cursor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~Cursor.html"
---

# Cursor Property (ITriadManipulator)

Sets the cursor to use when the pointer is over the triad manipulator.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property Cursor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITriadManipulator

instance.Cursor = value
```

### C#

```csharp
System.int Cursor {set;}
```

### C++/CLI

```cpp
property System.int Cursor {
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Cursor to use as defined by [swManipulatorCursor_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swManipulatorCursor_e.html)

## VBA Syntax

See [TriadManipulator::Cursor](ms-its:sldworksapivb6.chm::/sldworks~TriadManipulator~Cursor.html).

## See Also

[ITriadManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator.html)
[ITriadManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
