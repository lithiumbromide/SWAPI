---
title: "PrintCrossHatchOnOutOfDateViews Property (IPrintSpecification)"
project: "SOLIDWORKS API Help"
interface: "IPrintSpecification"
member: "PrintCrossHatchOnOutOfDateViews"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~PrintCrossHatchOnOutOfDateViews.html"
---

# PrintCrossHatchOnOutOfDateViews Property (IPrintSpecification)

Gets or sets whether to print a cross hatch on out-of-date views.

## Syntax

### Visual Basic (Declaration)

```vb
Property PrintCrossHatchOnOutOfDateViews As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPrintSpecification
Dim value As System.Boolean

instance.PrintCrossHatchOnOutOfDateViews = value

value = instance.PrintCrossHatchOnOutOfDateViews
```

### C#

```csharp
System.bool PrintCrossHatchOnOutOfDateViews {get; set;}
```

### C++/CLI

```cpp
property System.bool PrintCrossHatchOnOutOfDateViews {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to print a cross hatch on out-of-date views, false to not

## VBA Syntax

See [PrintSpecification::PrintCrossHatchOnOutOfDateViews](ms-its:sldworksapivb6.chm::/sldworks~PrintSpecification~PrintCrossHatchOnOutOfDateViews.html).

## Examples

See the [IPrintSpecification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPrintSpecification.html) examples.

## See Also

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.html)
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
