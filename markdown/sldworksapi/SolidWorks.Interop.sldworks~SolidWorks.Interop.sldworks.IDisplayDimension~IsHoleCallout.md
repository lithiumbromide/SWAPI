---
title: "IsHoleCallout Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "IsHoleCallout"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsHoleCallout.html"
---

# IsHoleCallout Method (IDisplayDimension)

Gets whether this display dimension is a hole callout.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsHoleCallout() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

value = instance.IsHoleCallout()
```

### C#

```csharp
System.bool IsHoleCallout()
```

### C++/CLI

```cpp
System.bool IsHoleCallout();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the display dimension is a hole callout, false if not

## VBA Syntax

See [DisplayDimension::IsHoleCallout](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~IsHoleCallout.html).

## Examples

[Get Whether Display Dimension is a Hole Callout (VBA)](Get_Whether_Display_Dimension_is_a_Hole_Callout_Example_VB.htm)

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDrawingDoc::AddHoleCallout2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddHoleCallout2.html)
[IDrawingDoc::IAddHoleCallout2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IAddHoleCallout2.html)
[IDisplayDimension::GetHoleCalloutVariables Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetHoleCalloutVariables.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
