---
title: "IGetArrowHeadInfo Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "IGetArrowHeadInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetArrowHeadInfo.html"
---

# IGetArrowHeadInfo Method (IWeldSymbol)

Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetArrowHeadInfo() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
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

- in-process, unmanaged C++: Pointer to an array of doubles (see Remarks)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The information returned is independent of whether this weld symbol has an arrowhead.

Format of return information is the following array of doubles:

retval[0] = arrow length (that is, leader into arrowhead)

retval[1] = arrowhead length

retval[2] = arrowhead width

retval[3] = arrowhead style as defined in [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)
[IWeldSymbol::GetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetArrowHeadAtIndex.html)
[IWeldSymbol::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetArrowHeadCount.html)
[IWeldSymbol::GetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetArrowHeadInfo.html)
[IWeldSymbol::IGetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetArrowHeadAtIndex.html)

## Availability

SOLIDWORKS 98Plus, datecode 1998319
