---
title: "ActivePrinter Property (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ActivePrinter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivePrinter.html"
---

# ActivePrinter Property (ISldWorks)

Obsolete. Superseded by [IModelDoc2::Printer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~Printer.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property ActivePrinter As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.String

instance.ActivePrinter = value

value = instance.ActivePrinter
```

### C#

```csharp
System.string ActivePrinter {get; set;}
```

### C++/CLI

```cpp
property System.String^ ActivePrinter {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [SldWorks::ActivePrinter](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~ActivePrinter.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
