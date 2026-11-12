---
title: "ScaleToFit Property (IPageSetup)"
project: "SOLIDWORKS API Help"
interface: "IPageSetup"
member: "ScaleToFit"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~ScaleToFit.html"
---

# ScaleToFit Property (IPageSetup)

Enables or disables scaling the page to fit the printer.

## Syntax

### Visual Basic (Declaration)

```vb
Property ScaleToFit As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPageSetup
Dim value As System.Boolean

instance.ScaleToFit = value

value = instance.ScaleToFit
```

### C#

```csharp
System.bool ScaleToFit {get; set;}
```

### C++/CLI

```cpp
property System.bool ScaleToFit {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to scale page to fit the printer, false to not

## VBA Syntax

See [PageSetup::ScaleToFit](ms-its:sldworksapivb6.chm::/sldworks~PageSetup~ScaleToFit.html).

## Remarks

If this property is false, then you can use [IPageSetup::Scale2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPageSetup~Scale2.html) to set the scaling factor.

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
