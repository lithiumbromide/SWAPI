---
title: "Query Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "Query"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Query.html"
---

# Query Property (IDocumentSpecification)

Gets or sets whether the options passed during a document's open, load, and save can be retrieved by this API.

## Syntax

### Visual Basic (Declaration)

```vb
Property Query As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.Boolean

instance.Query = value

value = instance.Query
```

### C#

```csharp
System.bool Query {get; set;}
```

### C++/CLI

```cpp
property System.bool Query {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to retrieve options, false to not (default)

## VBA Syntax

See [DocumentSpecification::Query](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~Query.html).

## Remarks

Various options can be passed to document operation APIs such as [IModelDoc2::Save3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~Save3.html), [IModelDocExtension::SaveAs4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SaveAs4.html), and [ISldWorks::LoadFile4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~LoadFile4.html). These options can be retrieved from the document, if Query is set to true. Only silent information can be retrieved.

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
