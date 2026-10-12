---
title: "MaterialPropertyValues Property (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "MaterialPropertyValues"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~MaterialPropertyValues.html"
---

# MaterialPropertyValues Property (IBody)

Obsolete. Superseded by [IBody2::MaterialPropertyValues2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~MaterialPropertyValues2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialPropertyValues As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim value As System.Object

instance.MaterialPropertyValues = value

value = instance.MaterialPropertyValues
```

### C#

```csharp
System.object MaterialPropertyValues {get; set;}
```

### C++/CLI

```cpp
property System.Object^ MaterialPropertyValues {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Body::MaterialPropertyValues](ms-its:sldworksapivb6.chm::/sldworks~Body~MaterialPropertyValues.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
