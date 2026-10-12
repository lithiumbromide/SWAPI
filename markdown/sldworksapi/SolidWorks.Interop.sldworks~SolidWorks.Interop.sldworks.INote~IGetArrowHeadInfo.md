---
title: "IGetArrowHeadInfo Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "IGetArrowHeadInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetArrowHeadInfo.html"
---

# IGetArrowHeadInfo Method (INote)

Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetArrowHeadInfo() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Double

value = instance.IGetArrowHeadInfo()
```

### C#

```csharp
System.double IGetArrowHeadInfo()
```

### C++/CLI

```cpp
System.double IGetArrowHeadInfo();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This information is independent of whether this note actually has an arrowhead.

This method returns an array of doubles that describe the geometry of the arrowhead on the far end of the leader line.

Format of return information is the following array of doubles:

- return value[0] = arrow length (i.e. leader into arrowhead)
- return value[1] = arrowhead length
- return value[2] = arrowhead width
- return value[3] = arrowhead style as defined in [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::IGetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetArrowHeadAtIndex.html)
[INote::GetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetArrowHeadAtIndex.html)
[INote::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetArrowHeadCount.html)
[INote::GetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetArrowHeadInfo.html)
