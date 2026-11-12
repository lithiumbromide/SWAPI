---
title: "IArrayData Property (IMathTransform)"
project: "SOLIDWORKS API Help"
interface: "IMathTransform"
member: "IArrayData"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IArrayData.html"
---

# IArrayData Property (IMathTransform)

Gets and sets the array of 16 doubles for this transform.

## Syntax

### Visual Basic (Declaration)

```vb
Property IArrayData As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMathTransform
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

- in-process, unmanaged C++: Pointer to an array of 16 doubles (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

The first 9 elements define the 3x3 rotation matrix. The next 3 elements define the translation component. The next element defines the scaling component. The last 3 elements are unused.

The array data argument should be in a form that allows the direct calling of methods such as [IComponent2::Transform2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~Transform2.html).

## See Also

[IMathTransform Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html)
[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
