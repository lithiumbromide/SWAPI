---
title: "AddFeatureMgrView3x64 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "AddFeatureMgrView3x64"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddFeatureMgrView3x64.html"
---

# AddFeatureMgrView3x64 Method (IModelDocExtension)

Adds the specified tab to the FeatureManager design tree view in x64 applications.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddFeatureMgrView3x64( _
   ByRef Bitmap As System.Long, _
   ByRef AppView As System.Long, _
   ByVal ToolTip As System.String, _
   ByVal WhichPane As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Bitmap As System.Long
Dim AppView As System.Long
Dim ToolTip As System.String
Dim WhichPane As System.Integer
Dim value As System.Boolean

value = instance.AddFeatureMgrView3x64(Bitmap, AppView, ToolTip, WhichPane)
```

### C#

```csharp
System.bool AddFeatureMgrView3x64(
   ref System.long Bitmap,
   ref System.long AppView,
   System.string ToolTip,
   System.int WhichPane
)
```

### C++/CLI

```cpp
System.bool AddFeatureMgrView3x64(
   System.int64% Bitmap,
   System.int64% AppView,
   System.String^ ToolTip,
   System.int WhichPane
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Bitmap`: Pointer to the bitmap that you want to use for the FeatureManager design tree tab; the bitmap should be no larger than 16x18; this standard pointer is created by performing a New on Cbitmap
- `AppView`: Pointer to an existing view that you want to use as your FeatureManager design tree view. If you do not have an existing view, then use [IModelViewMgr::CreateFeatureMgrView2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.html), which returns a view handle
- `ToolTip`: Tooltip string
- `WhichPane`: Pane in which to add the view as defined in [swFeatMgrPane_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html)

### Return Value

True if the FeatureManager design tree view tab is added successfully, false if not

## VBA Syntax

See [ModelDocExtension::AddFeatureMgrView3x64](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~AddFeatureMgrView3x64.html).

## Remarks

See the Remarks in [IModelDoc2::AddFeatureMgrView3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddFeatureMgrView3.html) for more information about using this x64 method.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::ActivateFeatureMgrViewx64 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ActivateFeatureMgrViewx64.html)
[IModelDocExtension::DeActivateFeatureMgrViewx64 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeActivateFeatureMgrViewx64.html)

## Availability

SOLIDWORKS 2026 SP01, Revision Number 34.1
