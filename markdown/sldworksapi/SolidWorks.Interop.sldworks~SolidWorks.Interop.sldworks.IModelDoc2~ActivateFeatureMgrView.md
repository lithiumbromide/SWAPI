---
title: "ActivateFeatureMgrView Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ActivateFeatureMgrView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ActivateFeatureMgrView.html"
---

# ActivateFeatureMgrView Method (IModelDoc2)

Obsolete. Superseded by [IFeatureMgrView::ActivateView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatMgrView~ActivateView.html) or [IModelDocExtension::ActivateFeatureMgrViewx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ActivateFeatureMgrViewx64.html).

This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016.

The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used.

## Syntax

### Visual Basic (Declaration)

```vb
Function ActivateFeatureMgrView( _
   ByRef AppView As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim AppView As System.Integer
Dim value As System.Integer

value = instance.ActivateFeatureMgrView(AppView)
```

### C#

```csharp
System.int ActivateFeatureMgrView(
   ref System.int AppView
)
```

### C++/CLI

```cpp
System.int ActivateFeatureMgrView(
   System.int% AppView
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AppView`:

## VBA Syntax

See [ModelDoc2::ActivateFeatureMgrView](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ActivateFeatureMgrView.html).

## Remarks

**All applications are required to be compatible with SOLIDWORKS x64. You must replace all calls to 32-bit only APIs with calls to their 64-bit safe counterparts.**

See [Eliminating 32-bit only API use](sldworksapiprogguide.chm::/Overview/Eliminating_32-Bit_Only_API_Use.htm) for more information.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
