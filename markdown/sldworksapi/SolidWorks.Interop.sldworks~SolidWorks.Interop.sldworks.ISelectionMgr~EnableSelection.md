---
title: "EnableSelection Property (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "EnableSelection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~EnableSelection.html"
---

# EnableSelection Property (ISelectionMgr)

Enables or disables selection.

## Syntax

### Visual Basic (Declaration)

```vb
Property EnableSelection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim value As System.Boolean

instance.EnableSelection = value

value = instance.EnableSelection
```

### C#

```csharp
System.bool EnableSelection {get; set;}
```

### C++/CLI

```cpp
property System.bool EnableSelection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if selection is enabled, false if disabled

## VBA Syntax

See [SelectionMgr::EnableSelection](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~EnableSelection.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)
[ISelectionMgr::EnableContourSelection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~EnableContourSelection.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
