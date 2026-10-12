---
title: "CreateFeatureMgrWindowFromHandlex64 Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "CreateFeatureMgrWindowFromHandlex64"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrWindowFromHandlex64.html"
---

# CreateFeatureMgrWindowFromHandlex64 Method (IModelViewManager)

On 64-bit machines, creates a new view in the FeatureManager design tree using the specified .NET tab control.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFeatureMgrWindowFromHandlex64( _
   ByVal BitMapFile As System.String, _
   ByVal WindowHandle As System.Long, _
   ByVal ToolTip As System.String, _
   ByVal WhichPane As System.Integer _
) As FeatMgrView
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim BitMapFile As System.String
Dim WindowHandle As System.Long
Dim ToolTip As System.String
Dim WhichPane As System.Integer
Dim value As FeatMgrView

value = instance.CreateFeatureMgrWindowFromHandlex64(BitMapFile, WindowHandle, ToolTip, WhichPane)
```

### C#

```csharp
FeatMgrView CreateFeatureMgrWindowFromHandlex64(
   System.string BitMapFile,
   System.long WindowHandle,
   System.string ToolTip,
   System.int WhichPane
)
```

### C++/CLI

```cpp
FeatMgrView^ CreateFeatureMgrWindowFromHandlex64(
   System.String^ BitMapFile,
   System.int64 WindowHandle,
   System.String^ ToolTip,
   System.int WhichPane
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BitMapFile`: Fully qualified path to the bitmap file that you want to use for the control
- `WindowHandle`: Handle of the .NET tab control
- `ToolTip`: Text for the ToolTip
- `WhichPane`: Pane to use as defined in [swFeatMgrPane_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html)

### Return Value

[IFeatMgrView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatMgrView.html)

## VBA Syntax

See [ModelViewManager::CreateFeatureMgrWindowFromHandlex64](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~CreateFeatureMgrWindowFromHandlex64.html).

## Examples

[Add .NET Controls to SOLIDWORKS using an Add-in (C#)](Add_.NET_Controls_to_SOLIDWORKS_Using_an_Add-in_Example_CSharp.htm)
[Add .NET Controls to SOLIDWORKS using an Add-in (VB.NET)](Add_.NET_Controls_to_SolidWorks_Using_an_Add-in_Example_VBNET.htm)

## Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS Design software.

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelViewManager::DisplayWindowFromHandlex64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DisplayWindowFromHandlex64.html)
[IModelViewManager::CreateFeatureMgrWindowFromHandle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrWindowFromHandle.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
