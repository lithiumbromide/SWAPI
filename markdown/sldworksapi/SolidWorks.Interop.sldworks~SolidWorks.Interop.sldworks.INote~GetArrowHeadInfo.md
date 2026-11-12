---
title: "GetArrowHeadInfo Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetArrowHeadInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetArrowHeadInfo.html"
---

# GetArrowHeadInfo Method (INote)

Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArrowHeadInfo() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As INote
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

See [Note::GetArrowHeadInfo](ms-its:sldworksapivb6.chm::/sldworks~Note~GetArrowHeadInfo.html).

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
[INote::GetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetArrowHeadAtIndex.html)
[INote::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetArrowHeadCount.html)
[INote::IGetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetArrowHeadAtIndex.html)
[INote::IGetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetArrowHeadInfo.html)
