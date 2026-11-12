---
title: "ShowMessageBar Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "ShowMessageBar"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ShowMessageBar.html"
---

# ShowMessageBar Method (IModelDocExtension)

Shows the specified message bar in this document's window.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowMessageBar( _
   ByVal Definition As System.Object, _
   ByVal Handler As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Definition As System.Object
Dim Handler As System.Object
Dim value As System.Integer

value = instance.ShowMessageBar(Definition, Handler)
```

### C#

```csharp
System.int ShowMessageBar(
   System.object Definition,
   System.object Handler
)
```

### C++/CLI

```cpp
System.int ShowMessageBar(
   System.Object^ Definition,
   System.Object^ Handler
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Definition`: [IMessageBarDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition.html)
- `Handler`: [IMessageBarHandler](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler.html)

### Return Value

Result code as defined by [swShowMessageBarResult_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swShowMessageBarResult_e.html)

## VBA Syntax

See [ModelDocExtension::ShowMessageBar](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~ShowMessageBar.html).

## Examples

See the [IMessageBarHandler](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler.html) examples.

## Remarks

This method is called by an add-in to display the specified message bar in this document's window.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
