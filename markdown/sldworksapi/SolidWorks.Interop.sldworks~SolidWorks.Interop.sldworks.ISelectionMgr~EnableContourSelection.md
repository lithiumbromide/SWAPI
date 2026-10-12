---
title: "EnableContourSelection Property (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "EnableContourSelection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~EnableContourSelection.html"
---

# EnableContourSelection Property (ISelectionMgr)

Enables and disables contour selection.

## Syntax

### Visual Basic (Declaration)

```vb
Property EnableContourSelection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim value As System.Boolean

instance.EnableContourSelection = value

value = instance.EnableContourSelection
```

### C#

```csharp
System.bool EnableContourSelection {get; set;}
```

### C++/CLI

```cpp
property System.bool EnableContourSelection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable contour selection, false to disable it

## VBA Syntax

See [SelectionMgr::EnableContourSelection](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~EnableContourSelection.html).

## Examples

[Enable Contour Selection (VBA)](Enable_Contour_Selection_Example_VB.htm)
[Enable Contour Selection (VB.NET)](Enable_Contour_Selection_Example_VBNET.htm)
[Enable Contour Selection (C#)](Enable_Contour_Selection_Example_CSharp.htm)

## Remarks

This property enables you to select regions that are defined by single, multiple, open, or closed sketch boundaries. See the SOLIDWORKS Help for more information about selecting contours.

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)
[ISelectionMgr::EnableSelection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~EnableSelection.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
