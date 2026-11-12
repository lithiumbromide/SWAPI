---
title: "GetArrowHeadInfo Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetArrowHeadInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetArrowHeadInfo.html"
---

# GetArrowHeadInfo Method (IGtol)

Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArrowHeadInfo() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
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

Array (see **Remarks**)

## VBA Syntax

See [Gtol::GetArrowHeadInfo](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetArrowHeadInfo.html).

## Remarks

This information returned by this method is independent of whether this note actually has an arrowhead.

The format of the return value is the following array of doubles:

retval[0] = Arrow length (for example, leader into arrowhead)

retval[1] = Arrowhead length

retval[2] = Arrowhead width

retval[3] = Arrowhead style as defined in [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetArrowHeadAtIndex.html)
[IGtol::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetArrowHeadCount.html)
[IGtol::IGetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetArrowHeadAtIndex.html)
[IGtol::IGetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetArrowHeadInfo.html)
