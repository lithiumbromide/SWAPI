---
title: "Severity Property (IMessageBarDefinition)"
project: "SOLIDWORKS API Help"
interface: "IMessageBarDefinition"
member: "Severity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition~Severity.html"
---

# Severity Property (IMessageBarDefinition)

Gets or sets the severity level of this message bar.

## Syntax

### Visual Basic (Declaration)

```vb
Property Severity As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMessageBarDefinition
Dim value As System.Integer

instance.Severity = value

value = instance.Severity
```

### C#

```csharp
System.int Severity {get; set;}
```

### C++/CLI

```cpp
property System.int Severity {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Severity level as defined by [swUserMessageBarSeverity_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserMessageBarSeverity_e.html)

## VBA Syntax

See [MessageBarDefinition::Severity](ms-its:sldworksapivb6.chm::/sldworks~MessageBarDefinition~Severity.html).

## Examples

See the [IMessageBarHandler](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler.html) examples.

## Remarks

The default value of this property is swUserMessageBarSeverity_e.swUserMessageBarSeverity_Information.

## See Also

[IMessageBarDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition.html)
[IMessageBarDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
