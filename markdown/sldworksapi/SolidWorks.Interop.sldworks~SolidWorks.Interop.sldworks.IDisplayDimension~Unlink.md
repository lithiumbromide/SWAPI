---
title: "Unlink Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "Unlink"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Unlink.html"
---

# Unlink Method (IDisplayDimension)

Unlinks a previously linked display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function Unlink() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Integer

value = instance.Unlink()
```

### C#

```csharp
System.int Unlink()
```

### C++/CLI

```cpp
System.int Unlink();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Error code as defined by [swLinkDimensionError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLinkDimensionError_e.html)

## VBA Syntax

See [DisplayDimension::Unlink](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~Unlink.html).

## Examples

[Unlink Dimensions (VBA)](Unlink_Dimensions_Example_VB.htm)

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetLinkedText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetLinkedText.html)
[IDisplayDimension::SetLinkedText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLinkedText.html)
[IDisplayDimension::IsLinked Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsLinked.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
