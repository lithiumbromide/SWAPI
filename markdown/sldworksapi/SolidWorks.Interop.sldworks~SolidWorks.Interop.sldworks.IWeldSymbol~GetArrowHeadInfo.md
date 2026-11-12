---
title: "GetArrowHeadInfo Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "GetArrowHeadInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetArrowHeadInfo.html"
---

# GetArrowHeadInfo Method (IWeldSymbol)

Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArrowHeadInfo() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim value As System.Object

value = instance.GetArrowHeadInfo()
```

### C#

```csharp
System.object GetArrowHeadInfo()
```

### C++/CLI

```cpp
System.Object^ GetArrowHeadInfo();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [WeldSymbol::GetArrowHeadInfo](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~GetArrowHeadInfo.html).

## Remarks

This information returned by this method is independent of whether this weld symbol has an arrowhead.

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
[IWeldSymbol::IGetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetArrowHeadAtIndex.html)
[IWeldSymbol::IGetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetArrowHeadInfo.html)

## Availability

SOLIDWORKS 98Plus, datecode 1998319
