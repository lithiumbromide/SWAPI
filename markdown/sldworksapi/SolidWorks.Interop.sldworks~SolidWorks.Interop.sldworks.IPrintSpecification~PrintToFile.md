---
title: "PrintToFile Property (IPrintSpecification)"
project: "SOLIDWORKS API Help"
interface: "IPrintSpecification"
member: "PrintToFile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~PrintToFile.html"
---

# PrintToFile Property (IPrintSpecification)

Gets or sets whether to print to a file.

## Syntax

### Visual Basic (Declaration)

```vb
Property PrintToFile As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPrintSpecification
Dim value As System.Boolean

instance.PrintToFile = value

value = instance.PrintToFile
```

### C#

```csharp
System.bool PrintToFile {get; set;}
```

### C++/CLI

```cpp
property System.bool PrintToFile {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to print to a file, false to print to a [printer queue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~PrinterQueue.html)

## VBA Syntax

See [PrintSpecification::PrintToFile](ms-its:sldworksapivb6.chm::/sldworks~PrintSpecification~PrintToFile.html).

## See Also

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.html)
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
