---
title: "IncludeDoNotShowAgain Property (IMessageBarDefinition)"
project: "SOLIDWORKS API Help"
interface: "IMessageBarDefinition"
member: "IncludeDoNotShowAgain"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition~IncludeDoNotShowAgain.html"
---

# IncludeDoNotShowAgain Property (IMessageBarDefinition)

Gets or sets whether to display the "Do not show again" check box for this message bar.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeDoNotShowAgain As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMessageBarDefinition
Dim value As System.Boolean

instance.IncludeDoNotShowAgain = value

value = instance.IncludeDoNotShowAgain
```

### C#

```csharp
System.bool IncludeDoNotShowAgain {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeDoNotShowAgain {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True (default) to display the check box, false to not.

## VBA Syntax

See [MessageBarDefinition::IncludeDoNotShowAgain](ms-its:sldworksapivb6.chm::/sldworks~MessageBarDefinition~IncludeDoNotShowAgain.html).

## See Also

[IMessageBarDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition.html)
[IMessageBarDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
