---
title: "ExplementaryAngle Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "ExplementaryAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExplementaryAngle.html"
---

# ExplementaryAngle Method (IDisplayDimension)

Flips an angular dimension to its explementary angle.

## Syntax

### Visual Basic (Declaration)

```vb
Function ExplementaryAngle() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

value = instance.ExplementaryAngle()
```

### C#

```csharp
System.bool ExplementaryAngle()
```

### C++/CLI

```cpp
System.bool ExplementaryAngle();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if successful, false if not

## VBA Syntax

See [DisplayDimension::ExplementaryAngle](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~ExplementaryAngle.html).

## Examples

[Create Angular Dimension (VBA)](Create_Angular_Dimension_Example_VB.htm)
[Create Angular Dimension (VB.NET)](Create_Angular_Dimension_Example_VBNET.htm)
[Create Angular Dimension (C#)](Create_Angular_Dimension_Example_CSharp.htm)

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::VerticallyOppositeAngle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~VerticallyOppositeAngle.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
