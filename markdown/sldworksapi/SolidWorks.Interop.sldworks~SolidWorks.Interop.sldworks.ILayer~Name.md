---
title: "Name Property (ILayer)"
project: "SOLIDWORKS API Help"
interface: "ILayer"
member: "Name"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~Name.html"
---

# Name Property (ILayer)

Gets and sets the name of this layer.

## Syntax

### Visual Basic (Declaration)

```vb
Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ILayer
Dim value As System.String

instance.Name = value

value = instance.Name
```

### C#

```csharp
System.string Name {get; set;}
```

### C++/CLI

```cpp
property System.String^ Name {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Layer name

## VBA Syntax

See [Layer::Name](ms-its:sldworksapivb6.chm::/sldworks~Layer~Name.html).

## See Also

[ILayer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.html)
[ILayer Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
