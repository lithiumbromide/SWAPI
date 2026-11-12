---
title: "GetUseDocSecondArrow Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetUseDocSecondArrow"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocSecondArrow.html"
---

# GetUseDocSecondArrow Method (IDisplayDimension)

Gets whether this diameter display dimension uses the document default setting for the display of the second outside arrow.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUseDocSecondArrow() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

value = instance.GetUseDocSecondArrow()
```

### C#

```csharp
System.bool GetUseDocSecondArrow()
```

### C++/CLI

```cpp
System.bool GetUseDocSecondArrow();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this display dimension uses the document setting, false if it uses the local setting

## VBA Syntax

See [DisplayDimension::GetUseDocSecondArrow](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetUseDocSecondArrow.html).

## Remarks

For diameter dimensions, the second outside arrow is the arrow that appears on the opposite side of the arc from the dimension text. This occurs only when the text is outside of the arc.

This method determines whether this display dimension uses the default document setting for second arrow display.

This method applies only to diameter dimensions. If you execute this method for any other types of dimensions, SOLIDWORKS returns false.

Use [IDisplayDimension::SetSecondArrow](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetSecondArrow.html) to set this value.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::ArrowSide Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ArrowSide.html)
[IDisplayDimension::GetSecondArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetSecondArrow.html)

## Availability

SOLIDWORKS 99, datecode 1999207
