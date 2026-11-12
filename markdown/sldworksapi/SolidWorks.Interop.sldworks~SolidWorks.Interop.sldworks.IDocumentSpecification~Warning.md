---
title: "Warning Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "Warning"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Warning.html"
---

# Warning Property (IDocumentSpecification)

Gets or sets any file load warnings when opening a model document.

## Syntax

### Visual Basic (Declaration)

```vb
Property Warning As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.Integer

instance.Warning = value

value = instance.Warning
```

### C#

```csharp
System.int Warning {get; set;}
```

### C++/CLI

```cpp
property System.int Warning {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Warnings as defined by [swFileLoadWarning_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileLoadWarning_e.html)

## VBA Syntax

See [DocumentSpecification::Warning](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~Warning.html).

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
