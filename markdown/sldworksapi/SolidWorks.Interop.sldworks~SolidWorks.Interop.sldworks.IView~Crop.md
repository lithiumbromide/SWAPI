---
title: "Crop Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "Crop"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Crop.html"
---

# Crop Method (IView)

Obsolete. Superseded by [IView::Crop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Crop2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Crop() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.Crop()
```

### C#

```csharp
System.int Crop()
```

### C++/CLI

```cpp
System.int Crop();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Crop view status as defined in [swCropViewErrors_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCropViewErrors_e.html)

## VBA Syntax

See [View::Crop](ms-its:sldworksapivb6.chm::/sldworks~View~Crop.html).

## Examples

[Crop View (VBA)](Crop_View_Example_VB.htm)
[Crop View (VB.NET)](Crop_View_Example_VBNET.htm)
[Crop View (C#)](Crop_View_Example_CSharp.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
