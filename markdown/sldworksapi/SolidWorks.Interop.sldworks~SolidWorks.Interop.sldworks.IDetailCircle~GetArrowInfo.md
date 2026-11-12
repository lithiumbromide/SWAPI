---
title: "GetArrowInfo Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "GetArrowInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetArrowInfo.html"
---

# GetArrowInfo Method (IDetailCircle)

Gets the position of the arrows for this detail circle.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArrowInfo() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim value As System.Object

value = instance.GetArrowInfo()
```

### C#

```csharp
System.object GetArrowInfo()
```

### C++/CLI

```cpp
System.Object^ GetArrowInfo();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array containing the arrow position information

## VBA Syntax

See [DetailCircle::GetArrowInfo](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~GetArrowInfo.html).

## Remarks

The section line in a drawing view has arrows at each end of the line. This method returns an array that contains 12 doubles, the (X, Y, Z) of the start and end point of one arrow, followed by the (X, Y, Z) of the start and end point of the other arrow.

These values match some of the information in the array returned by [IView::GetSectionLineInfo2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetSectionLineInfo2.html) and [IViewIGetSectionLineInfo2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetSectionLineInfo2.html); the arrow information near the middle of the array. The arrow information in that array also contains the arrow width, height, and style, which is not in the array returned by this method. To get this information using document preference settings, use [IModelDocExtension::GetUserPreferenceDouble](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceDouble.html) with swDetailingSectionArrowHeight, swDetailingSectionArrowWidth, or swDetailingSectionArrowLength, and [IModelDocExtension::GetUserPreferenceInteger](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.html) with swDetailingArrowStyleForDimensions.

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)
[IDetailCircle::IGetArrowInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~IGetArrowInfo.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
