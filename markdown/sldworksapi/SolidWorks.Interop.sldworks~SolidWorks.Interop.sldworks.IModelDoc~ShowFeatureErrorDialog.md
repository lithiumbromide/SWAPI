---
title: "ShowFeatureErrorDialog Property (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ShowFeatureErrorDialog"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ShowFeatureErrorDialog.html"
---

# ShowFeatureErrorDialog Property (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ShowFeatureErrorDialog](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ShowFeatureErrorDialog.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowFeatureErrorDialog As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim value As System.Boolean

instance.ShowFeatureErrorDialog = value

value = instance.ShowFeatureErrorDialog
```

### C#

```csharp
System.bool ShowFeatureErrorDialog {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowFeatureErrorDialog {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc::ShowFeatureErrorDialog](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ShowFeatureErrorDialog.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
