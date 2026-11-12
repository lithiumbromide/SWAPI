---
title: "Name Property (IManipulator)"
project: "SOLIDWORKS API Help"
interface: "IManipulator"
member: "Name"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator~Name.html"
---

# Name Property (IManipulator)

Gets and sets the name of a manipulator.

## Syntax

### Visual Basic (Declaration)

```vb
Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IManipulator
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

Name of the manipulator

## VBA Syntax

See [Manipulator::Name](ms-its:sldworksapivb6.chm::/sldworks~Manipulator~Name.html).

## See Also

[IManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator.html)
[IManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
