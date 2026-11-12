---
title: "LoadModel Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "LoadModel"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~LoadModel.html"
---

# LoadModel Property (IDocumentSpecification)

Gets or sets whether to load the model if the document is a detached drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Property LoadModel As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.Boolean

instance.LoadModel = value

value = instance.LoadModel
```

### C#

```csharp
System.bool LoadModel {get; set;}
```

### C++/CLI

```cpp
property System.bool LoadModel {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to load the model, false to not

## VBA Syntax

See [DocumentSpecification::LoadModel](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~LoadModel.html).

## Remarks

To avoid a warning when opening shaded modes in views, set this property to TRUE so that the view is automatically loaded in shaded.

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
