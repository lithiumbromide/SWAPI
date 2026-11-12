---
title: "GetControl Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "GetControl"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetControl.html"
---

# GetControl Method (IModelViewManager)

Gets the control associated with this model view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetControl( _
   ByVal Name As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim Name As System.String
Dim value As System.Object

value = instance.GetControl(Name)
```

### C#

```csharp
System.object GetControl(
   System.string Name
)
```

### C++/CLI

```cpp
System.Object^ GetControl(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the control

### Return Value

Control object

## VBA Syntax

See [ModelViewManager::GetControl](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~GetControl.html).

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelViewManager::IGetControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~IGetControl.html)
[IModelViewManager::ActivateControlTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ActivateControlTab.html)
[IModelViewManager::ActivateModelTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ActivateModelTab.html)
[IModelViewManager::AddControl3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl3.html)
[IModelViewManager::AddControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl.html)
[IModelViewManager::DeleteControlTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DeleteControlTab.html)
[IModelViewManager::IsControlTabActive Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~IsControlTabActive.html)
[IModelViewManager::IsModelTabActive Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~IsModelTabActive.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
