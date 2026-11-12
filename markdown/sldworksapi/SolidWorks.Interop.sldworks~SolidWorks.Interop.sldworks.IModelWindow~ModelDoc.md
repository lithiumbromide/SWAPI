---
title: "ModelDoc Property (IModelWindow)"
project: "SOLIDWORKS API Help"
interface: "IModelWindow"
member: "ModelDoc"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow~ModelDoc.html"
---

# ModelDoc Property (IModelWindow)

Gets the model document in this model window.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ModelDoc As ModelDoc2
```

### Visual Basic (Usage)

```vb
Dim instance As IModelWindow
Dim value As ModelDoc2

value = instance.ModelDoc
```

### C#

```csharp
ModelDoc2 ModelDoc {get;}
```

### C++/CLI

```cpp
property ModelDoc2^ ModelDoc {
   ModelDoc2^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Model document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) in this model window

## VBA Syntax

See [ModelWindow::ModelDoc](ms-its:sldworksapivb6.chm::/sldworks~ModelWindow~ModelDoc.html).

## Examples

[Switch Documents (C#)](Switch_Documents_Example_CSharp.htm)
[Switch Documents (VB.NET)](Switch_Documents_Example_VBNET.htm)
[Switch Documents (VBA)](Switch_Documents_Example_VB.htm)

## See Also

[IModelWindow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow.html)
[IModelWindow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
