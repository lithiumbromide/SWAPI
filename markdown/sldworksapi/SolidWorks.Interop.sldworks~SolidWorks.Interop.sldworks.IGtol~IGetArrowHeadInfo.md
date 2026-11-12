---
title: "IGetArrowHeadInfo Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "IGetArrowHeadInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetArrowHeadInfo.html"
---

# IGetArrowHeadInfo Method (IGtol)

Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetArrowHeadInfo() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
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

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This information returned by this method is independent of whether this note actually has an arrowhead.

The format of the return information is the following array of doubles:

retval[0] = Arrow length (for example, leader into arrowhead)

retval[1] = Arrowhead length

retval[2] = Arrowhead width

retval[3] = Arrowhead style as defined in [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetArrowHeadAtIndex.html)
[IGtol::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetArrowHeadCount.html)
[IGtol::GetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetArrowHeadInfo.html)
[IGtol::IGetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetArrowHeadAtIndex.html)
