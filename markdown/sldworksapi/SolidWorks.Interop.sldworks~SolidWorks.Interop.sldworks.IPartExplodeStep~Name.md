---
title: "Name Property (IPartExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IPartExplodeStep"
member: "Name"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~Name.html"
---

# Name Property (IPartExplodeStep)

Gets or sets the name of this explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPartExplodeStep
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

Name of this explode step

## VBA Syntax

See [PartExplodeStep::Name](ms-its:sldworksapivb6.chm::/sldworks~PartExplodeStep~Name.html).

## Examples

See the [IPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.html) example.

## See Also

[IPartExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.html)
[IPartExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
