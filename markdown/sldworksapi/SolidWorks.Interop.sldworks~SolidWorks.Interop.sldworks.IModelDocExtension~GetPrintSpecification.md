---
title: "GetPrintSpecification Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetPrintSpecification"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPrintSpecification.html"
---

# GetPrintSpecification Method (IModelDocExtension)

Gets the IPrintSpecification object for this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPrintSpecification() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Object

value = instance.GetPrintSpecification()
```

### C#

```csharp
System.object GetPrintSpecification()
```

### C++/CLI

```cpp
System.Object^ GetPrintSpecification();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IPrintSpecification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPrintSpecification.html)

## VBA Syntax

See [ModelDocExtension::GetPrintSpecification](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetPrintSpecification.html).

## Examples

[Print Drawing (VBA)](Print_Drawing_as_High_Quality_Example_VB.htm)
[Print Drawing (VB.NET)](Print_Drawing_as_High_Quality_Example_VBNET.htm)
[Print Drawing (C#)](Print_Drawing_as_High_Quality_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::PrintOut4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PrintOut4.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
