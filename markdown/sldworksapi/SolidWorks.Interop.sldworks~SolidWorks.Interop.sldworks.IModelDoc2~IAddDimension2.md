---
title: "IAddDimension2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IAddDimension2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddDimension2.html"
---

# IAddDimension2 Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::AddDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDimension.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddDimension2( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As DisplayDimension
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As DisplayDimension

value = instance.IAddDimension2(X, Y, Z)
```

### C#

```csharp
DisplayDimension IAddDimension2(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
DisplayDimension^ IAddDimension2(
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

See [ModelDoc2::IAddDimension2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IAddDimension2.html).

## Remarks

You should only use this method on the visible document. Before using this method, you can check to see if the document is visible by using [ISldWorks::Visible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~Visible.html).

Dimensions are created based on selection location. For example, creating an angular dimension between two lines gets different results based on which line endpoints are selected. Therefore, if you are using [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select the entities for dimensioning, then you should specify the XYZ selection coordinates. You must also leave the object name argument empty, because if you pass the object name to IModelDocExtension::SelectByID2, then the selection routines tries to locate that item without using the coordinates.

Because coordinates are ignored when the object name is passed, the dimensioning routines are not able to use a specific selection location for the dimension. This causes unpredictable results in your dimension creation because you cannot be sure which line endpoint is selected by IModelDocExtension::SelectByID2.

When you use this method, you might also want to use [ISldWorks::SetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html) swInputDimValOnCreate to suppress the dialog box that lets the user enter the dimension value.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::AddDiameterDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddDiameterDimension2.html)
[IModelDoc2::AddDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddDimension2.html)
[IModelDoc2::AddHorizontalDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddHorizontalDimension2.html)
[IModelDoc2::AddRadialDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddRadialDimension2.html)
[IModelDoc2::AddVerticalDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddVerticalDimension2.html)
[IModelDoc2::IAddDiameterDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddDiameterDimension2.html)
[IModelDoc2::IAddHorizontalDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddHorizontalDimension2.html)
[IModelDoc2::IAddRadialDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddRadialDimension2.html)
[IModelDoc2::IAddVerticalDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddVerticalDimension2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
