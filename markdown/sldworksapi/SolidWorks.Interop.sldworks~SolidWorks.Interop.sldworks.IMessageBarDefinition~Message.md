---
title: "Message Property (IMessageBarDefinition)"
project: "SOLIDWORKS API Help"
interface: "IMessageBarDefinition"
member: "Message"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition~Message.html"
---

# Message Property (IMessageBarDefinition)

Gets or sets the message displayed on this message bar.

## Syntax

### Visual Basic (Declaration)

```vb
Property Message As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IMessageBarDefinition
Dim value As System.String

instance.Message = value

value = instance.Message
```

### C#

```csharp
System.string Message {get; set;}
```

### C++/CLI

```cpp
property System.String^ Message {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Non-empty message string

## VBA Syntax

See [MessageBarDefinition::Message](ms-its:sldworksapivb6.chm::/sldworks~MessageBarDefinition~Message.html).

## Remarks

This property must be set.

## See Also

[IMessageBarDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition.html)
[IMessageBarDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
