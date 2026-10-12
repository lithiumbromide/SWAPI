---
title: "type Property (ISwDMConfiguration13)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration13"
member: "type"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration13~type.html"
---

# type Property (ISwDMConfiguration13)

Gets the type of this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration13
Dim value As System.Integer

value = instance.type
```

### C#

```csharp
System.int type {get;}
```

### C++/CLI

```cpp
property System.int type {
   System.int get();
}
```

### Property Value

Configuration type as defined in [swDmConfigurationType](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmConfigurationType.html)

## VBA Syntax

See [SwDMConfiguration13::type](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration13~type.html).

## Examples

[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)
[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)

## See Also

[ISwDMConfiguration13 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration13.html)
[ISwDMConfiguration13 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration13_members.html)

## Availability

SOLIDWORKS Document Manager API 2010 SP05
