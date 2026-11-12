---
title: "Error Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "Error"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Error.html"
---

# Error Property (IDocumentSpecification)

Gets or sets the file load errors when opening a model document.

## Syntax

### Visual Basic (Declaration)

```vb
Property Error As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.Integer

instance.Error = value

value = instance.Error
```

### C#

```csharp
System.int Error {get; set;}
```

### C++/CLI

```cpp
property System.int Error {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

File load errors as defined by [swFileLoadError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileLoadError_e.html)

## VBA Syntax

See [DocumentSpecification::Error](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~Error.html).

## Examples

[Open Drawing Document Read-only (VBA)](Open_Drawing_Document_Read-only_Example_VB.htm)
[Open Assembly Document (C#)](Open_Assembly_Document_Example_CSharp.htm)
[Open Assembly Document (VB.NET)](Open_Assembly_Document_Example_VBNET.htm)
[Open Assembly Document (VBA)](Open_Assembly_Document_Example_VB.htm)

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
