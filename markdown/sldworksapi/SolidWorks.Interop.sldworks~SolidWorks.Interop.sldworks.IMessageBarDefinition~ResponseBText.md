---
title: "ResponseBText Property (IMessageBarDefinition)"
project: "SOLIDWORKS API Help"
interface: "IMessageBarDefinition"
member: "ResponseBText"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition~ResponseBText.html"
---

# ResponseBText Property (IMessageBarDefinition)

Gets or sets the text displayed on the second button or command link of this message bar.

## Syntax

### Visual Basic (Declaration)

```vb
Property ResponseBText As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IMessageBarDefinition
Dim value As System.String

instance.ResponseBText = value

value = instance.ResponseBText
```

### C#

```csharp
System.string ResponseBText {get; set;}
```

### C++/CLI

```cpp
property System.String^ ResponseBText {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text displayed on second user response control; default is an empty string

## VBA Syntax

See [MessageBarDefinition::ResponseBText](ms-its:sldworksapivb6.chm::/sldworks~MessageBarDefinition~ResponseBText.html).

## Remarks

This property must be set to a non-empty string if [IMessageBarDefinition::ResponseBType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition~ResponseBType.html) is not [swUserMessageBarResponseType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserMessageBarResponseType_e.html).swUserMessageBarResponseType_None.

## See Also

[IMessageBarDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition.html)
[IMessageBarDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
