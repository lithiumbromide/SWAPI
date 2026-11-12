---
title: "SheetName Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "SheetName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~SheetName.html"
---

# SheetName Property (IDocumentSpecification)

Gets or sets the name of the sheet in a drawing document to open.

## Syntax

### Visual Basic (Declaration)

```vb
Property SheetName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.String

instance.SheetName = value

value = instance.SheetName
```

### C#

```csharp
System.string SheetName {get; set;}
```

### C++/CLI

```cpp
property System.String^ SheetName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Sheet name

## VBA Syntax

See [DocumentSpecification::SheetName](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~SheetName.html).

## Examples

[Open Specified Sheet in Drawing Document (VB.NET)](Open_Specified_Sheet_in_Drawing_Document_Example_VBNET.htm)
[Open Specified Sheet in Drawing Document (VBA)](Open_Specified_Sheet_in_Drawing_Document_Example_VB.htm)
[Open Specified Sheet in Drawing Document (C#)](Open_Specified_Sheet_in_Drawing_Document_Example_CSharp.htm)

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)

## Availability

SOLIDWORKS 2009 SP4, Revision Number 17.4
