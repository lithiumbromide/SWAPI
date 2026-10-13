---
title: "ModelViewManager Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ModelViewManager"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ModelViewManager.html"
---

# ModelViewManager Property (IModelDoc2)

Gets the [IModelViewManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager.html) object, which allows access to the model view.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ModelViewManager As ModelViewManager
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As ModelViewManager

value = instance.ModelViewManager
```

### C#

```csharp
ModelViewManager ModelViewManager {get;}
```

### C++/CLI

```cpp
property ModelViewManager^ ModelViewManager {
   ModelViewManager^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::ModelViewManager](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ModelViewManager.html).

## Examples

[Create Drag Arrow Manipulator (VBA)](Create_Drag_Arrow_Manipulator_Example_VB.htm)
[Set Viewports (C#)](Set_Viewports_Example_CSharp.htm)
[Set Viewports (VB.NET)](Set_Viewports_Example_VBNET.htm)
[Set Viewports (VBA)](Set_Viewports_Example_VB.htm)
[Add ActiveX Tabs to Model View (C#)](Add_ActiveX_Tabs_to_Model_View_Example_CSharp.htm)
[Add ActiveX Tabs to Model View (VB.NET)](Add_ActiveX_Tabs_to_Model_View_Example_VBNET.htm)
[Add ActiveX Tabs to Model View (VBA)](Add_ActiveX_Tabs_to_Model_View_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
