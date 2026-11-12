---
title: "IArrayData Property (IMathVector)"
project: "SOLIDWORKS API Help"
interface: "IMathVector"
member: "IArrayData"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IArrayData.html"
---

# IArrayData Property (IMathVector)

Gets or sets the array of three doubles for this vector.

## Syntax

### Visual Basic (Declaration)

```vb
Property IArrayData As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMathVector
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

- in-process, unmanaged C++: Pointerto an array of three doubles

VBA, VB.NET, C#, and C++/CLI: Not supported

## See Also

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.html)
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.html)
[IMathVector::ArrayData Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~ArrayData.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
