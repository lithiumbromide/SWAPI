---
title: "IMaterialPropertyValues Property (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IMaterialPropertyValues"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IMaterialPropertyValues.html"
---

# IMaterialPropertyValues Property (IBody)

Obsolete. Superseded by [IBody2::IMaterialPropertyValues2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IMaterialPropertyValues2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IMaterialPropertyValues As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim value As System.Double

instance.IMaterialPropertyValues = value

value = instance.IMaterialPropertyValues
```

### C#

```csharp
System.double IMaterialPropertyValues {get; set;}
```

### C++/CLI

```cpp
property System.double IMaterialPropertyValues {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Body::IMaterialPropertyValues](ms-its:sldworksapivb6.chm::/sldworks~Body~IMaterialPropertyValues.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
