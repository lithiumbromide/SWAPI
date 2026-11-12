---
title: "IGetLineInfo Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "IGetLineInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetLineInfo.html"
---

# IGetLineInfo Method (IDrSection)

Gets the vertices of the section line.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetLineInfo() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.Double

value = instance.IGetLineInfo()
```

### C#

```csharp
System.double IGetLineInfo()
```

### C++/CLI

```cpp
System.double IGetLineInfo();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This method returns an array that consists of several coordinate pairs. The number of coordinate pairs is determined by the number of line segments in the section line.

Call [DrSection::IGetLineSegmentCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection~IGetLineSegmentCount.html) and multiply that number by 6 to get the size for the array. Each coordinate pair consists of 6 doubles, the (X, Y, Z) coordinate of each end point of the segment.

These values are the same as some of the information in the array returned by the[IView::IGetSectionLineInfo2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetSectionLineInfo2.html). The line segment information in that array also contains the line style. The array returned by this method does not contain that information because it is a document-level setting, and cannot be controlled per section line. Use [IModelDocExtension::GetUserPreferenceInteger](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.html) or [IModelDocExtension::SetUserPreferenceInteger](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SetUserPreferenceInteger.html) with swLineFontSectionLineStyle to get or set that value.

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::GetLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetLineInfo.html)
[IDrSection::ISetLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ISetLineInfo.html)
[IDrSection::SetLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetLineInfo.html)
[IView::EnumSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumSectionLines.html)
[IView::GetSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLines.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
