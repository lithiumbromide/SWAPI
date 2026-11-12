---
title: "DefineMessageBar Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "DefineMessageBar"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DefineMessageBar.html"
---

# DefineMessageBar Method (ISldWorks)

Called by a SOLIDWORKS add-in, creates a message bar definition object.

## Syntax

### Visual Basic (Declaration)

```vb
Function DefineMessageBar( _
   ByVal UniqueName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim UniqueName As System.String
Dim value As System.Object

value = instance.DefineMessageBar(UniqueName)
```

### C#

```csharp
System.object DefineMessageBar(
   System.string UniqueName
)
```

### C++/CLI

```cpp
System.Object^ DefineMessageBar(
   System.String^ UniqueName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UniqueName`: Unique ID of this message bar

### Return Value

[IMessageBarDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition.html)

## VBA Syntax

See [SldWorks::DefineMessageBar](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~DefineMessageBar.html).

## Examples

See the [IMessageBarHandler](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler.html) examples.

## Remarks

It is the add-in's responsibility to ensure that the ID is unique by using, for example, a combination of add-in module name and unique message identifier:

"MyAddInName+ID_MYMESSAGE1"

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
