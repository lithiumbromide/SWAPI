---
title: "PrintFile Property (IPrintSpecification)"
project: "SOLIDWORKS API Help"
interface: "IPrintSpecification"
member: "PrintFile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~PrintFile.html"
---

# PrintFile Property (IPrintSpecification)

Gets or sets the path and file name to which to print the document.

## Syntax

### Visual Basic (Declaration)

```vb
Property PrintFile As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPrintSpecification
Dim value As System.String

instance.PrintFile = value

value = instance.PrintFile
```

### C#

```csharp
System.string PrintFile {get; set;}
```

### C++/CLI

```cpp
property System.String^ PrintFile {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

File name; default file name is **output.prn**

## VBA Syntax

See [PrintSpecification::PrintFile](ms-its:sldworksapivb6.chm::/sldworks~PrintSpecification~PrintFile.html).

## Remarks

This property is valid only if [IPrintSpecification::PrintToFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~PrintToFile.html) is set to true.

## See Also

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.html)
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
