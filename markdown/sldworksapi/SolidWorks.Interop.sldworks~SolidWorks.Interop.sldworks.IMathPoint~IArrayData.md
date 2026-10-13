---
title: "IArrayData Property (IMathPoint)"
project: "SOLIDWORKS API Help"
interface: "IMathPoint"
member: "IArrayData"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~IArrayData.html"
---

# IArrayData Property (IMathPoint)

Gets or sets the array of x,y,z coordinates that describe this math point.

## Syntax

### Visual Basic (Declaration)

```vb
Property IArrayData As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMathPoint
Dim value As System.Double

instance.IArrayData = value

value = instance.IArrayData
```

### C#

```csharp
System.double IArrayData {get; set;}
```

### C++/CLI

```cpp
property System.double IArrayData {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

- in-process, unmanaged C++: Pointer to an array of 3 doubles representing the x,y,z coordinates of the math point

VBA, VB.NET, C#, and C++/CLI: Not supported

## See Also

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.html)
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.html)
[IMathPoint::ArrayData Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~ArrayData.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
