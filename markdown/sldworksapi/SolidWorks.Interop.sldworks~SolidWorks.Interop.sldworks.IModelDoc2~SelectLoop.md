---
title: "SelectLoop Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SelectLoop"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectLoop.html"
---

# SelectLoop Method (IModelDoc2)

Selects the loop that corresponds to the selected edge.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SelectLoop()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.SelectLoop()
```

### C#

```csharp
void SelectLoop()
```

### C++/CLI

```cpp
void SelectLoop();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::SelectLoop](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SelectLoop.html).

## Remarks

This method associates the loop with the selected edge in the [ISelectionMgr](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr.html); it does not add an item to the ISelectionMgr. To find out if the selected edge has an associated loop, use [ISelectionMgr::GetSelectedObjectLoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
