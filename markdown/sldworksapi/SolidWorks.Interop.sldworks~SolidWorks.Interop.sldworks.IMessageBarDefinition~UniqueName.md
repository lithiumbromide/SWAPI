---
title: "UniqueName Property (IMessageBarDefinition)"
project: "SOLIDWORKS API Help"
interface: "IMessageBarDefinition"
member: "UniqueName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition~UniqueName.html"
---

# UniqueName Property (IMessageBarDefinition)

Gets the ID of this message bar.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property UniqueName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IMessageBarDefinition
Dim value As System.String

value = instance.UniqueName
```

### C#

```csharp
System.string UniqueName {get;}
```

### C++/CLI

```cpp
property System.String^ UniqueName {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Unique ID of this message bar

## VBA Syntax

See [MessageBarDefinition::UniqueName](ms-its:sldworksapivb6.chm::/sldworks~MessageBarDefinition~UniqueName.html).

## Remarks

The ID is defined by the add-in in its call to [ISldWorks::DefineMessageBar](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DefineMessageBar.html).

It is the add-in's responsibility to ensure that the ID is unique by using, for example, a combination of add-in module name and unique message identifier:

"MyAddInName+ID_MYMESSAGE1"

## See Also

[IMessageBarDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition.html)
[IMessageBarDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
