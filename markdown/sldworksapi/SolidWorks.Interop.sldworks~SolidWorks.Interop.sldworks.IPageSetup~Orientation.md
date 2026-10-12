---
title: "Orientation Property (IPageSetup)"
project: "SOLIDWORKS API Help"
interface: "IPageSetup"
member: "Orientation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~Orientation.html"
---

# Orientation Property (IPageSetup)

Gets or sets the page orientation.

## Syntax

### Visual Basic (Declaration)

```vb
Property Orientation As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPageSetup
Dim value As System.Integer

instance.Orientation = value

value = instance.Orientation
```

### C#

```csharp
System.int Orientation {get; set;}
```

### C++/CLI

```cpp
property System.int Orientation {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Page orientation as defined in [swPageSetupOrientation_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPageSetupOrientation_e.html)

## VBA Syntax

See [PageSetup::Orientation](ms-its:sldworksapivb6.chm::/sldworks~PageSetup~Orientation.html).

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
