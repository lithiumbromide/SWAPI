---
title: "DeActivateFeatureMgrView Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "DeActivateFeatureMgrView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~DeActivateFeatureMgrView.html"
---

# DeActivateFeatureMgrView Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::DeActivateFeatureMgrView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~DeActivateFeatureMgrView.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function DeActivateFeatureMgrView( _
   ByRef AppView As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
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

- `AppView`:

## VBA Syntax

See [ModelDoc::DeActivateFeatureMgrView](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~DeActivateFeatureMgrView.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
