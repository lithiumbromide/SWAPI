---
title: "AddHorizontalDimension2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "AddHorizontalDimension2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddHorizontalDimension2.html"
---

# AddHorizontalDimension2 Method (IModelDoc2)

Creates a horizontal dimension for the currently selected entities at the specified location.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddHorizontalDimension2( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object

value = instance.AddHorizontalDimension2(X, Y, Z)
```

### C#

```csharp
System.object AddHorizontalDimension2(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.Object^ AddHorizontalDimension2(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: Dimension text location in meters
- `Y`: Dimension text location in meters
- `Z`: Dimension text location in meters

### Return Value

Newly created [dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html)

## VBA Syntax

See [ModelDoc2::AddHorizontalDimension2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~AddHorizontalDimension2.html).

## Examples

[Dimension Edge in Drawing (VBA)](Dimension_Edge_in_Drawing_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::AddDiameterDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddDiameterDimension2.html)
[IModelDoc2::AddDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddDimension2.html)
[IModelDoc2::AddRadialDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddRadialDimension2.html)
[IModelDoc2::AddVerticalDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddVerticalDimension2.html)
[IModelDoc2::IAddDiameterDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddDiameterDimension2.html)
[IModelDoc2::IAddDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddDimension2.html)
[IModelDoc2::IAddRadialDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddRadialDimension2.html)
[IModelDoc2::IAddVerticalDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddVerticalDimension2.html)
[IModelDoc2::IAddHorizontalDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddHorizontalDimension2.html)
[IModelDocExtension::AddSymmetricDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddSymmetricDimension.html)
[IModelDocExtension::AddSpecificDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddSpecificDimension.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
