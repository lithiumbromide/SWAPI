---
title: "AddFeatureMgrView3 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "AddFeatureMgrView3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddFeatureMgrView3.html"
---

# AddFeatureMgrView3 Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::AddFeatureMgrView3x64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddFeatureMgrView3x64.html).

This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016.

The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used.

Adds the specified tab to the FeatureManager design tree view.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddFeatureMgrView3( _
   ByRef Bitmap As System.Integer, _
   ByRef AppView As System.Integer, _
   ByVal ToolTip As System.String, _
   ByVal WhichPane As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Bitmap As System.Integer
Dim AppView As System.Integer
Dim ToolTip As System.String
Dim WhichPane As System.Integer
Dim value As System.Boolean

value = instance.AddFeatureMgrView3(Bitmap, AppView, ToolTip, WhichPane)
```

### C#

```csharp
System.bool AddFeatureMgrView3(
   ref System.int Bitmap,
   ref System.int AppView,
   System.string ToolTip,
   System.int WhichPane
)
```

### C++/CLI

```cpp
System.bool AddFeatureMgrView3(
   System.int% Bitmap,
   System.int% AppView,
   System.String^ ToolTip,
   System.int WhichPane
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Bitmap`: Pointer to the bitmap that you want to use for the FeatureManager design tree tab; the bitmap should be no larger than 16x18; this standard pointer is created by performing a New on Cbitmap
- `AppView`: Pointer to an existing view that you want to use as your FeatureManager design tree view. If you do not have an existing view, then use [IModelViewMgr::CreateFeatureMgrView2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.html), which returns a view handle
- `ToolTip`: ToolTip string
- `WhichPane`: Pane in which to add the view as defined in [swFeatMgrPane_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html)

### Return Value

True if the FeatureManager design tree view tab is added successfully, false if not

## VBA Syntax

See [ModelDoc2::AddFeatureMgrView3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~AddFeatureMgrView3.html).

## Remarks

**All applications are required to be compatible with SOLIDWORKS x64. You must replace all calls to 32-bit only APIs with calls to their 64-bit safe counterparts.**

See [Eliminating 32-bit only API use](sldworksapiprogguide.chm::/Overview/Eliminating_32-Bit_Only_API_Use.htm) for more information.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDocExtension::AddFeatureMgrView3x64 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddFeatureMgrView3x64.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
