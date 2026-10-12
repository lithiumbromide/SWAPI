---
title: "TreeDisplay Property (IDimXpertManager)"
project: "SOLIDWORKS API Help"
interface: "IDimXpertManager"
member: "TreeDisplay"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager~TreeDisplay.html"
---

# TreeDisplay Property (IDimXpertManager)

Gets the organization of the DimXpertManager tab information: by annotation, by features, or flat.

## Syntax

### Visual Basic (Declaration)

```vb
Property TreeDisplay As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertManager
Dim value As System.Integer

instance.TreeDisplay = value

value = instance.TreeDisplay
```

### C#

```csharp
System.int TreeDisplay {get; set;}
```

### C++/CLI

```cpp
property System.int TreeDisplay {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of tree display as defined in [swDimXpertTreeDisplay_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimXpertTreeDisplay_e.html)

## VBA Syntax

See [DimXpertManager::TreeDisplay](ms-its:sldworksapivb6.chm::/sldworks~DimXpertManager~TreeDisplay.html).

## Examples

[Get DimXpertManager Info (VBA)](Get_DimXpertManager_Info_Example_VB.htm)
[Get DimXpertManager Info (VB.NET)](Get_DimXpertManager_Info_Example_VBNET.htm)

## Remarks

This property corresponds to a Tree Display menu item when the right-mouse-button is clicked on a schema in the DimXpertManager tab.

## See Also

[IDimXpertManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager.html)
[IDimXpertManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
