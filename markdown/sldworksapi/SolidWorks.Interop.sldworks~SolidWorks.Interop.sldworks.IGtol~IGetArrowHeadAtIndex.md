---
title: "IGetArrowHeadAtIndex Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "IGetArrowHeadAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetArrowHeadAtIndex.html"
---

# IGetArrowHeadAtIndex Method (IGtol)

Gets information on the specified arrow head in this GTol.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetArrowHeadAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim Index As System.Integer
Dim value As System.Double

value = instance.IGetArrowHeadAtIndex(Index)
```

### C#

```csharp
System.double IGetArrowHeadAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double IGetArrowHeadAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of the arrow head

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The return value is an array of doubles in the following format:

[ arrowHeadPt[3], arrowHeadDir[3], arrowHeadWidth, arrowHeadHeight, arrowHeadStyle ]

where:

| arrowHeadPt [3] | XYZ arrow head tip location |
| --- | --- |
| arrowHeadDir [3] | XYZ arrow head direction |
| arrowHeadWidth | Arrow head width where the width is measured along the arrow head direction |
| arrowHeadHeight | Arrow head height |
| arrowHeadStyle | Arrow head style as defined in swArrowStyle_e |

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetArrowHeadAtIndex.html)
[IGtol::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetArrowHeadCount.html)
[IGtol::GetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetArrowHeadInfo.html)
[IGtol::IGetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetArrowHeadInfo.html)
