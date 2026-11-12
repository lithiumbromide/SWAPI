---
title: "DeActivateFeatureMgrView Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "DeActivateFeatureMgrView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeActivateFeatureMgrView.html"
---

# DeActivateFeatureMgrView Method (IModelDoc2)

Deactivates a tab in the FeatureManager design tree view.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeActivateFeatureMgrView( _
   ByRef AppView As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim AppView As System.Integer
Dim value As System.Boolean

value = instance.DeActivateFeatureMgrView(AppView)
```

### C#

```csharp
System.bool DeActivateFeatureMgrView(
   ref System.int AppView
)
```

### C++/CLI

```cpp
System.bool DeActivateFeatureMgrView(
   System.int% AppView
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AppView`: Pointer to the FeatureManager design tree view

### Return Value

True if deactivated, false if not

## VBA Syntax

See [ModelDoc2::DeActivateFeatureMgrView](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~DeActivateFeatureMgrView.html).

## Remarks

This method is valid only for x86 applications.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::AddFeatureMgrView3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddFeatureMgrView3.html)
[IModelDocExtension::DeActivateFeatureMgrViewx64 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeActivateFeatureMgrViewx64.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
