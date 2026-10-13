---
title: "CreateFeatureMgrView Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "CreateFeatureMgrView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrView.html"
---

# CreateFeatureMgrView Method (IModelViewManager)

Obsolete. Superseded by [IModelViewManager::CreateFeatureMgrView2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFeatureMgrView( _
   ByVal PPicture As System.Object, _
   ByVal ToolTip As System.String, _
   ByVal WhichPane As System.Integer _
) As FeatMgrView
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim PPicture As System.Object
Dim ToolTip As System.String
Dim WhichPane As System.Integer
Dim value As FeatMgrView

value = instance.CreateFeatureMgrView(PPicture, ToolTip, WhichPane)
```

### C#

```csharp
FeatMgrView CreateFeatureMgrView(
   System.object PPicture,
   System.string ToolTip,
   System.int WhichPane
)
```

### C++/CLI

```cpp
FeatMgrView^ CreateFeatureMgrView(
   System.Object^ PPicture,
   System.String^ ToolTip,
   System.int WhichPane
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PPicture`:
- `ToolTip`:
- `WhichPane`:

## VBA Syntax

See [ModelViewManager::CreateFeatureMgrView](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~CreateFeatureMgrView.html).

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
