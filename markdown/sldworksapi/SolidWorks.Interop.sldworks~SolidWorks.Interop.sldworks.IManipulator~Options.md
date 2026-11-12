---
title: "Options Property (IManipulator)"
project: "SOLIDWORKS API Help"
interface: "IManipulator"
member: "Options"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator~Options.html"
---

# Options Property (IManipulator)

Gets or sets whether the manipulator is deleted when a component in an assembly is modified or deleted.

## Syntax

### Visual Basic (Declaration)

```vb
Property Options As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IManipulator
Dim value As System.Integer

instance.Options = value

value = instance.Options
```

### C#

```csharp
System.int Options {get; set;}
```

### C++/CLI

```cpp
property System.int Options {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Option as defined in [swManipulatorOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swManipulatorOptions_e.html) (see **Remarks**)

## VBA Syntax

See [Manipulator::Options](ms-its:sldworksapivb6.chm::/sldworks~Manipulator~Options.html).

## Remarks

SOLIDWORKS recommends setting this property to swManipulatorOpts_KeepAfterComponentModify when working in an assembly.

## See Also

[IManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator.html)
[IManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator_members.html)

## Availability

SOLIDWORKS 2009 SP2, Revision Number 17.2
