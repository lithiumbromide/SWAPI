---
title: "IAddHoleCallout2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "IAddHoleCallout2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IAddHoleCallout2.html"
---

# IAddHoleCallout2 Method (IDrawingDoc)

Adds a hole callout at the specified position to the hole whose edge is selected.

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddHoleCallout2( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As DisplayDimension
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As DisplayDimension

value = instance.IAddHoleCallout2(X, Y, Z)
```

### C#

```csharp
DisplayDimension IAddHoleCallout2(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
DisplayDimension^ IAddHoleCallout2(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X position of hole callout in meters
- `Y`: Y position of hole callout in meters
- `Z`: Z position of hole callout in meters

### Return Value

Pointer to [DisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html) object representing the hole callout

## VBA Syntax

See [DrawingDoc::IAddHoleCallout2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~IAddHoleCallout2.html).

## Remarks

When you call this method, the user must click OK in the dialog that shows the system-generated hole callout.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDisplayDimension::IsHoleCallout Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsHoleCallout.html)
[IDrawingDoc::AddHoleCallout2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddHoleCallout2.html)
[IDisplayDimension::GetHoleCalloutVariables Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetHoleCalloutVariables.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
