---
title: "ResponseAText Property (IMessageBarDefinition)"
project: "SOLIDWORKS API Help"
interface: "IMessageBarDefinition"
member: "ResponseAText"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition~ResponseAText.html"
---

# ResponseAText Property (IMessageBarDefinition)

Gets or sets the text displayed on the first button or command link of this message bar.

## Syntax

### Visual Basic (Declaration)

```vb
Property ResponseAText As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IMessageBarDefinition
Dim value As System.String

instance.ResponseAText = value

value = instance.ResponseAText
```

### C#

```csharp
System.string ResponseAText {get; set;}
```

### C++/CLI

```cpp
property System.String^ ResponseAText {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text displayed on first user response control; default is an empty string

## VBA Syntax

See [MessageBarDefinition::ResponseAText](ms-its:sldworksapivb6.chm::/sldworks~MessageBarDefinition~ResponseAText.html).

## Examples

See the [IMessageBarHandler](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler.html) examples.

## Remarks

This property must be set to a non-empty string if [IMessageBarDefinition::ResponseAType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition~ResponseAType.html) is not [swUserMessageBarResponseType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserMessageBarResponseType_e.html).swUserMessageBarResponseType_None.

## See Also

[IMessageBarDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition.html)
[IMessageBarDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
