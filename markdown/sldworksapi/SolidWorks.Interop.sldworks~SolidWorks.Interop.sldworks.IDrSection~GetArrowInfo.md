---
title: "GetArrowInfo Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "GetArrowInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetArrowInfo.html"
---

# GetArrowInfo Method (IDrSection)

Gets the position of the arrows for the section line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArrowInfo() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
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

Array of objects (see **Remarks**)

## VBA Syntax

See [DrSection::GetArrowInfo](ms-its:sldworksapivb6.chm::/sldworks~DrSection~GetArrowInfo.html).

## Remarks

The section line in a drawing view has arrows at each end of the line. This method returns an array that consists of 12 doubles, the (X, Y, Z) of the start and end point of one arrow followed by the (X, Y, Z) of the start and end point of the other arrow.

These values are the same as some of the information in the array returned by [IView::GetSectionLineInfo2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetSectionLineInfo2.html). The arrow information in that array also contains the arrow width, height and style. That information is not included in the array returned by this method, but you can get it from the document preference settings because these values are controlled only at the document level, not on an individual section line basis.

See:

- [IModelDocExtension::GetUserPreferenceDouble](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceDouble.html) with swDetailingSectionArrowHeight, swDetailingSectionArrowWidth, or swDetailingSectionArrowLength
- [IModelDocExtension::GetUserPreferenceInteger](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.html) with swDetailingArrowStyleForDimensions

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::IGetArrowInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetArrowInfo.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
