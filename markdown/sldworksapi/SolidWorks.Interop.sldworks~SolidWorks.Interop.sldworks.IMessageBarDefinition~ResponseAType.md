---
title: "ResponseAType Property (IMessageBarDefinition)"
project: "SOLIDWORKS API Help"
interface: "IMessageBarDefinition"
member: "ResponseAType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition~ResponseAType.html"
---

# ResponseAType Property (IMessageBarDefinition)

Gets or sets the first response user control for this message bar.

## Syntax

### Visual Basic (Declaration)

```vb
Property ResponseAType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMessageBarDefinition
Dim value As System.Integer

instance.ResponseAType = value

value = instance.ResponseAType
```

### C#

```csharp
System.int ResponseAType {get; set;}
```

### C++/CLI

```cpp
property System.int ResponseAType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

First response user control as defined by [swUserMessageBarResponseType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserMessageBarResponseType_e.html)

## VBA Syntax

See [MessageBarDefinition::ResponseAType](ms-its:sldworksapivb6.chm::/sldworks~MessageBarDefinition~ResponseAType.html).

## Examples

See the [IMessageBarHandler](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler.html) examples.

## Remarks

Default value of this property is swUserMessageBarResponseType_e.swUserMessageBarResponseType_None.

## See Also

[IMessageBarDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition.html)
[IMessageBarDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
