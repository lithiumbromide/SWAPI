---
title: "Title Property (IMessageBarDefinition)"
project: "SOLIDWORKS API Help"
interface: "IMessageBarDefinition"
member: "Title"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition~Title.html"
---

# Title Property (IMessageBarDefinition)

Gets or sets the title of this message bar.

## Syntax

### Visual Basic (Declaration)

```vb
Property Title As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IMessageBarDefinition
Dim value As System.String

instance.Title = value

value = instance.Title
```

### C#

```csharp
System.string Title {get; set;}
```

### C++/CLI

```cpp
property System.String^ Title {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Non-empty title string

## VBA Syntax

See [MessageBarDefinition::Title](ms-its:sldworksapivb6.chm::/sldworks~MessageBarDefinition~Title.html).

## Examples

See the [IMessageBarHandler](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler.html) examples.

## Remarks

This property must be set.

## See Also

[IMessageBarDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition.html)
[IMessageBarDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
