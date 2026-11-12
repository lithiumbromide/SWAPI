---
title: "Visible Property (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "Visible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~Visible.html"
---

# Visible Property (IModelDoc)

Obsolete. Superseded by [IModelDoc2::Visible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~Visible.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Visible As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim value As System.Boolean

instance.Visible = value

value = instance.Visible
```

### C#

```csharp
System.bool Visible {get; set;}
```

### C++/CLI

```cpp
property System.bool Visible {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc::Visible](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~Visible.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
