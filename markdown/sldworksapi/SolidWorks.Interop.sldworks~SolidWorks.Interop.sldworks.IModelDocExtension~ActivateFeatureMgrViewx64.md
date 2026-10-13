---
title: "ActivateFeatureMgrViewx64 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "ActivateFeatureMgrViewx64"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ActivateFeatureMgrViewx64.html"
---

# ActivateFeatureMgrViewx64 Method (IModelDocExtension)

Activates the specified FeatureManager view in x64 applications.

## Syntax

### Visual Basic (Declaration)

```vb
Function ActivateFeatureMgrViewx64( _
   ByRef AppView As System.Long _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim AppView As System.Long
Dim value As System.Integer

value = instance.ActivateFeatureMgrViewx64(AppView)
```

### C#

```csharp
System.int ActivateFeatureMgrViewx64(
   ref System.long AppView
)
```

### C++/CLI

```cpp
System.int ActivateFeatureMgrViewx64(
   System.int64% AppView
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AppView`: Pointer to a FeatureManager design tree view

### Return Value

Pane as defined by [swFeatMgrPane_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html) where the view resides

## VBA Syntax

See [ModelDocExtension::ActivateFeatureMgrViewx64](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~ActivateFeatureMgrViewx64.html).

## Remarks

See [IFeatMgrView::ActivateView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~ActivateView.html) for examples you can tailor to use this method in x64 applications.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2026 SP01, Revision Number 34.1
