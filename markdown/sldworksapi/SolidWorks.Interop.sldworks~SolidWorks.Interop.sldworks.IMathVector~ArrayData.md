---
title: "ArrayData Property (IMathVector)"
project: "SOLIDWORKS API Help"
interface: "IMathVector"
member: "ArrayData"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~ArrayData.html"
---

# ArrayData Property (IMathVector)

Gets or sets the array of three doubles for this vector.

## Syntax

### Visual Basic (Declaration)

```vb
Property ArrayData As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMathVector
Dim value As System.Object

instance.ArrayData = value

value = instance.ArrayData
```

### C#

```csharp
System.object ArrayData {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ArrayData {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of three doubles

## VBA Syntax

See [MathVector::ArrayData](ms-its:sldworksapivb6.chm::/sldworks~MathVector~ArrayData.html).

## See Also

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.html)
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.html)
[IMathVector::IArrayData Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IArrayData.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
