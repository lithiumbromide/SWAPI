---
title: "GetSecondArrow Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetSecondArrow"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetSecondArrow.html"
---

# GetSecondArrow Method (IDisplayDimension)

Gets whether this diameter display dimension has the second arrow enabled.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSecondArrow() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

value = instance.GetSecondArrow()
```

### C#

```csharp
System.bool GetSecondArrow()
```

### C++/CLI

```cpp
System.bool GetSecondArrow();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the second arrow is displayed, false if the second arrow is not displayed (see **Remarks**)

## VBA Syntax

See [DisplayDimension::GetSecondArrow](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetSecondArrow.html).

## Remarks

For diameter dimensions, the second outside arrow is the arrow that appears on the opposite side of the arc from the dimension text. This occurs only when the text is outside of the arc.

Display of this arrow is optional, and is controlled by a value stored in one of two places: on the owning document or on the individual display dimension. Use [IDisplayDimension::GetUseDocSecondArrow](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetUseDocSecondArrow.html) to determine whether the document or the individual display dimension is controlling the second arrow display.

The return value from this method is not valid when the document is controlling the display of second arrows.

This method applies only to diameter dimensions. If this method is executed on any other type of dimension, SOLIDWORKS returns false.

Use [IDisplayDimension::SetSecondArrow](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetSecondArrow.html) to set the second arrow values.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetUseDocSecondArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocSecondArrow.html)
[IDisplayDimension::SetSecondArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetSecondArrow.html)
[IDisplayDimension::ArrowSide Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ArrowSide.html)

## Availability

SOLIDWORKS 99, datecode 1999207
