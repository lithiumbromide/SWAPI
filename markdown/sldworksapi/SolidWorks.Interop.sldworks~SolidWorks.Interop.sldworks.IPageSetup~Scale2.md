---
title: "Scale2 Property (IPageSetup)"
project: "SOLIDWORKS API Help"
interface: "IPageSetup"
member: "Scale2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~Scale2.html"
---

# Scale2 Property (IPageSetup)

Gets or sets the scale for printing the page.

## Syntax

### Visual Basic (Declaration)

```vb
Property Scale2 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPageSetup
Dim value As System.Double

instance.Scale2 = value

value = instance.Scale2
```

### C#

```csharp
System.double Scale2 {get; set;}
```

### C++/CLI

```cpp
property System.double Scale2 {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Print scale factor from 1% to 1000%

## VBA Syntax

See [PageSetup::Scale2](ms-its:sldworksapivb6.chm::/sldworks~PageSetup~Scale2.html).

## Remarks

This value is only used when [IPageSetup::ScaleToFit](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPageSetup~ScaleToFit.html) is set to false.

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
